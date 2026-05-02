"""
Pendor INI MCP Server
Exposes tools for Claude to read and modify M&B Warband / PoP config files.
"""

import json
import sys
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

import ini_handler as ini

app = Server("pendor-ini")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
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
                        "description": "Optional section name to filter by (e.g. 'Battle', 'Campaign').",
                    }
                },
                "required": [],
            },
        ),
        Tool(
            name="update_module_ini",
            description=(
                "Update a setting in module.ini. Automatically creates a backup before changing. "
                "Example: key='battle_size_max', value='600'"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "The setting name, e.g. 'battle_size_max'"},
                    "value": {"type": "string", "description": "The new value to set"},
                },
                "required": ["key", "value"],
            },
        ),
        Tool(
            name="update_rgl_config",
            description=(
                "Update a setting in rgl_config.ini. Automatically creates a backup before changing. "
                "Example: section='Battle', key='iBattleSizeMax', value='600'"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "section": {"type": "string", "description": "The section name, e.g. 'Battle'"},
                    "key": {"type": "string", "description": "The setting key, e.g. 'iBattleSizeMax'"},
                    "value": {"type": "string", "description": "The new value to set"},
                },
                "required": ["section", "key", "value"],
            },
        ),
        Tool(
            name="search_settings",
            description="Search for a keyword across all INI files. Returns matching settings from both files.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Keyword to search for, e.g. 'battle', 'xp', 'damage'"},
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="list_backups",
            description="List available backups. Optionally filter by file ('module' or 'rgl_config').",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_key": {
                        "type": "string",
                        "enum": ["module", "rgl_config"],
                        "description": "Which file's backups to list (omit for all).",
                    }
                },
                "required": [],
            },
        ),
        Tool(
            name="restore_backup",
            description="Restore an INI file from a backup. Backs up the current file first.",
            inputSchema={
                "type": "object",
                "properties": {
                    "backup_path": {"type": "string", "description": "Full path to the backup file to restore"},
                    "file_key": {
                        "type": "string",
                        "enum": ["module", "rgl_config"],
                        "description": "Which file to restore ('module' or 'rgl_config')",
                    },
                },
                "required": ["backup_path", "file_key"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    try:
        if name == "list_ini_files":
            result = {k: v for k, v in ini.INI_FILES.items()}
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "read_module_ini":
            data = ini.read_module_ini()
            return [TextContent(type="text", text=json.dumps(data, indent=2))]

        elif name == "read_rgl_config":
            section = arguments.get("section")
            data = ini.read_rgl_config(section)
            return [TextContent(type="text", text=json.dumps(data, indent=2))]

        elif name == "update_module_ini":
            key = arguments["key"]
            value = arguments["value"]
            backup = ini.update_module_ini(key, value)
            return [TextContent(type="text", text=json.dumps({
                "success": True,
                "key": key,
                "new_value": value,
                "backup_created": backup,
            }, indent=2))]

        elif name == "update_rgl_config":
            section = arguments["section"]
            key = arguments["key"]
            value = arguments["value"]
            backup = ini.update_rgl_config(section, key, value)
            return [TextContent(type="text", text=json.dumps({
                "success": True,
                "section": section,
                "key": key,
                "new_value": value,
                "backup_created": backup,
            }, indent=2))]

        elif name == "search_settings":
            results = ini.search_settings(arguments["query"])
            return [TextContent(type="text", text=json.dumps(results, indent=2))]

        elif name == "list_backups":
            file_key = arguments.get("file_key")
            backups = ini.list_backups(file_key)
            return [TextContent(type="text", text=json.dumps(backups, indent=2))]

        elif name == "restore_backup":
            dst = ini.restore_backup(arguments["backup_path"], arguments["file_key"])
            return [TextContent(type="text", text=json.dumps({
                "success": True,
                "restored_to": dst,
            }, indent=2))]

        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        return [TextContent(type="text", text=json.dumps({
            "error": str(e),
            "type": type(e).__name__,
        }, indent=2))]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
