# Applied Tweaks Log

Tracks all tweaks applied to the PoP installation at:
`C:\Program Files (x86)\Steam\steamapps\common\MountBlade Warband\Modules\Prophesy of Pendor V3.9.5`

To revert any tweak, use the original values listed below.

---

## Tweak 21f — Increase XP gain rates
**File:** `module.ini`
**Status:** ✅ Applied

| Setting | Before | After |
|---------|--------|-------|
| `player_xp_multiplier` | `1.5` | `3.0` |
| `hero_xp_multiplier` | `1.5` | `3.0` |
| `regulars_xp_multiplier` | `1.0` | `2.0` |

---

## Tweak 21b — Remove luck decay
**File:** `simple_triggers.txt`
**Status:** ✅ Applied

Original line 22:
```
200.000000  2 2106 2 144115188075856083 1 2111 2 144115188075856083 25 
```
Replaced with empty trigger:
```
200.000000  0
```

---

## Tweak 9b — Disable ammo reduction on sally-outs
**File:** `mission_templates.txt`
**Status:** ✅ Applied

Original:
```
0.100000 0.500000 100000000.000000  0  1 1 3 936748722493063848 0 6 
```
Replaced with:
```
0.100000 0.500000 100000000.000000  0  0
```

---

## Tweak 17b — Faster garrison/lord party training
**File:** `simple_triggers.txt`
**Status:** ✅ Applied

Training trigger interval halved so troops level up twice as fast:
- `48.000000` → `24.000000` (line 34, the garrison training trigger)

---

## Tweak 1a — Easier unique spawn capture
**Files:** `menus.txt`, `scripts.txt`
**Status:** ✅ Applied

Capture threshold lowered from `60` to `40` (roll + prisoner_management×5 >= 40):
- `menus.txt`: `2147483678 2 1224979098644774956 60` → `...956 40`
- `scripts.txt`: `30 2 1224979098644774957 60` → `...957 40` (both Eyegrim and Three Seers instances)

---

## Tweak 16c — Disable companion complaints
**Files:** `scripts.txt`, `simple_triggers.txt`
**Status:** ✅ Applied (complaint triggers disabled; menu button skipped)

- `scripts.txt`: `2133 2 144115188075857049 74 1025` → `...74 31` (disables complaint score check)
- `simple_triggers.txt`: `1025 2 144115188075855964 -1` → `31 2 ...` (disables food complaint trigger)
- `simple_triggers.txt`: `1025 2 144115188075855882 -1` → `31 2 ...` (disables personality complaint trigger)

---

## Tweak 10t — Participate in battles while wounded
**File:** `menus.txt`
**Status:** ✅ Applied

Removed `2147485156 1 360287970189639680` (wounded check) from 9 battle entry menu options:
- `mno_encounter_attack`, `mno_join_attack`, `mno_join_siege_with_allies`
- `mno_castle_lead_attack`, `mno_siege_defender_join_battle`, `mno_village_attack_bandits`
- `mno_castle_attack_surprise`, `mno_castle_attack`, `mno_camp_train_melee`

---

## Tweak 14f — Guildmaster auto-offers new quest when you decline
**File:** `conversation.txt`
**Status:** ✅ Applied

Removed the condition checking if you've already been given a quest (so guildmaster always offers):
- Condition count: `3` → `2`
- Removed: `2147483679 2 144115188075856101 144115188075855892`

---

## Tweak 11a — Increase loot from battles
**File:** `scripts.txt`
**Status:** ✅ Applied

Loot divisor halved (twice as much loot drops per battle):
- `2108 2 1224979098644774927 8` → `...927 4`

---

## Tweak 16a — Companions cannot leave party
**Files:** `conversation.txt`, `triggers.txt`, `simple_triggers.txt`
**Status:** ✅ Applied

- `conversation.txt`: removed condition from `member_separate_confirm` (condition count 1→0)
- `conversation.txt`: added always-fail condition `31 2 1 0` to `companion_quitting` (count 0→1)
- `triggers.txt`: `2133 2 144115188075855884 1224979098644774918` → `...855884 0` (companion stored as nobody)
- `simple_triggers.txt`: counter 101→102; inserted `31 2 1 0` before `110 1 144115188075855884`

---

## Tweak 12k — Sell garrisoned prisoners to ransom brokers
**File:** `scripts.txt`
**Status:** ✅ Applied

Extended `sell_all_prisoners` script to also loop through garrison prisoners:
- Counter: `13` → `28`
- Inserted garrison prisoner loop after party prisoner block (before final faction check)

---

## Tweak 19c — Prisoner capacity scales with party size
**File:** `scripts.txt`
**Status:** ✅ Applied

Replaced `game_get_party_prisoner_limit` with party-size formula:
- Old: fixed prisoner cap based on prisoner management skill only
- New: `capacity = (party_size - 1) / (5 - 0.3 × Prisoner_Management)`
- Script counter: `6` → `10`

---

## Tweak 12d — Better enterprise production rates
**File:** `scripts.txt`
**Status:** ✅ Applied

All enterprise labor/upkeep costs halved (slot 53). Mill/Bakery output also doubled (30→60):
- Mill/Bakery (711861): output 30→60, labor 50→25
- Brewery (711849): labor 120→60
- Wine Press (711848): labor 220→110
- Tannery (711845): labor 220→110
- Velvet Weavery (711838): labor 250→125
- Wool Weavery (711833): labor 450→225
- Silver Smith (711836): labor 250→125
- Olive Press (711843): labor 410→205
- Iron Mine (711841): labor 1025→512

---

## Tweak 9c — Fix sally-out consciousness bug
**File:** `mission_templates.txt`
**Status:** ✅ Applied

Removed `2147484654 1 0` (bad consciousness op) from `mst_castle_attack_walls_defenders_sally` trigger.
Counter decreased: `12` → `11`

---

## Tweak 13v — Faster/cheaper fief improvements
**Files:** `menus.txt`, `simple_triggers.txt`, `scripts.txt`
**Status:** ✅ Applied

- `menus.txt`: build speed divisor `150` → `300` (builds twice as fast per denar spent)
- `simple_triggers.txt`: auto-repair frequency `168.07h` → `84h` (twice as frequent)
- `scripts.txt`: removed repair cost op `1529 2 360287970189639680 1224979098644774921`; counter 65→64

---

## Tweak 14g (partial) — Fix looter quest: make looters approach aggressively
**File:** `conversation.txt`
**Status:** ✅ Applied (Fix 3 of 3; Fixes 1+2 skipped — too complex)

In `dlga_merchant_quest_looters_brief:close_window`: counter 25→26, replaced passive assignment block with aggressive approach ops (`1641`, `1639`, `1606`, `1607`).

---

## Tweak 3c — Cheaper/faster CKO equipping
**File:** `scripts.txt`
**Status:** ✅ Applied

In `get_item_upgrade_cost_and_time`:
- Time multiplier: `100` → `500` (equipping ~5x faster)
- Cost divisor: `1000` → `200` (5x cheaper)
- Minimum cost: `1000` → `100` denars

---

## Tweak 13l — Send troops to any owned walled fief remotely
**Files:** `variables.txt`, `dialog_states.txt`, `conversation.txt`, `simple_triggers.txt`
**Status:** ✅ Applied

Adds new village elder dialogue option to send troops from your party to any owned walled fief for 500 denars (covers food).

- `variables.txt`: added `send_troops_tweak` (line 1449, ID `144115188075857320`)
- `dialog_states.txt`: added 4 new states (1874-1877): `send_reinf_to_fief1` through `send_reinf_to_fief4`
- `conversation.txt`: counter `4152` → `4158`; added 6 new dialogue lines after `dlga_village_elder_talk:village_elder_request_mission_ask`
- `simple_triggers.txt`: counter `133` → `134`; added new trigger at end of file (handles the actual troop transfer)

---

## Tweak 2g — Guarantee KO chapters at game start
**File:** `scripts.txt`
**Status:** ✅ Applied (requires new game)

All KO chapter spawn probabilities set to 100%:
- Silvermists (648518346341351456): `31` → `100`
- Ebony Gauntlet (648518346341351461): `31`/`46` → `100`/`100`
- Radiant Cross (648518346341351448): `81`/`91` → `100`/`100`
- Falcons (648518346341351500): `51` → `100`
- Windriders (648518346341351462): `21` → `100`
- Dragons (648518346341351453): `31` → `100`
- Lions (648518346341351452): `11` → `100`
