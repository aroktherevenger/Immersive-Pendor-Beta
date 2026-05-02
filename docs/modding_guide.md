# Pendor Modding — Getting Started Guide

## Prerequisites
1. Mount & Blade: Warband (v1.174 or later)
2. Prophesy of Pendor v3.9.x installed
3. Python 2.7 (NOT Python 3) — [python.org/downloads](https://www.python.org/downloads/)
4. The M&B module system files (download from TaleWorlds forums or bundled with PoP)

## Initial Setup

### 1. Set environment variables
Add these to your system or a local `.env` batch file:
```batch
set WARBAND_MODULE_PATH=C:\Program Files (x86)\Steam\steamapps\common\MountBlade Warband\Modules\Prophesy of Pendor V3.9.5
set VANILLA_POP_PATH=C:\Program Files (x86)\Steam\steamapps\common\MountBlade Warband\Modules\Prophesy of Pendor V3.9.5_vanilla_backup
set PATH=%PATH%;C:\Python27
```

### 2. Back up your PoP installation
Before modding, copy your entire PoP folder to `POP_vanilla_backup`.
This is what `tools/diff_pop.py` compares against.

### 3. Copy M&B module system process scripts
Copy the `process_*.py` files from the M&B module system into `module_system/`.
These are NOT included in this repo (they belong to TaleWorlds).

## Typical Workflow

### Adding a new troop
1. Open `module_system/module_troops.py`
2. Append a new entry to the `troops` list (never insert in the middle)
3. Reference `header_common.py` for flags and `encode_attr()` / `encode_wp()`
4. Run `python tools/build.py`
5. Launch Warband on a **new save** and test

### Adding a new item
1. Open `module_system/module_items.py`
2. Append to the `items` list
3. Make sure the mesh name exists in the game's `.brf` files
4. Run `python tools/build.py` and test

### Adding a quest
1. Add the quest entry to `module_quests.py`
2. Add the dialog trigger to `module_dialogs.py`
3. Add any needed script hooks in `module_scripts.py` (create if needed)
4. Build and test on a new save

## Testing Tips
- Use the **cheat menu** (enable in Warband settings) to spawn troops, set renown
- `Ctrl+X` in-game gives you gold for testing economy balance
- Check `rgl_log.txt` in the Warband install folder for crash logs
- When dialogs don't fire, check the condition order — conditions short-circuit

## Common Errors

| Error | Cause | Fix |
|---|---|---|
| "Unknown troop id" | ID reference mismatch | Check troop list order hasn't shifted |
| Game crashes on load | Syntax error in compiled txt | Run diff_pop.py to find the bad line |
| Dialog never appears | Wrong speaker token or failed condition | Step through dialog conditions manually |
| New item invisible | Mesh name typo | Check `.brf` file with OpenBRF |
| Save corrupted | Modified middle of a list | Always append; test on new saves |

## Resources
- TaleWorlds Forum — Mount & Blade modding subforum
- PoP Official Thread on TWC (TaleWorlds Community)
- M&B Module System Documentation (bundled with module system download)
- OpenBRF — tool for editing `.brf` mesh/texture resource files
