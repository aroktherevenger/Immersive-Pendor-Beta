#!/usr/bin/env python2
# build.py
# Compiles the module system Python files into M&B text files.
# Run this from the project root: python tools/build.py
#
# Requirements:
#   - Python 2.7
#   - M&B module system files (process_*.py) present in module_system/ or PATH
#   - WARBAND_MODULE_PATH env var pointing to your PoP install folder (optional)

from __future__ import print_function
import os
import sys
import shutil
import subprocess

PROJECT_ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULE_DIR      = os.path.join(PROJECT_ROOT, "module_system")
OUTPUT_DIR      = os.path.join(PROJECT_ROOT, "output")

# Set this to your Warband PoP install path, or use the env var
WARBAND_MODULE_PATH = os.environ.get(
    "WARBAND_MODULE_PATH",
    r"C:\Program Files (x86)\Steam\steamapps\common\MountBlade Warband\Modules\Prophesy of Pendor V3.9.5"
)

PROCESS_SCRIPTS = [
    "process_troops.py",
    "process_items.py",
    "process_parties.py",
    "process_quests.py",
    "process_dialogs.py",
    "process_scenes.py",
    "process_factions.py",
    "process_skills.py",
]


def ensure_output_dir():
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print("[build] Created output/ directory")


def run_processor(script):
    script_path = os.path.join(MODULE_DIR, script)
    if not os.path.isfile(script_path):
        print("[build] WARNING: {} not found, skipping".format(script))
        return False
    print("[build] Running {}...".format(script))
    result = subprocess.call([sys.executable, script_path], cwd=MODULE_DIR)
    if result != 0:
        print("[build] ERROR: {} exited with code {}".format(script, result))
        return False
    return True


def copy_to_install():
    if not os.path.isdir(WARBAND_MODULE_PATH):
        print("[build] WARNING: WARBAND_MODULE_PATH not found: {}".format(
            WARBAND_MODULE_PATH))
        print("[build] Skipping copy step. Set WARBAND_MODULE_PATH env var to auto-copy.")
        return
    txt_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".txt")]
    for f in txt_files:
        src = os.path.join(OUTPUT_DIR, f)
        dst = os.path.join(WARBAND_MODULE_PATH, f)
        shutil.copy2(src, dst)
        print("[build] Copied {} -> {}".format(f, WARBAND_MODULE_PATH))


def main():
    print("[build] Pendor Mod Build Script")
    print("[build] Project root: {}".format(PROJECT_ROOT))
    ensure_output_dir()

    failed = []
    for script in PROCESS_SCRIPTS:
        if not run_processor(script):
            failed.append(script)

    if failed:
        print("\n[build] FAILED scripts: {}".format(", ".join(failed)))
        sys.exit(1)

    print("\n[build] All processors completed.")
    copy_to_install()
    print("[build] Done.")


if __name__ == "__main__":
    main()
