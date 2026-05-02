#!/usr/bin/env python2
# diff_pop.py
# Compares your compiled output/*.txt files against vanilla PoP text files.
# Helps you see exactly what your mod changes before testing.
#
# Usage:
#   python tools/diff_pop.py [file.txt]
#   python tools/diff_pop.py troops.txt          # diff just troops
#   python tools/diff_pop.py                      # diff all output files

from __future__ import print_function
import os
import sys
import difflib

PROJECT_ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR      = os.path.join(PROJECT_ROOT, "output")
VANILLA_POP_DIR = os.environ.get(
    "VANILLA_POP_PATH",
    r"C:\Program Files (x86)\Steam\steamapps\common\MountBlade Warband\Modules\Prophesy of Pendor V3.9.5"
)


def diff_file(filename):
    output_path  = os.path.join(OUTPUT_DIR, filename)
    vanilla_path = os.path.join(VANILLA_POP_DIR, filename)

    if not os.path.isfile(output_path):
        print("Output file not found: {}".format(output_path))
        return
    if not os.path.isfile(vanilla_path):
        print("Vanilla file not found: {}".format(vanilla_path))
        print("Set VANILLA_POP_PATH env var to your unmodified PoP folder.")
        return

    with open(vanilla_path, "r") as f:
        vanilla_lines = f.readlines()
    with open(output_path, "r") as f:
        output_lines = f.readlines()

    diff = list(difflib.unified_diff(
        vanilla_lines, output_lines,
        fromfile="vanilla/{}".format(filename),
        tofile="output/{}".format(filename),
        lineterm=""
    ))

    if not diff:
        print("[{}] No changes from vanilla.".format(filename))
        return

    print("[{}] {} lines changed:".format(filename, len(diff)))
    for line in diff:
        print(line)


def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        if not os.path.isdir(OUTPUT_DIR):
            print("No output/ directory found. Run tools/build.py first.")
            sys.exit(1)
        files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".txt")]

    if not files:
        print("No .txt files to compare.")
        sys.exit(0)

    for f in files:
        diff_file(f)
        print()


if __name__ == "__main__":
    main()
