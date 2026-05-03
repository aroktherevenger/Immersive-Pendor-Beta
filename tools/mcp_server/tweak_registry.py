"""
Tweak Registry — tracks every change applied to PoP game files.

Every applied tweak is stored in registry.json with:
- What file was changed
- What the original value was
- What the new value is
- What area of the code was touched (so conflicts can be detected)
- When it was applied

Before applying a new tweak, check_conflicts() compares the target file
and search pattern against existing entries. If the same region was already
touched by a previous tweak, it warns so we don't blindly overwrite or
apply incompatible changes on top of each other.
"""

import json
import os
from datetime import datetime

REGISTRY_PATH = os.path.join(
    os.path.dirname(__file__), "registry.json"
)


def _load() -> dict:
    if not os.path.isfile(REGISTRY_PATH):
        return {"tweaks": []}
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(data: dict):
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def register_tweak(
    tweak_id: str,
    tweak_name: str,
    file_path: str,
    search_pattern: str,
    original_text: str,
    new_text: str,
    notes: str = "",
    wiki_ref: str = "",
) -> dict:
    """
    Record a successfully applied tweak.
    Returns the registry entry that was saved.
    """
    data = _load()
    entry = {
        "id": tweak_id,
        "name": tweak_name,
        "file": file_path,
        "search_pattern": search_pattern,
        "original": original_text,
        "replacement": new_text,
        "notes": notes,
        "wiki_ref": wiki_ref,
        "applied_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    # Update existing entry if same id, otherwise append
    existing = [t for t in data["tweaks"] if t["id"] == tweak_id]
    if existing:
        data["tweaks"] = [e if e["id"] != tweak_id else entry
                          for e in data["tweaks"]]
    else:
        data["tweaks"].append(entry)
    _save(data)
    return entry


def check_conflicts(file_path: str, search_pattern: str) -> list:
    """
    Check if any previously applied tweak touched the same file
    and overlapping pattern. Returns list of conflicting entries.

    A conflict is when:
    - Same file AND
    - The new search_pattern appears inside a previous tweak's
      original/replacement text, OR vice versa (overlapping region)
    """
    data = _load()
    conflicts = []
    norm_file = os.path.normpath(file_path).lower()
    for entry in data["tweaks"]:
        if os.path.normpath(entry["file"]).lower() != norm_file:
            continue
        # Check if patterns overlap
        prev_pattern = entry["search_pattern"].lower()
        new_pattern = search_pattern.lower()
        if (new_pattern in prev_pattern or
                prev_pattern in new_pattern or
                new_pattern in entry["original"].lower() or
                new_pattern in entry["replacement"].lower()):
            conflicts.append(entry)
    return conflicts


def list_tweaks(file_filter: str = None) -> list:
    """Return all registered tweaks, optionally filtered by file name."""
    data = _load()
    tweaks = data["tweaks"]
    if file_filter:
        tweaks = [t for t in tweaks
                  if file_filter.lower() in t["file"].lower()]
    return tweaks


def get_tweak(tweak_id: str) -> dict | None:
    """Return a specific tweak entry by ID."""
    data = _load()
    for entry in data["tweaks"]:
        if entry["id"] == tweak_id:
            return entry
    return None


def remove_tweak(tweak_id: str) -> bool:
    """Remove a tweak from the registry (use after reverting it)."""
    data = _load()
    before = len(data["tweaks"])
    data["tweaks"] = [t for t in data["tweaks"] if t["id"] != tweak_id]
    _save(data)
    return len(data["tweaks"]) < before


def summarize_by_file() -> dict:
    """Return {filename: [tweak_id, ...]} grouped by file."""
    data = _load()
    result = {}
    for entry in data["tweaks"]:
        fname = os.path.basename(entry["file"])
        result.setdefault(fname, []).append({
            "id": entry["id"],
            "name": entry["name"],
            "applied_at": entry["applied_at"],
        })
    return result
