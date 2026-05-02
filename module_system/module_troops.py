# module_troops.py
# Defines all troop entries for the mod.
# Format: ["troop_id", "Name", "Plural", flags, scene_obj, reserved,
#           face_key1, face_key2, [items], [attribs], [wp], [skills], faction]
#
# IMPORTANT: Only APPEND new troops at the bottom. Inserting in the middle
# shifts all IDs and will break existing save files.

from header_common import *
from module_constants import *

# ── Faces ─────────────────────────────────────────────────────────────────────
# Reuse PoP's face keys. These are hex-encoded face morph values.
face_young_1    = 0x000000001c38c469
face_young_2    = 0x0000000064118a15
face_middle_1   = 0x000000005c4f4912
face_old_1      = 0x00000000782d8a52
face_noldor     = 0x00000000601f0000  # Elvish features

# ── Vanilla PoP Troops (stubs — DO NOT redefine, for ID reference only) ──────
# These exist in the base PoP module. Listed here so we can reference IDs.
# trp_player            = 0  (always slot 0)
# trp_kingdom_1_recruit = first Pendor recruit
# ... (see docs/pop_structure.md for full list)

# ── New Troops Added by This Mod ──────────────────────────────────────────────
# Start appending after all vanilla PoP troops.

troops = [
    # ── Example: A new Pendor footman variant ────────────────────────────────
    ["mod_pendor_footman_veteran",
     "Veteran Pendor Footman", "Veteran Pendor Footmen",
     tf_male | tf_guarantee_armor | tf_guarantee_helmet | tf_guarantee_boots,
     0, 0,
     face_middle_1, face_old_1,
     # Equipment: sword, shield, spear, armor, helmet, boots
     [("scimitar_b", 0), ("kite_shield", 0), ("war_spear", 0),
      ("mail_hauberk", 0), ("nasal_helmet", 0), ("mail_chausses", 0)],
     # Attributes: str, agi, int, cha, level
     encode_attr(strength=12, agility=12, intelligence=8, charisma=8, level=20),
     # Weapon proficiencies: 1h, 2h, polearm, archery, crossbow, throwing
     encode_wp(one_handed=120, polearm=100),
     # Skills
     [encode_skill(skl_ironflesh, 3), encode_skill(skl_power_strike, 2),
      encode_skill(skl_shield, 2)],
     fac_kingdom_1],

    # ── Example: A new D'Shar mounted archer variant ──────────────────────────
    ["mod_dshar_wind_archer_elite",
     "D'Shar Wind Archer Elite", "D'Shar Wind Archer Elites",
     tf_male | tf_mounted | tf_guarantee_horse | tf_guarantee_armor |
     tf_guarantee_helmet | tf_guarantee_ranged,
     0, 0,
     face_young_1, face_young_2,
     [("arabian_armor_b", 0), ("nomad_bow", 0), ("barbed_arrows", 0),
      ("arabian_sword_c", 0), ("arabian_helmet_b", 0),
      ("nomad_boots", 0), ("arabian_horse_b", 0)],
     encode_attr(strength=10, agility=15, intelligence=8, charisma=8, level=22),
     encode_wp(one_handed=100, archery=160, horse_archery=140),
     [encode_skill(skl_horse_archery, 4), encode_skill(skl_power_draw, 3),
      encode_skill(skl_riding, 5)],
     fac_kingdom_4],
]
