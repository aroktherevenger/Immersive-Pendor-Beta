# Pendor Modding Project

## Project Overview
This project is a mod-of-a-mod targeting **Prophesy of Pendor (PoP) v3.9.x** for **Mount & Blade: Warband**.
The goal is to extend, rebalance, or add new content on top of the existing PoP module.

## Directory Structure
```
Pendor Modding/
├── CLAUDE.md               # This file — project context for Claude
├── .gitignore
├── module_system/          # Python source files compiled into the mod
│   ├── module_troops.py    # Troop definitions (knights, recruits, etc.)
│   ├── module_items.py     # Weapons, armor, equipment
│   ├── module_parties.py   # Party templates and spawns
│   ├── module_factions.py  # Faction definitions
│   ├── module_quests.py    # Quest definitions
│   ├── module_dialogs.py   # NPC dialogues
│   ├── module_skills.py    # Skill trees and modifiers
│   ├── module_scenes.py    # Scene/map definitions
│   ├── module_constants.py # Shared constants and enums
│   └── header_common.py    # Common PoP/M&B header imports
├── patches/                # Targeted diffs / change logs per feature
├── docs/                   # Design notes, references, modding guides
│   ├── pop_structure.md    # How PoP is organized internally
│   ├── knight_orders.md    # Reference for all knight orders in PoP
│   └── modding_guide.md    # Step-by-step guide for this project
├── tools/                  # Helper scripts
│   ├── build.py            # Compile module system → text files
│   └── diff_pop.py         # Compare against vanilla PoP files
└── output/                 # Compiled text files (git-ignored)
```

## Tech Stack
- **Language:** Python 2.7 (required by M&B Warband module system)
- **Game:** Mount & Blade: Warband (v1.174+)
- **Base mod:** Prophesy of Pendor v3.9.5
- **PoP install path:** `C:\Program Files (x86)\Steam\steamapps\common\MountBlade Warband\Modules\Prophesy of Pendor V3.9.5`
- **Compiler:** `process_utilities.py` / `process_troops.py` etc. from M&B module system

## Key PoP Concepts
- **Knight Orders:** D'Shar Windriders, Jatu Black Hand, Clarion Call, etc. — defined in `module_troops.py`
- **Snake Cult:** Major antagonist faction — complex spawn logic in `module_parties.py`
- **Noldor:** High-tier AI faction — mostly in `module_troops.py` and `module_parties.py`
- **Pendor Nobles:** Player's main progression path — quests in `module_quests.py`
- **Unique Spawns:** Named lords with special gear — spread across troops/parties/items

## Modding Workflow
1. Edit the relevant `module_*.py` file in `module_system/`
2. Run `tools/build.py` to compile to text files
3. Copy output text files into your PoP installation folder
4. Launch Warband and test in-game
5. Document changes in `patches/` with a short description

## Important Constraints
- Always use Python 2.7 syntax (no f-strings, no walrus operator, print is a statement)
- Item/troop IDs must stay consistent — inserting new entries in the middle breaks saves
- Append new troops/items to the END of lists to avoid ID shifts
- Test with a new save when changing troops/items; existing saves may corrupt

## Common M&B Module System Patterns
```python
# Troop definition format:
# ["troop_id", "Name", "Plural Name", troop_flags, scene_obj, reserved,
#  face_key_1, face_key_2, [equipment], [attributes], [wp], [skills], [faction]]

# Item definition format:
# ["item_id", "Item Name", [("mesh_name", modifier_flags)],
#  item_kind, modifiers, flags, capabilities, value, weight, ...]
```
