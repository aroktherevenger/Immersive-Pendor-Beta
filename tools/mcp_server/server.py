"""
Pendor INI + Game File MCP Server
Tools for Claude to read/modify PoP config files and compiled game text files,
with a tweak registry that tracks every change and detects conflicts.
"""

import json
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

import ini_handler as ini
import game_file_handler as gfh
import tweak_registry as registry

app = Server("pendor-ini")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        # ── INI file tools ────────────────────────────────────────────────────
        Tool(
            name="list_ini_files",
            description="List all known INI config files for PoP and their paths.",
            inputSchema={"type": "object", "properties": {}, "required": []},
        ),
        Tool(
            name="read_module_ini",
            description="Read all settings from module.ini (PoP gameplay tweaks).",
            inputSchema={"type": "object", "properties": {}, "required": []},
        ),
        Tool(
            name="read_rgl_config",
            description=(
                "Read settings from rgl_config.ini (engine/graphics/battle settings). "
                "Optionally filter by section name (e.g. 'Battle', 'Campaign', 'Graphics')."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "section": {
                        "type": "string",
                        "description": "Section name to filter by (e.g. 'Battle', 'Campaign').",
                    }
                },
                "required": [],
            },
        ),
        Tool(
            name="update_module_ini",
            description="Update a setting in module.ini. Auto-backs up before changing.",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "Setting name, e.g. 'battle_size_max'"},
                    "value": {"type": "string", "description": "New value to set"},
                },
                "required": ["key", "value"],
            },
        ),
        Tool(
            name="update_rgl_config",
            description="Update a setting in rgl_config.ini. Auto-backs up before changing.",
            inputSchema={
                "type": "object",
                "properties": {
                    "section": {"type": "string", "description": "Section name, e.g. 'Battle'"},
                    "key": {"type": "string", "description": "Setting key, e.g. 'iBattleSizeMax'"},
                    "value": {"type": "string", "description": "New value"},
                },
                "required": ["section", "key", "value"],
            },
        ),
        Tool(
            name="search_ini_settings",
            description="Search for a keyword across all INI files.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Keyword, e.g. 'battle', 'xp', 'damage'"},
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="list_ini_backups",
            description="List available INI backups. Filter by 'module' or 'rgl_config'.",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_key": {
                        "type": "string",
                        "enum": ["module", "rgl_config"],
                    }
                },
                "required": [],
            },
        ),
        Tool(
            name="restore_ini_backup",
            description="Restore an INI file from a backup. Backs up current file first.",
            inputSchema={
                "type": "object",
                "properties": {
                    "backup_path": {"type": "string"},
                    "file_key": {"type": "string", "enum": ["module", "rgl_config"]},
                },
                "required": ["backup_path", "file_key"],
            },
        ),

        # ── Game text file tools ──────────────────────────────────────────────
        Tool(
            name="list_game_files",
            description=(
                "List all known PoP compiled game text files that can be tweaked "
                "(scripts.txt, conversation.txt, troops.txt, etc.)."
            ),
            inputSchema={"type": "object", "properties": {}, "required": []},
        ),
        Tool(
            name="search_game_file",
            description=(
                "Search for a pattern in a PoP game text file. "
                "Returns matching lines with surrounding context. "
                "Use this before applying a tweak to confirm the text exists."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "file_key": {
                        "type": "string",
                        "description": "File to search, e.g. 'scripts', 'conversation', 'troops'",
                    },
                    "pattern": {
                        "type": "string",
                        "description": "Text or regex pattern to search for",
                    },
                    "context_lines": {
                        "type": "integer",
                        "description": "Lines of context to show around each match (default 3)",
                    },
                },
                "required": ["file_key", "pattern"],
            },
        ),
        Tool(
            name="read_game_file_lines",
            description="Read a specific line range from a PoP game text file.",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_key": {"type": "string", "description": "File key, e.g. 'scripts'"},
                    "start_line": {"type": "integer"},
                    "end_line": {"type": "integer"},
                },
                "required": ["file_key", "start_line", "end_line"],
            },
        ),
        Tool(
            name="apply_tweak",
            description=(
                "Apply a wiki tweak to a PoP game text file by replacing a specific text. "
                "Automatically: backs up the file, checks for conflicts with previously "
                "applied tweaks, and records the change in the registry. "
                "Always search_game_file first to confirm the text exists and get exact wording."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "tweak_id": {
                        "type": "string",
                        "description": "Short unique ID for this tweak, e.g. '1c_spawn_rate'",
                    },
                    "tweak_name": {
                        "type": "string",
                        "description": "Human-readable name, e.g. 'Tweak 1c - Spawn Rate and Delay'",
                    },
                    "file_key": {
                        "type": "string",
                        "description": "File to modify, e.g. 'scripts', 'conversation'",
                    },
                    "search_text": {
                        "type": "string",
                        "description": "Exact text to find in the file",
                    },
                    "replacement_text": {
                        "type": "string",
                        "description": "Text to replace it with",
                    },
                    "notes": {
                        "type": "string",
                        "description": "Optional notes about what this tweak does",
                    },
                    "wiki_ref": {
                        "type": "string",
                        "description": "Wiki reference, e.g. 'Tweaks page, Tweak 1c'",
                    },
                    "occurrence": {
                        "type": "integer",
                        "description": "Which occurrence to replace: 1=first, 0=all (default: 1)",
                    },
                },
                "required": ["tweak_id", "tweak_name", "file_key",
                             "search_text", "replacement_text"],
            },
        ),
        Tool(
            name="revert_tweak",
            description=(
                "Revert a previously applied tweak back to its original text. "
                "Backs up the current file first, then removes the entry from the registry."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "tweak_id": {
                        "type": "string",
                        "description": "The tweak ID to revert, e.g. '1c_spawn_rate'",
                    },
                },
                "required": ["tweak_id"],
            },
        ),

        # ── Tweak registry tools ──────────────────────────────────────────────
        Tool(
            name="list_applied_tweaks",
            description=(
                "List all tweaks that have been applied to the game files, "
                "optionally filtered by file name. Shows what's been changed and when."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "file_filter": {
                        "type": "string",
                        "description": "Optional file name filter, e.g. 'scripts' or 'conversation'",
                    },
                },
                "required": [],
            },
        ),
        Tool(
            name="tweaks_by_file",
            description="Show a summary of all applied tweaks grouped by which file they modified.",
            inputSchema={"type": "object", "properties": {}, "required": []},
        ),
        Tool(
            name="check_tweak_conflicts",
            description=(
                "Check whether a planned tweak would conflict with previously applied tweaks "
                "before actually applying it."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "file_key": {"type": "string", "description": "File to check"},
                    "search_text": {"type": "string", "description": "Text the new tweak would search for"},
                },
                "required": ["file_key", "search_text"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    try:
        # ── INI tools ─────────────────────────────────────────────────────────
        if name == "list_ini_files":
            return [TextContent(type="text",
                                text=json.dumps(ini.INI_FILES, indent=2))]

        elif name == "read_module_ini":
            return [TextContent(type="text",
                                text=json.dumps(ini.read_module_ini(), indent=2))]

        elif name == "read_rgl_config":
            data = ini.read_rgl_config(arguments.get("section"))
            return [TextContent(type="text", text=json.dumps(data, indent=2))]

        elif name == "update_module_ini":
            backup = ini.update_module_ini(arguments["key"], arguments["value"])
            return [TextContent(type="text", text=json.dumps({
                "success": True, "key": arguments["key"],
                "new_value": arguments["value"], "backup": backup,
            }, indent=2))]

        elif name == "update_rgl_config":
            backup = ini.update_rgl_config(
                arguments["section"], arguments["key"], arguments["value"])
            return [TextContent(type="text", text=json.dumps({
                "success": True, "section": arguments["section"],
                "key": arguments["key"], "new_value": arguments["value"],
                "backup": backup,
            }, indent=2))]

        elif name == "search_ini_settings":
            return [TextContent(type="text",
                                text=json.dumps(ini.search_settings(arguments["query"]), indent=2))]

        elif name == "list_ini_backups":
            backups = ini.list_backups(arguments.get("file_key"))
            return [TextContent(type="text", text=json.dumps(backups, indent=2))]

        elif name == "restore_ini_backup":
            dst = ini.restore_backup(arguments["backup_path"], arguments["file_key"])
            return [TextContent(type="text", text=json.dumps(
                {"success": True, "restored_to": dst}, indent=2))]

        # ── Game file tools ───────────────────────────────────────────────────
        elif name == "list_game_files":
            return [TextContent(type="text",
                                text=json.dumps(gfh.GAME_FILES, indent=2))]

        elif name == "search_game_file":
            results = gfh.search_in_file(
                arguments["file_key"],
                arguments["pattern"],
                arguments.get("context_lines", 3),
            )
            return [TextContent(type="text", text=json.dumps(results, indent=2))]

        elif name == "read_game_file_lines":
            lines = gfh.read_lines(
                arguments["file_key"],
                arguments["start_line"],
                arguments["end_line"],
            )
            return [TextContent(type="text", text=json.dumps(lines, indent=2))]

        elif name == "apply_tweak":
            result = gfh.apply_tweak(
                tweak_id=arguments["tweak_id"],
                tweak_name=arguments["tweak_name"],
                file_key=arguments["file_key"],
                search_text=arguments["search_text"],
                replacement_text=arguments["replacement_text"],
                notes=arguments.get("notes", ""),
                wiki_ref=arguments.get("wiki_ref", ""),
                occurrence=arguments.get("occurrence", 1),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "revert_tweak":
            result = gfh.revert_tweak(arguments["tweak_id"])
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        # ── Registry tools ────────────────────────────────────────────────────
        elif name == "list_applied_tweaks":
            tweaks = registry.list_tweaks(arguments.get("file_filter"))
            return [TextContent(type="text", text=json.dumps(tweaks, indent=2))]

        elif name == "tweaks_by_file":
            summary = registry.summarize_by_file()
            return [TextContent(type="text", text=json.dumps(summary, indent=2))]

        elif name == "check_tweak_conflicts":
            path = gfh.resolve_file(arguments["file_key"])
            conflicts = registry.check_conflicts(path, arguments["search_text"])
            return [TextContent(type="text", text=json.dumps({
                "conflicts_found": len(conflicts),
                "conflicts": conflicts,
            }, indent=2))]

        else:
            return [TextContent(type="text",
                                text=json.dumps({"error": f"Unknown tool: {name}"}))]

    except Exception as e:
        return [TextContent(type="text", text=json.dumps({
            "error": str(e), "type": type(e).__name__,
        }, indent=2))]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream,
                      app.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
