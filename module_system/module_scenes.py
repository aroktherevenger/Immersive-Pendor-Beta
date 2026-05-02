# module_scenes.py
# Scene / map location definitions for new areas added by this mod.

from header_common import *
from module_constants import *

# Scene flags
sf_default              = 0x00000000
sf_generate             = 0x00000001  # procedurally generated terrain
sf_indoors              = 0x00000010
sf_has_lower_level      = 0x00000100
sf_battle_scene         = 0x00000200

scenes = [
    # Format: ["scene_id", "Scene Name", scene_flags, "mesh_name",
    #           passage_list, chest_list, patrol_list,
    #           (xmin, xmax, ymin, ymax),  # map boundaries
    #           respawn_point]

    ["mod_iron_bastion",
     "Iron Bastion",
     sf_battle_scene | sf_has_lower_level,
     "scn_castle_c",          # reuse castle mesh from vanilla
     [("exit", 0, 0)],        # passages: (name, x, y)
     [],                       # chests
     [],                       # patrol points
     (0, 600, 0, 600),
     (300, 300)],              # spawn point

    ["mod_jatu_encampment_ruins",
     "Jatu Encampment Ruins",
     sf_generate | sf_battle_scene,
     "scn_steppe_encounter",
     [("exit", 0, 0)],
     [("mod_noldor_relic_chest", 280, 310)],  # chest holding the quest item
     [],
     (0, 400, 0, 400),
     (200, 200)],
]
