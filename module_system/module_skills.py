# module_skills.py
# New skills or skill modifications for this mod.
# Most skill behavior is hardcoded in M&B engine; this file adjusts metadata.

from header_common import *
from module_constants import *

# Skill flags
sf_trainer_skill    = 0x00000004   # Can only be used by trainer NPCs
sf_weapon_master    = 0x00000008   # Tied to weapon proficiency gain

skills = [
    # Vanilla skills are not redefined here.
    # Only add genuinely NEW skills below.

    # Example: a new "Alchemy" skill (requires scripting hooks to function)
    # ["mod_skill_alchemy",
    #  "Alchemy",
    #  sf_default,
    #  10,        # max level
    #  "Allows crafting of potions and alchemical goods. "
    #  "Each level increases recipe count and reduces crafting time."],
]

# ── Skill modifier tables ──────────────────────────────────────────────────────
# Override how vanilla skills scale. Format: (skill_id, level, bonus_value)
# These are applied via script hooks, not compiled directly.
skill_modifiers = {
    # Make Surgery slightly more effective per point
    skl_surgery:        {1: 4, 2: 8, 3: 12, 4: 16, 5: 20,
                         6: 26, 7: 32, 8: 38, 9: 44, 10: 50},
    # Flatten Leadership bonus (more gradual scaling)
    skl_leadership:     {1: 5, 2: 10, 3: 16, 4: 22, 5: 29,
                         6: 36, 7: 44, 8: 52, 9: 61, 10: 70},
}
