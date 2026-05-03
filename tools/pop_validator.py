"""
PoP Validator - structural integrity check for Prophesy of Pendor text files.

Catches counter/body mismatches, truncated lines, and other format errors that
cause silent memory corruption in M&B Warband when the engine loads the file.

Usage:
    python pop_validator.py                     # validate all PoP files
    python pop_validator.py <file>              # validate a single file
    python pop_validator.py --hook              # hook mode (reads JSON from stdin)
"""

import sys
import os
import json
from pathlib import Path

POP_DIR = Path(
    r"C:\Program Files (x86)\Steam\steamapps\common\MountBlade Warband"
    r"\Modules\Prophesy of Pendor V3.9.5"
)


class Issue:
    def __init__(self, file, line, msg):
        self.file = file
        self.line = line
        self.msg = msg

    def __str__(self):
        return f"{self.file}:{self.line}: {self.msg}"


# ---------- conversation.txt ----------
def validate_conversation(path):
    issues = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith("dialogsfile"):
        return [Issue(path.name, 1, "missing 'dialogsfile' header")]
    try:
        counter = int(lines[1].strip())
    except Exception:
        return [Issue(path.name, 2, f"invalid counter: {lines[1].strip()!r}")]

    dlga_count = 0
    for i in range(2, len(lines)):
        line = lines[i].rstrip()
        if not line:
            issues.append(Issue(path.name, i + 1, "stray blank line"))
            continue
        if not line.startswith("dlga_"):
            issues.append(Issue(path.name, i + 1, f"not a dlga_ line: {line[:60]}"))
            continue
        dlga_count += 1
        toks = line.split()
        try:
            int(toks[1])  # flags
            int(toks[2])  # input_state
            cond_count = int(toks[3])
            pos = 4
            for _ in range(cond_count):
                int(toks[pos])  # opcode
                arg_count = int(toks[pos + 1])
                pos += 2 + arg_count
            pos += 1  # text token
            int(toks[pos])  # output_state
            pos += 1
            action_count = int(toks[pos])
            pos += 1
            for _ in range(action_count):
                int(toks[pos])
                arg_count = int(toks[pos + 1])
                pos += 2 + arg_count
            if pos >= len(toks):
                issues.append(Issue(path.name, i + 1, "missing voice_over after actions"))
        except Exception as e:
            issues.append(Issue(path.name, i + 1, f"op-count parse error: {e}: {line[:80]}"))

    if dlga_count != counter:
        issues.append(Issue(path.name, 2, f"counter says {counter} but found {dlga_count} dialogues"))
    return issues


# ---------- troops.txt ----------
def validate_troops(path):
    issues = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith("troopsfile"):
        return [Issue(path.name, 1, "missing 'troopsfile' header")]

    for i, line in enumerate(lines):
        if line.startswith("trp_"):
            name = line.split()[0]
            if i + 1 >= len(lines):
                issues.append(Issue(path.name, i + 1, f"{name}: missing equipment line"))
                continue
            eq_tokens = lines[i + 1].split()
            if len(eq_tokens) != 128:
                issues.append(
                    Issue(
                        path.name,
                        i + 2,
                        f"{name}: equipment has {len(eq_tokens)} tokens, expected 128 (64 slots x 2)",
                    )
                )
    return issues


# ---------- simple_triggers.txt ----------
def validate_simple_triggers(path):
    issues = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith("simple_triggers_file"):
        return [Issue(path.name, 1, "missing 'simple_triggers_file' header")]
    try:
        counter = int(lines[1].strip())
    except Exception:
        return [Issue(path.name, 2, f"invalid counter: {lines[1].strip()!r}")]

    actual = 0
    for i in range(2, len(lines)):
        if lines[i].strip():
            actual += 1
    if actual != counter:
        issues.append(Issue(path.name, 2, f"counter says {counter} but found {actual} triggers"))
    return issues


# ---------- mission_templates.txt ----------
def validate_mission_templates(path):
    issues = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    sections = []
    for i, line in enumerate(lines):
        if line.startswith("mst_"):
            sections.append((i, line.split()[0]))

    for idx, (start, name) in enumerate(sections):
        end = sections[idx + 1][0] if idx + 1 < len(sections) else len(lines)
        counter = None
        counter_idx = None
        for j in range(start + 1, end):
            s = lines[j].strip()
            if s.isdigit():
                counter = int(s)
                counter_idx = j
                break
        if counter_idx is None:
            continue
        trig_count = sum(
            1
            for j in range(counter_idx + 1, end)
            if lines[j].strip() and not lines[j].startswith("mst_")
        )
        if trig_count != counter:
            issues.append(
                Issue(
                    path.name,
                    counter_idx + 1,
                    f"{name}: counter says {counter}, actual triggers {trig_count}",
                )
            )
    return issues


# ---------- dialog_states.txt ----------
def validate_dialog_states(path):
    issues = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Format is one state name per line. Blank lines in the middle would shift
    # state IDs and corrupt every conversation reference downstream.
    last_nonblank = -1
    for i, line in enumerate(lines):
        if line.strip():
            last_nonblank = i
    for i in range(last_nonblank):
        if not lines[i].strip():
            issues.append(Issue(path.name, i + 1, "blank line in middle of dialog_states (must only trail)"))
    return issues


# ---------- sounds.txt ----------
def validate_sounds(path):
    issues = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith("soundsfile"):
        return [Issue(path.name, 1, "missing 'soundsfile' header")]
    try:
        file_count = int(lines[1].strip())
    except Exception:
        return [Issue(path.name, 2, f"invalid file count: {lines[1].strip()!r}")]

    names_idx = 2 + file_count
    if names_idx >= len(lines):
        return [Issue(path.name, names_idx + 1, "file truncated before names section")]
    try:
        names_count = int(lines[names_idx].strip())
    except Exception:
        return [
            Issue(
                path.name,
                names_idx + 1,
                f"expected names count at line {names_idx + 1}, got {lines[names_idx][:40]!r}",
            )
        ]
    expected = 2 + file_count + 1 + names_count
    actual = sum(1 for l in lines if l.strip())
    if actual != expected:
        issues.append(Issue(path.name, 2, f"expected {expected} non-blank lines, got {actual}"))
    return issues


# ---------- factions.txt ----------
def validate_factions(path):
    issues = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith("factionsfile"):
        return [Issue(path.name, 1, "missing 'factionsfile' header")]
    try:
        fac_count = int(lines[1].strip())
    except Exception:
        return [Issue(path.name, 2, f"invalid faction count: {lines[1].strip()!r}")]

    for f_idx in range(fac_count):
        row_idx = 2 + f_idx * 2 + 1
        if row_idx >= len(lines):
            break
        row = lines[row_idx].split()
        if len(row) != fac_count:
            issues.append(
                Issue(
                    path.name,
                    row_idx + 1,
                    f"faction #{f_idx} relation row has {len(row)} values, expected {fac_count}",
                )
            )
    return issues


VALIDATORS = {
    "conversation.txt": validate_conversation,
    "troops.txt": validate_troops,
    "simple_triggers.txt": validate_simple_triggers,
    "mission_templates.txt": validate_mission_templates,
    "dialog_states.txt": validate_dialog_states,
    "sounds.txt": validate_sounds,
    "factions.txt": validate_factions,
}


def validate_file(path):
    fn = VALIDATORS.get(path.name.lower())
    if not fn:
        return []
    try:
        return fn(path)
    except Exception as e:
        return [Issue(path.name, 0, f"validator crashed: {e}")]


def validate_all():
    all_issues = []
    for fname in VALIDATORS:
        p = POP_DIR / fname
        if p.exists():
            all_issues.extend(validate_file(p))
    return all_issues


def hook_mode():
    """Read JSON from stdin (Claude Code hook input). Validate the edited file
    if it lives inside the PoP install. Exit 2 to surface issues to Claude."""
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0

    tool_input = data.get("tool_input", {}) or {}
    file_path = tool_input.get("file_path", "")
    if not file_path:
        return 0

    p = Path(file_path)
    if "Prophesy of Pendor" not in str(p):
        return 0

    issues = validate_file(p)
    if issues:
        print(f"POP VALIDATOR: {len(issues)} issue(s) in {p.name}:", file=sys.stderr)
        for iss in issues[:15]:
            print(f"  {iss}", file=sys.stderr)
        if len(issues) > 15:
            print(f"  ... and {len(issues) - 15} more", file=sys.stderr)
        return 2
    return 0


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--hook":
        sys.exit(hook_mode())

    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        issues = validate_file(path)
        scope = path.name
    else:
        issues = validate_all()
        scope = "all PoP files"

    if issues:
        print(f"FAIL: {len(issues)} issue(s) in {scope}:")
        for iss in issues:
            print(f"  {iss}")
        sys.exit(1)
    else:
        print(f"OK: {scope} validate cleanly")
        sys.exit(0)


if __name__ == "__main__":
    main()
