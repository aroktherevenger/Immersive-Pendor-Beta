# module_items.py
# Defines new items added by this mod.
# IMPORTANT: Only APPEND new items. Inserting in the middle shifts IDs.

from header_common import *
from module_constants import *

# Item capability flags (weapon stats encoded as flags)
itcf_thrust_one_handed  = 0x00000001
itcf_overswing_one_handed = 0x00000002
itcf_slashright_one_handed = 0x00000004
itcf_slashleft_one_handed = 0x00000008
itcf_thrust_two_handed  = 0x00000100
itcf_overswing_two_handed = 0x00000200
itcf_thrust_polearm     = 0x00010000
itcf_overswing_polearm  = 0x00020000
itcf_horseback          = 0x10000000

# Damage types (ORed into weapon damage value)
# cut = 0, pierce = 1, blunt = 2 (encoded as damage | (type << 8))
def cut(dmg):   return dmg
def pierce(dmg): return dmg | (1 << 8)
def blunt(dmg): return dmg | (2 << 8)

items = [
    # Format:
    # ["item_id", "Item Name",
    #  [("mesh_name", modifier_flags)],
    #  item_kind, item_modifiers, item_flags, capabilities,
    #  value, weight, speed_rating, max_ammo,
    #  thrust_damage, swing_damage,
    #  weapon_length, shield_width, shield_height,
    #  head_armor, body_armor, leg_armor, difficulty]

    # ── Weapons ───────────────────────────────────────────────────────────────
    ["mod_pendor_longsword",
     "Pendor Knight's Longsword",
     [("sword_two_handed_a", 0)],
     itp_type_one_handed | itp_merchandise,
     0,  # no special modifiers
     itp_primary | itp_secondary,
     itcf_thrust_one_handed | itcf_slashright_one_handed | itcf_slashleft_one_handed,
     1800,   # value in denars
     1.5,    # weight in kg
     98,     # speed rating
     0,      # max ammo (0 for melee)
     pierce(28),   # thrust damage
     cut(38),      # swing damage
     96,     # weapon length
     0, 0,   # shield dimensions (unused for swords)
     0, 0, 0,  # armor values (unused for weapons)
     10],    # difficulty (strength requirement)

    ["mod_noldor_star_arrow",
     "Noldor Star-forged Arrow",
     [("arrow", 0)],
     itp_type_arrows | itp_merchandise,
     0,
     0,
     0,
     800,
     2.0,
     0,
     32,     # stack size
     pierce(14),
     0,
     95,     # missile speed
     0, 0, 0, 0, 0, 0],

    # ── Armor ─────────────────────────────────────────────────────────────────
    ["mod_pendor_plate_armor",
     "Pendor Royal Plate",
     [("full_plate_armor", 0)],
     itp_type_body_armor | itp_merchandise,
     0,
     itp_covers_legs,
     0,
     12000,
     25.0,
     0, 0, 0, 0,
     0, 0,
     0,      # head armor
     68,     # body armor
     42,     # leg armor (covered by this piece)
     15],    # difficulty
]
