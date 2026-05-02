# module_factions.py
# Faction definitions and relation tables.

from header_common import *
from module_constants import *

# Faction flags
ff_always_hostile       = 0x00000001
ff_can_have_queen       = 0x00000008
ff_show_relation_bar    = 0x00000010
ff_is_kingdom           = 0x00000020

factions = [
    # Vanilla factions are defined in base PoP — only list new ones here.

    # Example: A new hidden cult faction for this mod
    ["mod_iron_circle_cult",
     "Iron Circle Cult",
     ff_always_hostile,
     # Relation table: list of (faction_id, relation) pairs
     [(fac_kingdom_1, -80), (fac_kingdom_2, -80), (fac_kingdom_3, -80),
      (fac_kingdom_4, -80), (fac_kingdom_5, -80),
      (fac_snake_cult, 20),   # loosely allied with Snake Cult
      (fac_noldor, -60)],
     "Iron Circle",           # short name
     0x1a1a1a,                # color (dark grey hex)
     ],
]
