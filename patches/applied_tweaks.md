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

## Tweak 11c — Fix loot order bug (sort by level)
**File:** `scripts.txt`
**Status:** ✅ Applied

In `party_calculate_loot`: counter `336` → `359` (added 23 ops). Inserted selection-sort loop that finds the highest-level defeated troop and processes loot from them first, eliminating order-dependent loot RNG.

---

## Tweak 2q — Fix KO promotion reward tracking bug
**File:** `conversation.txt`
**Status:** ✅ Applied

In `dlga_start:hall_order_guard_talk`: replaced rank-up logic so each rank reward is granted explicitly when reached (not just the latest rank). Counter `18` → `19`. Prevents losing access to outfit rewards / Order Stronghold when ranking up multiple times in quick succession (e.g. creating 8-9 chapters in a row).
*Note: does not retroactively grant rewards already missed.*

---

## Tweak 2t — Sergeants get half stats from default training
**Status:** ⚠️ Reverted (replaced by 2u)

---

## Tweak 2u — KO upgrade system overhaul (Leonion)
**File:** `conversation.txt`
**Status:** ✅ Applied

Comprehensive rewrite of the KO/CKO war-room training system:
- **Cap:** Max 10 upgrade levels per order
- **Cost:** Scales by ×5/4 each level. Base 30 prestige + 50,000 denars at L1, ~213 prestige + 372k denars at L10. Total ~1.66M denars for full progression
- **Per-level bonuses:** Knights +1 STR/AGI/+10 WP; Sergeants +5 WP
- **Tier perks at specific levels:**
  - L1: Sg +10 WP
  - L2: Sg +1 STR/AGI
  - L3: Sg/Kn +1 Ironflesh
  - L4: Sg +1 STR/AGI
  - L5: Sg/Kn +10 WP
  - L6: Sg +1 PS/PT/PD
  - L7: Sg +1 STR/AGI/IF; Kn +1 IF
  - L8: Kn +1 PS/PT/PD/+10 WP
  - L9: Sg +1 STR/AGI/+10 WP
  - L10: Kn/Sg +1 PS/PT/PD
- Three dialogue lines fully replaced; menu now shows order name; done dialogue routes back to war room menu (so you can keep upgrading)

---

## Tweak 5b — Inquisition hostile to Singalians and Outlaws
**File:** `factions.txt`
**Status:** ✅ Applied (requires new game for full effect)

Faction relation matrix updated:
- `fac_inquisition` row: index 2 (outlaws) `0.0`→`-0.1`; index 40 (singalians) `0.0`→`-0.2`
- `fac_outlaws` row: index 43 (inquisition) `0.0`→`-0.1`
- `fac_singalians` row: index 43 (inquisition) `0.0`→`-0.2`

---

## Tweak 5k + 14c (combined boost) — Boost relation & honor quest rewards
**File:** `conversation.txt`
**Status:** ✅ Applied

Mass-edit via regex to make Pendor less grindy on relations/honor:
- All `change_player_relation_with_center` (town/village) positive values: ×1.5 (21 instances)
- All `change_player_relation_with_troop` (lord) positive values: ×1.5; negative penalties halved (83 instances)
- All `change_player_honor` positive values: ×1.5; negative penalties halved (46 instances)

Examples: Town `1`→`2`, town `5`→`7`, lord `9`→`13`, lord penalty `-30`→`-15`, honor `2`→`3`.

---

## Tweak 17x — Brother Randalf reveals all bandit lairs
**Files:** `quick_strings.txt`, `conversation.txt`
**Status:** ✅ Applied

After buying the Al-Aziz mines map, Brother Randalf now offers to reveal all bandit lair locations on the world map for 1000 denars. Manually re-trigger to refresh new lairs.

---

## Tweak 16l — Bodyguard companions in scenes
**Files:** `conversation.txt`, `mission_templates.txt`
**Status:** ✅ Applied

Up to 4 of your top companions follow you into town/village/castle scenes. Number = Leadership/3 + Renown/400 (max 4).
- `conversation.txt`: `dlga_start:close_window.11` counter 4→5 with new context flag
- `mission_templates.txt`: 6 sections updated with counter+3 and 3 new triggers each (`mst_town_default`, `mst_town_center`, `mst_village_center`, `mst_bandits_at_night`, `mst_castle_visit`, `mst_sneak_caught_fight`)

---

## Tweak 15g — Take equipment from captured lords
**File:** `conversation.txt`
**Status:** ✅ Applied

Added new dialogue option `dlga_prisoner_chat_noble2:close_window.4` to undress captured non-king lords. Cost: -25 relation, -1 honor. Lord auto-released after. Counter 4159→4160.

---

## Tweak 16n — Hire unique spawn leaders as companions when captured
**Files:** `dialog_states.txt`, `conversation.txt`, `scripts.txt`
**Status:** ✅ Applied

Adds a "How about you join my company?" option when talking to captured unique spawn leaders.
- `dialog_states.txt`: added `prisoner_chat_join` (state ID 1878)
- `conversation.txt`: counter 4160→4163; 3 new dialogue lines after `dlga_prisoner_chat_sig3:close_window.1`
- `scripts.txt`: `party_remove_all_companions` op counter 67→68 (added unique spawn protection); replaced body of `encounter_calculate_fit` (counter 86→83) to allow capturing unique spawns when Noldor lords are involved

---

## Tweak 21m — Fix ambient sounds persisting after leaving taverns/arenas
**Files:** `variables.txt`, `mission_templates.txt`
**Status:** ✅ Applied

- `variables.txt`: added `ambiance_channel` (line 1450, ID `144115188075857321`)
- `mission_templates.txt mst_town_default`: counter 19→16; deleted 3 stale sound triggers; replaced -19/-21 triggers with channel-aware versions
- `mission_templates.txt mst_arena_melee_fight`: replaced 0.2/-30/-29 triggers with channel-aware versions

---

## Tweak 12g — Increase merchant wealth based on prosperity
**File:** `simple_triggers.txt`
**Status:** ✅ Applied (approach 2)

Counter 134→135. Added new 24h trigger that scales merchant wealth based on town prosperity:
- Max wealth at 300 prosperity = 12000 denars (weapons/armor/horse merchants), 16000 (goods merchants)
- Builds up over 3 days

---

## Tweak 17a — Drastically reduce food consumption
**File:** `simple_triggers.txt`
**Status:** ✅ Applied

Food consumption interval `14h` → `168h` (every 7 days instead of every 14 hours). 12× slower consumption — effectively no more food grind.

---

## Tweak 15d — Reduce lord escape chances (revised)
**File:** `simple_triggers.txt`
**Status:** ✅ Applied (adjusted from initial too-strict version)

- **Player party escape chance: kept at vanilla** `(400 - 20×PrisonerMgmt)/10` (40%→20% based on PM)
- **Garrison escape chance halved:** `(200 - 10×StewardPrisonerMgmt)/10` → `(100 - 5×StewardPrisonerMgmt)/10` (10%→5% based on PM)

Field captures stay challenging; once you stash them in a fief, they're much more secure.

---

## Tweak 8d — Whistle for nearest horse
**Files:** `Sounds/horse_whistle.ogg`, `sounds.txt`, `mission_templates.txt`
**Status:** ✅ Applied

Press **H** in field battles or village bandit fights to whistle for the nearest horse within 50m. Horse comes to where you stood when you pressed the button (doesn't track you).
- Copied `horse_whistle.ogg` to PoP `Sounds/` folder
- `sounds.txt`: counter 1342→1343; added `horse_whistle.ogg 2720` entry; secondary counter 639→640; appended `snd_horse_whistle 2720 1 1342 0`
- `mission_templates.txt`: `mst_lead_charge` counter 66→67 with new trigger; `mst_village_attack_bandits` counter 24→25 with new trigger

---

## Tweak 16p — Restore equipment of mid/high-tier companions
**Files:** `troops.txt`, `conversation.txt`
**Status:** ✅ Applied (requires new game for full effect)

Companions costing 3000+ denars to hire get top-tier gear and locked inventories until certain levels:

**Equipment overhauls in `troops.txt`:**
- **Lethaldiran [30]**: Noldor Runesword, Noble Shield, Composite Bow, Arrows, Captain Helm with Hood, Trimmed Ranger Garb, Enchanted Boots, Ornate Gloves, Grey Warhorse
- **Sir Jocelyn [25]**: Ebony Knight Sword, Black & White Heater Shield, Siege Crossbow + Bolts, Dark Knight Helm, Pendor Ornate Plate, Empire Shynbaulds, Supreme Steel Gauntlets, Ironbred Charger
- **Sir Alistair [25]**: Ebony Noble Sword, Order of Eventide Kite Shield, Long Dark Knight Lance, Black Helm with Feathers, Eventide Plate, Ebony Greaves, Black Steel Gauntlets, Black Leather Draped Warhorse
- **Sir Rayne [20]**: Silvered Longsword, Order of the Falcon Kite Shield, Long Blue Knight Lance, Silvermist Helm with Mail, Falcon Plate, Silver & Gold Greaves, Silver Gauntlets, Falcon Steed
- **Frederick [25]**: Zweihander, Royal Hounskull Bascinet (Open), Forlorn Hope Heavy Plate, Empire Shynbaulds, Mettenheim Steel Mittens
- **Ediz [15]**: Singalian Noble Sabre, Embossed Round Shield, Short Composite Bow, Bodkin Arrows, Jatu Cavalry Helmet, Singalian Black Studded Leather, Splinted Greaves, Dark Leather Gloves, Leather Draped Horse. Stats: level 9→10, riding/shield boosted, 1h profs 140→150
- **Donavan [15]**: Barclay Noble Sword, Great Lance, Arquebus, Heater Shield (Twin Eagles), Barclay Pot Helmet, Cuir Bouilli, Mail Boots, Mail Mittens, War Horse. Riding 3→4
- **Diev [20]**: Ravenstern Great Sword, Long Composite Bow, Ranger Arrows, Kierguard Helm, Ravenstern Kierguard Plate, Polished Steel Boots, Hourglass Gauntlets. 1h 220→200, 2h 200→220
- **Sir Roland [30]**: Ebony Arming Sword, Long Dawn Knight Lance, Order of the Dawn Heater Shield, Silver Helmet (Open), Silver Ornate Plated Armor with Cape, Silver & Gold Greaves, Supreme Silver Gauntlets, White Draped Warhorse
- **Sigismund [25]**: Pendor Great Sword, Siege Crossbow, Siege Bolts, Open Unicorn Helm, Ebony Platemail, Black Greaves, Ebony Gauntlets
- **Boadice [30]**: Rune Bastard Sword, Long Blue Knight Lance, Ancient Engraved Shield, Jarids, Veccavian Open Helm with Tail, Unicorn Plate, Silver & Gold Greaves, Supreme Silver Gauntlets, Unicorn Steed

**Inventory locks in `conversation.txt`:**
- `dlga_member_trade:do_member_trade`: 2 lines → 12 lines (each companion blocked until their stage level [15/20/25/30])
- `dlga_member_automanage_report:member_talk`: 1 line → 11 lines
- Counter 4163→4183 (+20)

---

## Tweak 15c — Attack any lord without restrictions
**File:** `conversation.txt`
**Status:** ✅ Applied

Removes the relation-check that blocks attacking neutral/friendly lords on the world map. Plus a safety: attacking your own kingdom's lords doesn't trigger the make-kingdom-hostile script.
- `dlga_lord_talk:party_encounter_lord_hostile_ultimatum_surrender`: counter 3→2; removed `2147483678 2 144115188075856958 0` (relation gate)
- `dlga_party_encounter_lord_hostile_ultimatum_surrender:close_window`: counter 8→11; wrapped the kingdom-hostile script call in a check (skip if attacking own kingdom)

---

## Tweak 15n — Give money to poor friendly lords
**Files:** `dialog_states.txt`, `conversation.txt`
**Status:** ✅ Applied

New dialogue option: give 10,000 denars to friendly (relation ≥30) poor (wealth ≤2000) lords for +8 relation. The money goes to their budget — they actually spend it on troops.
- `dialog_states.txt`: added `lord_sponsor` (state ID 1879)
- `conversation.txt`: counter 4183→4185; added 2 dialogue lines after `dlga_lord_talk:lord_predemand`

---

## 🛠️ Crash Fix (2026-05-03)
**File:** `conversation.txt`

Two crash dumps reported. Root cause: 5 blank lines accidentally inserted by Edit operations during 13l, 17x, 16n, 15g, 15n (each `new_string` ended with a trailing newline that became a blank line). Game engine expects exactly `N` dialogues after the counter — blank lines shift offsets and corrupt parsing.

Removed 5 blank lines at original positions 397, 1621, 2441, 3719, 3742. Counter (4185) now matches actual dialogue count exactly.

---

## 🛠️ Crash Fix #2 (2026-05-03 - "out of memory")
**File:** `conversation.txt`

User reported a second crash with "out of memory" exception during conversation loading.

Root cause: Tweak **14g** (looter quest aggressive approach) had a counter mismatch. The dialogue counter said `26` ops but the body actually had `27` ops because the original `1642 2 72057594037927936 0` operation was supposed to be replaced (per wiki) but I kept it accidentally — adding the new ops on top instead of replacing.

The engine reads exactly `26` ops, then reads `1642 2 72057594037927936 0` as if it was the dialogue text, treating subsequent tokens as dialogue structure → garbage offsets → memory allocation runs wild → OOM.

Removed the extra `1642 2 72057594037927936 0` op from `dlga_merchant_quest_looters_brief:close_window`. Verified all 4185 dialogue lines now parse cleanly.

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
