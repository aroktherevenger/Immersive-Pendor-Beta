"""
Handles reading and writing for both INI file formats used by M&B Warband:
  - module.ini  : flat key=value with # comments (no section headers)
  - rgl_config.ini : standard INI with [Section] headers
"""

import os
import re
import shutil
import configparser
from datetime import datetime


# ── Known file paths ──────────────────────────────────────────────────────────
INI_FILES = {
    "module": r"C:\Program Files (x86)\Steam\steamapps\common\MountBlade Warband\Modules\Prophesy of Pendor V3.9.5\module.ini",
    "rgl_config": r"C:\Users\arosh\Documents\Mount&Blade Warband WSE2\rgl_config.ini",
}

BACKUP_DIR = r"C:\Users\arosh\Pendor Modding\tools\mcp_server\backups"


# ── Backup ────────────────────────────────────────────────────────────────────

def backup_file(file_key: str) -> str:
    """Create a timestamped backup of an INI file. Returns the backup path."""
    src = INI_FILES[file_key]
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = os.path.join(BACKUP_DIR, f"{file_key}_{ts}.ini")
    shutil.copy2(src, dst)
    return dst


def list_backups(file_key: str = None) -> list:
    """Return list of backup files, optionally filtered by file_key."""
    if not os.path.isdir(BACKUP_DIR):
        return []
    files = sorted(os.listdir(BACKUP_DIR), reverse=True)
    if file_key:
        files = [f for f in files if f.startswith(file_key + "_")]
    return [os.path.join(BACKUP_DIR, f) for f in files]


def restore_backup(backup_path: str, file_key: str) -> str:
    """Restore a backup file to its original location."""
    dst = INI_FILES[file_key]
    backup_file(file_key)  # backup current before restoring
    shutil.copy2(backup_path, dst)
    return dst


# ── module.ini parser (flat key=value, no sections) ───────────────────────────

def _parse_module_ini(path: str) -> list:
    """
    Parse module.ini into a list of dicts:
    [{"key": str, "value": str, "comment": str, "line_num": int, "raw": str}]
    Comment-only and blank lines are included with key=None.
    """
    entries = []
    with open(path, "r") as f:
        for i, raw in enumerate(f, 1):
            line = raw.rstrip("\n")
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                entries.append({"key": None, "value": None,
                                 "comment": stripped, "line_num": i, "raw": raw})
                continue
            # split on first # to separate inline comment
            if "#" in line:
                code_part, comment_part = line.split("#", 1)
                comment_part = "#" + comment_part
            else:
                code_part, comment_part = line, ""
            if "=" in code_part:
                k, v = code_part.split("=", 1)
                entries.append({
                    "key": k.strip(),
                    "value": v.strip(),
                    "comment": comment_part.strip(),
                    "line_num": i,
                    "raw": raw,
                })
            else:
                entries.append({"key": None, "value": None,
                                 "comment": stripped, "line_num": i, "raw": raw})
    return entries


def read_module_ini() -> dict:
    """Return {key: {value, comment, line_num}} for all settings in module.ini."""
    path = INI_FILES["module"]
    result = {}
    for entry in _parse_module_ini(path):
        if entry["key"] is not None:
            result[entry["key"]] = {
                "value": entry["value"],
                "comment": entry["comment"],
                "line_num": entry["line_num"],
            }
    return result


def update_module_ini(key: str, new_value: str) -> str:
    """Update a key in module.ini. Returns the backup path."""
    path = INI_FILES["module"]
    backup_path = backup_file("module")

    entries = _parse_module_ini(path)
    found = False
    new_lines = []
    for entry in entries:
        if entry["key"] == key:
            comment = f"  {entry['comment']}" if entry["comment"] else ""
            new_lines.append(f"{key} = {new_value}{comment}\n")
            found = True
        else:
            new_lines.append(entry["raw"] if entry["raw"].endswith("\n")
                             else entry["raw"] + "\n")

    if not found:
        raise KeyError(f"Key '{key}' not found in module.ini")

    with open(path, "w") as f:
        f.writelines(new_lines)

    return backup_path


# ── rgl_config.ini parser (standard INI with [Sections]) ─────────────────────

def read_rgl_config(section: str = None) -> dict:
    """
    Return settings from rgl_config.ini.
    If section given: {key: value} for that section only.
    Otherwise: {section: {key: value}} for all sections.
    """
    path = INI_FILES["rgl_config"]
    cfg = configparser.RawConfigParser()
    cfg.optionxform = str  # preserve key case
    cfg.read(path)

    if section:
        if not cfg.has_section(section):
            raise KeyError(f"Section [{section}] not found in rgl_config.ini")
        return dict(cfg.items(section))

    return {sec: dict(cfg.items(sec)) for sec in cfg.sections()}


def update_rgl_config(section: str, key: str, new_value: str) -> str:
    """Update a key in rgl_config.ini. Returns the backup path."""
    path = INI_FILES["rgl_config"]
    backup_path = backup_file("rgl_config")

    cfg = configparser.RawConfigParser()
    cfg.optionxform = str
    cfg.read(path)

    if not cfg.has_section(section):
        raise KeyError(f"Section [{section}] not found in rgl_config.ini")
    if not cfg.has_option(section, key):
        raise KeyError(f"Key '{key}' not found in [{section}]")

    cfg.set(section, key, new_value)

    with open(path, "w") as f:
        cfg.write(f)

    return backup_path


# ── Search ────────────────────────────────────────────────────────────────────

def search_settings(query: str) -> dict:
    """
    Search for a keyword across all INI files.
    Returns {"module": [...], "rgl_config": [...]} with matching entries.
    """
    q = query.lower()
    results = {"module": [], "rgl_config": []}

    # Search module.ini
    for key, info in read_module_ini().items():
        if q in key.lower() or q in info["comment"].lower():
            results["module"].append({
                "key": key,
                "value": info["value"],
                "comment": info["comment"],
            })

    # Search rgl_config.ini
    for section, settings in read_rgl_config().items():
        for key, value in settings.items():
            if q in key.lower() or q in section.lower():
                results["rgl_config"].append({
                    "section": section,
                    "key": key,
                    "value": value,
                })

    return results
