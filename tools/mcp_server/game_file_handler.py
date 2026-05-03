"""
Handles reading, searching, and patching PoP compiled game text files.

These are the large files in the PoP install folder (scripts.txt,
conversation.txt, troops.txt, etc.) that wiki tweaks modify.

All writes auto-backup before touching anything.
Conflict checking is done via tweak_registry before any patch.
"""

import os
import re
import shutil
from datetime import datetime

import tweak_registry as registry

POP_DIR = (r"C:\Program Files (x86)\Steam\steamapps\common"
           r"\MountBlade Warband\Modules\Prophesy of Pendor V3.9.5")

BACKUP_DIR = os.path.join(os.path.dirname(__file__), "backups", "game_files")

# Known moddable text files
GAME_FILES = {
    "scripts":          os.path.join(POP_DIR, "scripts.txt"),
    "conversation":     os.path.join(POP_DIR, "conversation.txt"),
    "simple_triggers":  os.path.join(POP_DIR, "simple_triggers.txt"),
    "troops":           os.path.join(POP_DIR, "troops.txt"),
    "items":            os.path.join(POP_DIR, "items.txt"),
    "parties":          os.path.join(POP_DIR, "parties.txt"),
    "party_templates":  os.path.join(POP_DIR, "party_templates.txt"),
    "menus":            os.path.join(POP_DIR, "menus.txt"),
    "quick_strings":    os.path.join(POP_DIR, "quick_strings.txt"),
    "variables":        os.path.join(POP_DIR, "variables.txt"),
    "dialog_states":    os.path.join(POP_DIR, "dialog_states.txt"),
    "triggers":         os.path.join(POP_DIR, "triggers.txt"),
    "factions":         os.path.join(POP_DIR, "factions.txt"),
    "skills":           os.path.join(POP_DIR, "skills.txt"),
    "quests":           os.path.join(POP_DIR, "quests.txt"),
    "scene_props":      os.path.join(POP_DIR, "scene_props.txt"),
}


def resolve_file(file_key: str) -> str:
    """Return full path for a file key or treat as direct path."""
    if file_key in GAME_FILES:
        return GAME_FILES[file_key]
    # Allow passing a bare filename like "scripts.txt"
    bare = file_key.replace(".txt", "")
    if bare in GAME_FILES:
        return GAME_FILES[bare]
    raise KeyError(
        f"Unknown file '{file_key}'. Known files: {list(GAME_FILES.keys())}"
    )


def backup_game_file(file_key: str) -> str:
    """Backup a game file before modifying it. Returns backup path."""
    path = resolve_file(file_key)
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = os.path.basename(path)
    dst = os.path.join(BACKUP_DIR, f"{fname}.{ts}.bak")
    shutil.copy2(path, dst)
    return dst


def search_in_file(file_key: str, pattern: str,
                   context_lines: int = 3) -> list:
    """
    Search for a pattern (plain text or regex) in a game file.
    Returns list of matches: {line_num, line, context_before, context_after}
    """
    path = resolve_file(file_key)
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    results = []
    for i, line in enumerate(lines):
        if re.search(pattern, line, re.IGNORECASE):
            before = lines[max(0, i - context_lines):i]
            after = lines[i + 1:i + 1 + context_lines]
            results.append({
                "line_num": i + 1,
                "line": line.rstrip("\n"),
                "context_before": [l.rstrip("\n") for l in before],
                "context_after": [l.rstrip("\n") for l in after],
            })
    return results


def read_lines(file_key: str, start_line: int,
               end_line: int) -> list:
    """Read a specific line range from a game file (1-indexed)."""
    path = resolve_file(file_key)
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    return [
        {"line_num": i + 1, "content": lines[i].rstrip("\n")}
        for i in range(start_line - 1, min(end_line, len(lines)))
    ]


def apply_tweak(
    tweak_id: str,
    tweak_name: str,
    file_key: str,
    search_text: str,
    replacement_text: str,
    notes: str = "",
    wiki_ref: str = "",
    occurrence: int = 1,
) -> dict:
    """
    Find search_text in file_key and replace it with replacement_text.

    - Checks registry for conflicts first and WARNS (does not block)
    - Backs up the file before touching it
    - Registers the change in the tweak registry
    - occurrence: which match to replace (1 = first, 0 = all)

    Returns result dict with success, backup path, and any conflicts found.
    """
    path = resolve_file(file_key)

    # 1. Conflict check
    conflicts = registry.check_conflicts(path, search_text)
    conflict_warning = None
    if conflicts:
        conflict_warning = (
            f"WARNING: {len(conflicts)} previously applied tweak(s) "
            f"touched overlapping code in {os.path.basename(path)}:\n" +
            "\n".join(f"  - [{c['id']}] {c['name']} (applied {c['applied_at']})"
                      for c in conflicts) +
            "\nProceeding anyway — verify these tweaks are compatible."
        )

    # 2. Read file
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    if search_text not in content:
        return {
            "success": False,
            "error": f"Search text not found in {os.path.basename(path)}.",
            "hint": "Check spelling, whitespace, or line endings.",
        }

    # 3. Backup
    backup_path = backup_game_file(file_key)

    # 4. Apply replacement
    if occurrence == 0:
        new_content = content.replace(search_text, replacement_text)
        count = content.count(search_text)
    else:
        parts = content.split(search_text)
        if len(parts) < occurrence + 1:
            return {
                "success": False,
                "error": (f"Only {len(parts)-1} occurrence(s) found, "
                          f"cannot replace occurrence #{occurrence}."),
            }
        new_content = search_text.join(parts[:occurrence]) + \
                      replacement_text + \
                      search_text.join(parts[occurrence:])
        count = 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    # 5. Register
    entry = registry.register_tweak(
        tweak_id=tweak_id,
        tweak_name=tweak_name,
        file_path=path,
        search_pattern=search_text,
        original_text=search_text,
        new_text=replacement_text,
        notes=notes,
        wiki_ref=wiki_ref,
    )

    return {
        "success": True,
        "file": os.path.basename(path),
        "occurrences_replaced": count,
        "backup_created": backup_path,
        "registry_entry": entry["id"],
        "conflict_warning": conflict_warning,
    }


def revert_tweak(tweak_id: str) -> dict:
    """
    Revert a previously applied tweak by restoring its original text.
    Removes the entry from the registry on success.
    """
    entry = registry.get_tweak(tweak_id)
    if not entry:
        return {"success": False, "error": f"Tweak '{tweak_id}' not found in registry."}

    path = entry["file"]
    if not os.path.isfile(path):
        return {"success": False, "error": f"File not found: {path}"}

    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    if entry["replacement"] not in content:
        return {
            "success": False,
            "error": "Replacement text not found in file — may have been overwritten by another tweak.",
            "entry": entry,
        }

    # Backup before reverting
    file_key = os.path.splitext(os.path.basename(path))[0]
    backup_path = backup_game_file(file_key)

    new_content = content.replace(entry["replacement"], entry["original"], 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    registry.remove_tweak(tweak_id)

    return {
        "success": True,
        "reverted": tweak_id,
        "backup_created": backup_path,
    }
