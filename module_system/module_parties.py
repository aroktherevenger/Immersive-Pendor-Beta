# module_parties.py
# Party templates — defines the composition of spawned groups on the world map.
# Unique spawns (named lords, special armies) are defined here too.

from header_common import *
from module_constants import *

# Party flags
pf_default              = 0x00000000
pf_active               = 0x00000001
pf_is_lord              = 0x00000010
pf_is_mercenary         = 0x00000020
pf_quest_party          = 0x00000100
pf_starts_hidden        = 0x00000200
pf_has_ai               = 0x00000400
pf_patrol_party         = 0x00001000

# AI behaviors
ai_bhvr_hold            = 0
ai_bhvr_travel_to_party = 1
ai_bhvr_raid_around_center = 2
ai_bhvr_patrol_location = 8

# Party template entry: (troop_id, min_count, max_count)
# troop_id must match the string id defined in module_troops.py

party_templates = [
    # ── Mod-added patrol / roaming groups ─────────────────────────────────────
    ["mod_pendor_veteran_patrol",
     "Pendor Veteran Patrol",
     pf_has_ai,
     fac_kingdom_1,
     ai_bhvr_patrol_location,
     [("mod_pendor_footman_veteran", 8, 16)],
     ],

    ["mod_dshar_wind_archer_warband",
     "D'Shar Wind Archer Warband",
     pf_has_ai,
     fac_kingdom_4,
     ai_bhvr_raid_around_center,
     [("mod_dshar_wind_archer_elite", 12, 20)],
     ],

    ["mod_iron_circle_raider",
     "Iron Circle Raiders",
     pf_has_ai | pf_always_hostile,
     "mod_iron_circle_cult",
     ai_bhvr_raid_around_center,
     [("mod_pendor_footman_veteran", 6, 10),   # corrupted soldiers
      ("mod_dshar_wind_archer_elite", 4, 8)],
     ],
]

# ── Unique / Named Parties ────────────────────────────────────────────────────
# These are one-of-a-kind spawns with fixed gear.
parties = [
    ["mod_iron_circle_champion",
     "Valorian the Ironclad",          # display name
     "Valorian the Ironclad",
     pf_is_lord | pf_has_ai,
     "mod_iron_circle_cult",
     ai_bhvr_travel_to_party,
     # Troops in party
     [("mod_pendor_footman_veteran", 20, 30),
      ("mod_dshar_wind_archer_elite", 10, 15)],
     # Starting location: center id (match a scene/map id)
     "center_iron_bastion",
     ],
]
