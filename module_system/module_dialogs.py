# module_dialogs.py
# NPC dialogue trees added by this mod.
# Uses M&B's dialog system: (speaker, partner, conditions, text, consequence, next_state)

from header_common import *
from module_constants import *

# Dialog speaker tokens (mirrors M&B header_dialogs.py)
anyone          = "anyone"
plyr            = "plyr"
party_tpl       = "party_tpl"
tavernkeeper    = "tavernkeeper"
village_elder   = "village_elder"
town_notable    = "town_notable"
lord            = "lord"
mercenary       = "mercenary"

# Dialog states
start           = "start"
close_window    = "close_window"

dialogs = [
    # ── Iron Circle Champion encounter ────────────────────────────────────────
    # When the player encounters Valorian the Ironclad
    ("mod_iron_circle_champion", anyone,
     start, [],
     "So, another champion of the weak kingdoms comes to test the Iron Circle. "
     "We are beyond your petty wars, {player_name}. Leave now, or face oblivion.",
     [], "mod_valorian_response"),

    (plyr, "mod_iron_circle_champion",
     "mod_valorian_response", [],
     "I've come to put an end to your cult, Valorian. Stand down or face me.",
     [], "mod_valorian_fight"),

    (plyr, "mod_iron_circle_champion",
     "mod_valorian_response", [],
     "Perhaps there is room for... negotiation?",
     [], "mod_valorian_negotiate"),

    ("mod_iron_circle_champion", anyone,
     "mod_valorian_fight", [],
     "Ha! Then let blood decide. Iron Circle, to arms!",
     [("call_script", "script_mod_start_iron_circle_battle")],
     close_window),

    ("mod_iron_circle_champion", anyone,
     "mod_valorian_negotiate", [],
     "Interesting. You are either very clever or very foolish. "
     "Bring me proof of your worth — destroy one of the Noldor's border patrols — "
     "and we will speak again.",
     [], close_window),

    # ── Tavernkeeper rumor about Iron Circle ──────────────────────────────────
    (tavernkeeper, anyone,
     start,
     [("check_quest_active", "mod_quest_iron_circle_threat")],
     "You look like someone who asks questions. I've heard travelers speak of "
     "dark-armored men camping near the old ruins east of Sarleon. "
     "Best avoided, if you ask me.",
     [], close_window),

    # ── Noldor elder — relic quest giver ─────────────────────────────────────
    (anyone, anyone,
     "mod_noldor_elder_start", [],
     "The stars weep for what was lost. Our quiver of star-forged arrows, "
     "stolen by Jatu raiders before you were born. If you would retrieve it, "
     "the Noldor would be... grateful.",
     [], "mod_noldor_relic_accept"),

    (plyr, anyone,
     "mod_noldor_relic_accept", [],
     "I will recover your quiver.",
     [("start_quest", "mod_quest_noldor_relic")],
     close_window),
]
