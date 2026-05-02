# Knight Orders in Prophesy of Pendor

Knight orders are elite factions the player can join or found. Each has unique
troops, gear, and quests. This document is a reference for modding their behavior.

## Vanilla Orders

| Order | Base Faction | Troop Key | Notes |
|---|---|---|---|
| Clarion Call of Pendor | Kingdom of Pendor | `npc_order_1_*` | Holy order, Pendor-aligned |
| Ebony Gauntlet | Kingdom of Pendor | `npc_order_2_*` | Heavy infantry focus |
| Dragon | Empire | `npc_order_3_*` | Dragon-themed cavalry |
| Radiant Cross | Empire | `npc_order_4_*` | Paladin style, anti-snake |
| Silvermist Rangers | Ravenstern | `npc_order_5_*` | Archer order |
| Immortals | D'Shar | `npc_order_6_*` | Elite D'Shar cavalry |
| Noldor Fellowship | Noldor | `npc_order_7_*` | Player-only, hardest to join |

## Order Quest Structure
Each order has a series of 3–5 quests unlocked by renown and relation thresholds.
These are defined in `module_quests.py` and triggered via `module_dialogs.py`.

## Adding a New Order (Checklist)
- [ ] Add order troops to `module_troops.py` (squire → knight → champion)
- [ ] Add order faction to `module_factions.py`
- [ ] Add order dialog chain to `module_dialogs.py` (application → test → acceptance)
- [ ] Add 3+ order quests to `module_quests.py`
- [ ] Add order banner item to `module_items.py`
- [ ] Add order hall scene to `module_scenes.py`
- [ ] Wire up spawn triggers in `module_parties.py`
- [ ] Test join flow and quest completion on a fresh save

## Notes on Balancing Orders
- Order troops should be about 15–20% stronger than top-tier kingdom troops
- Joining requirements: renown ≥ 600, relation with faction ≥ 20, skill check varies
- Order troops should have `tf_guarantee_*` flags for their signature gear
- Use `tf_no_cap_on_death` sparingly — only for named champions
