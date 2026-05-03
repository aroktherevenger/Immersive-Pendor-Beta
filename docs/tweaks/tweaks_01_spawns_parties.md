# Tweaks 1 — Spawns & Parties

Source: https://pop3.fandom.com/wiki/Tweaks (Template:Tweaks_1)

---

## Tweak 1a — Capture chances for Unique Spawn Leaders and Lords
**Files:** `menus.txt`, `scripts.txt`, `quick_strings.txt`, `simple_triggers.txt`

Every 120 hours a random value (0–99) is rolled. A spawn leader is captured if:
`x + (prisoner_management_skill × 5) >= 60`  
Change `60` to adjust capture difficulty (-100 = always, 150 = nearly impossible).

---

## Tweak 1b — Relation threshold for capturing spawn leaders
**File:** `menus.txt`

Default threshold: `0`. Increase to only capture leaders when relation is above a certain value.

---

## Tweak 1c — Spawn rate and delay of minor faction armies
**File:** `scripts.txt`

- GROUP A spawn rate: `400` (decrease to spawn more frequently)
- GROUP B spawn rate: `100` (10% base chance every 96 hours)
- Spawn delays vary by faction: `14`, `5`, `1000`, `100`, `0` hours

GROUP A parties: Vanskerry Sea Raider Army, Peasant Revolt Army, Azi Dahaka Death Cult Marauders, Burilgi, Oswald de Fleur, Boris the Raven, Meregan Kierlic, Alaric Von Brouhaha, Kodan Ironsword, Sheik Shalavan, Syla Uzas  
GROUP B parties: Tercio Villaviciosia, Conquistadoros de Aventura, Obrist Heynrich, Freikorps Mettenheim, Mettenheim Expeditionary Force, Renegade Witch Hunt, Daughters of Persinoe, Melitine forces

---

## Tweak 1d — Obtain special axes from captured NPCs
**File:** `conversation.txt`

Add two new dialogue entries to take Maltise's Asp Throwing Axes and Wolfbode the Slayer's axe when they are captured.

---

## Tweak 1e — Prevent special NPCs from leaving Pendor
**File:** `conversation.txt`

Affected NPCs: Aeldarian, Ithilrandir, Maltise. Prevents them from leaving so you can keep farming Qualis Gems etc.  
Replacements: Noldor Composite Bow (Aeldarian), Noldor War Sword (Ithilrandir)

---

## Tweak 1f — Eyegrim the Devourer party limits and growth
**File:** `simple_triggers.txt`

- Party soft cap: `5000`
- Daily conversion: 100% of living party members + 25% of prisoners → undead
- Can restrict to only converting rescued prisoners

---

## Tweak 1g — Minor faction spawn composition
**File:** `party_templates.txt` (use Party Templates Editor)

Recommended changes:
- Snake Cult: Add Snake Cult Leader [0–1]
- Heretic Army: Swap Adventurer for Heretic High Priest [6–24]
- Jatu Army: Replace Adventurer with Noldor Hunter [0–2]
- K'Juda: Noldor Hunter [1–3] → Jatu Warlord [20–50]
- Mettenheim: Swap troop ratios, add Heavy Crossbow [30–60]
- Vanskerry: Hero Adventurer → Vanskerry Leader; Adventurer → Queen Agnus Freebooter

---

## Tweak 1h — Unique Spawn town sacking conditions
**File:** `simple_triggers.txt`

Conditions for a spawn to sack a town (checked every `14` hours):
- Minimum autocalc strength: `30,000`
- Maximum distance to town: `5` units
- Random chance: `15` (from 0–100)

---

## Tweak 1i — Automatic spawn location notifications
**File:** `simple_triggers.txt`

Adds notification messages about spawn locations every `12` hours (adjustable).  
Note: Peasant Revolt Armies not included; some spawns may appear listed near two fiefs.

---

## Tweak 1j — Sighting report cost for spawn information
**File:** `conversation.txt`

Default cost: `2000` gold. Search `2000_shiny_gold_pieces` — 4 instances to change.

---

## Tweak 1k — Count enemy and allied units on world map
**Files:** `quick_strings.txt`, `scripts.txt`

Hold Left Shift + right-click a party name to see total allies and enemies within `5` units.  
Key string: `qstr_enemy_num:{reg5} Number_of_enemies:{reg5}_Number_of_allies:{reg6}`

---

## Tweak 1l — Spawn frequency for various parties
**File:** `simple_triggers.txt`

Trigger frequencies (in hours):
- Red Brotherhood, D'Shar Raiders, Snake Cult, Outlaws, Vanskerry, Singalian: `12`
- Noldor patrols, Heretic Coven, Three Seers, Inquisition, KO, Jatu, Mystmountain: `16`
- Rogue Knights, Adventurers: `96`
- Deserters, Militia Patrols, Signature Patrols: `168`
- Azi Dahaka Death Cult: `120`

Decrease value = more frequent spawns.

---

## Tweak 1m — Hired assassin spawning chance
**File:** `simple_triggers.txt`

Default: `10`% chance per night when resting in a walled fief not owned by you.

---

## Tweak 1n — Maximum party count on world map
**Files:** `scripts.txt`, `conversation.txt`

Party caps:
- Red Brotherhood: `13`, Singalian Slavers: `10`, Azi Dahaka: `4`
- Deserters: `8`, Vanskerry: `15`, Signature Patrols (each): `4`
- Outlaw Bands: `30`, Militia Patrols (auto-created): `9`
- Total militia patrols all kingdoms: `20`

---

## Tweak 1o — Deserter party size
**File:** `scripts.txt`

Formula: random between `10` and `(11 + (PlayerLevel × 2) - 1)`  
At level 10: parties range from 10 to 30 units.

---

## Tweak 1p — Level multiplier for party size growth
**File:** `scripts.txt` (script: `update_party_creation_random_limits`)

Default multiplier: `4`. Increase to make parties grow faster with player level.

---

## Tweak 1q — Militia patrol troop capacity
**File:** `conversation.txt`

Default cap: `100` troops. Find 3 instances in militia dialogue entries.

---

## Tweak 1r — Militia patrols joining player battles
**File:** `scripts.txt` (script: `let_nearby_parties_join_current_battle`)

Change counter from 118 to 120 operations. Replace faction check to include militia (faction ID `576460752303423495`).

---

## Tweak 1s — Patrol patrolling radius
**Files:** `scripts.txt`, `conversation.txt`

Default radius: `5` (= 30 in-game units; values × 6 = actual distance).  
Affects: village militia, Errant Knights, independent KO, stronghold KO patrols.

---

## Tweak 1t — Prevent Noldor from attacking civilians
**Files:** `scripts.txt`, `party_templates.txt`

Option 1: Add new script `game_check_party_sees_party`  
Option 2 (Party Editor): Mark Militia_Patrol (#7), Village_Farmers (#97), Caravan (#109) as "civilian"; mark Noldor parties as "dont attack civilians"

---

## Tweak 1u — Cattle movement speed
**File:** `troops.txt` (use Morgh's Editor)

Check 'Mounted' flag on cattle, set Riding: 0→10, Pathfinding: 0→10. Requires new game.

---

## Tweak 1v — Party map speed
**File:** `scripts.txt` (new script: `game_get_party_speed_multiplier`)

- Global modifier: `150`% (50% increase)
- Speed reduction factor: `200`
- Player party bonus: `110`%
- Unique spawn bonus: `110`%

---

## Tweak 1w — Player party size
**File:** `scripts.txt` (script: `game_get_party_companion_limit`)

Formula: `10 + (leadership × 10) + (charisma × 2) + (renown ÷ 25)`

---

## Tweak 1x — Prevent hateful factions from disappearing
**File:** `scripts.txt` (script: `determine_victory_conditions_and_text`, line 1191)

Add 22 operations (counter: 392→414) to check faction survival until Pendor is unified. Affects 4 instances of despawn logic.
