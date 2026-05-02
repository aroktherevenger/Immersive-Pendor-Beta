# module_quests.py
# Quest definitions added by this mod.

from header_common import *
from module_constants import *

# Quest flags
qf_default              = 0x00000000
qf_random_quest         = 0x00000001
qf_knight_order_quest   = 0x00000002

quests = [
    # Format: ["quest_id", "Quest Title", qf_flags, "Quest description text"]

    ["mod_quest_iron_circle_threat",
     "The Iron Circle Menace",
     qf_default,
     "Strange reports have reached you of a new cult calling itself the Iron Circle. "
     "They wear corrupted Pendor arms and seem to have ties to the Snake Cult. "
     "Investigate their stronghold and put an end to their leader, Valorian the Ironclad."],

    ["mod_quest_noldor_relic",
     "The Lost Star Quiver",
     qf_default,
     "A Noldor elder speaks of a sacred quiver of star-forged arrows lost during "
     "the Jatu raids a generation ago. Recover it from the Jatu encampment and "
     "return it to earn the Noldor's gratitude — and a reward befitting their craft."],

    ["mod_quest_veteran_training",
     "Forging Veterans",
     qf_knight_order_quest,
     "The local garrison commander needs experienced soldiers. Train a group of "
     "raw recruits into Veteran Pendor Footmen by taking them into battle. "
     "Return when they have proven themselves."],
]
