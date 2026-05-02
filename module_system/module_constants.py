# Project-wide constants for this PoP mod.
# Add new named constants here rather than using magic numbers.

# ── Version ───────────────────────────────────────────────────────────────────
MOD_VERSION = "0.1.0"
POP_BASE_VERSION = "3.9.5"

# ── Balance Multipliers ───────────────────────────────────────────────────────
# Tweak these to do broad rebalances without touching every troop/item.
KNIGHT_ORDER_XP_MULT    = 1.0   # XP required to join/rank up a knight order
NOLDOR_STRENGTH_MULT    = 1.0   # Overall stat multiplier for Noldor troops
SNAKE_CULT_SPAWN_RATE   = 1.0   # Multiplier on Snake Cult party spawn frequency
JATU_HORDE_SIZE_MULT    = 1.0   # Multiplier on Jatu horde party sizes

# ── Knight Order IDs (for cross-file references) ──────────────────────────────
ORDER_CLARION_CALL      = "clarion_call"
ORDER_EBONY_GAUNTLET    = "ebony_gauntlet"
ORDER_DRAGON            = "dragon"
ORDER_SUNNI             = "sunni"
ORDER_SILVERMIST        = "silvermist_rangers"
ORDER_IMMORTALS         = "immortals"
ORDER_NOLDOR            = "noldor_fellowship"

# ── Unique Spawn Names ────────────────────────────────────────────────────────
# Reference these when linking quests/dialogs to unique lords
UNIQUE_SPAWNS = [
    "maltise_the_accursed",
    "kodan_the_blade",
    "ansen_the_grey",
    "ueruen_the_blessed",
    "valdis_the_dragon",
]

# ── Loot Table Weights ────────────────────────────────────────────────────────
LOOT_COMMON     = 100
LOOT_UNCOMMON   = 40
LOOT_RARE       = 10
LOOT_LEGENDARY  = 2
