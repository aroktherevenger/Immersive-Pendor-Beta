# Tweaks 9 — Sieges

Source: https://pop3.fandom.com/wiki/Tweaks (Template:Tweaks_9)

---

## Tweak 9a — Reassign troops to infantry/archers during sieges
**File:** `mission_templates.txt`

Replaces lances with melee weapons during siege:
- Strength ≥ `13`: Morningstar (entry `1304`)
- Strength < `13`: Sword (entry `1190`)

Trigger counter: +1 for three sections (sally-outs, belfry, ladder). Compatible with Dynamic Reassignment submod.

---

## Tweak 9b — Disable ammo reduction on sally-outs
**File:** `mission_templates.txt`

Find `1 1 3 936748722493063848 0 6` → replace with `0`

---

## Tweak 9c — Fix sally-out consciousness bug
**File:** `mission_templates.txt`

Remove operation `2147484654 1 0` and decrease counter by 1 (12→11).  
Fixes bug where player knockout caused battle loss even if troops were winning.

---

## Tweak 9d — Disable defender charges
**File:** `mission_templates.txt`

Find 2 instances of the 26-operation trigger → replace with 7-operation trigger.  
Prevents AI defenders from automatically ordering "Charge!" after reinforcement waves.

---

## Tweak 9e — Change soldiers spawned in siege stages
**File:** `mission_templates.txt`

Town courtyard (2nd stage):
- Ally spawn: `8` soldiers
- Enemy spawn: `3` soldiers per point (7 points)

Castle hall (final stage):
- Attackers: `1` per point (3 points)
- Defenders: `1` per point (5 points)

---

## Tweak 9f — Change ammo refill rates in siege defense
**File:** `mission_templates.txt`

- AI refill rate: `60` seconds
- Player refill rate: `180` seconds

To revert player to 60s: delete the player trigger and decrease counters by 1 per section.

---

## Tweak 9g — Spread defending ranged reinforcements equally
**Files:** `scripts.txt`, `mission_templates.txt`

- Replace `siege_move_archers_to_archer_positions` script body (48 operations)
- Replace 92 instances of `33 3 1224979098644774914 1 3` with `30 2 1224979098644774914 1`
- Replace 10 instances of `-71` timestamp trigger

Affects all ranged defenders. Mutually exclusive with other tweaks that modify the archer positioning script.

---

## Tweak 9h — Adjust surrender requirements
**Files:** `conversation.txt`, `scripts.txt`

- Town food supply: `50000` units (100 days)
- Castle food supply: `1500` units (30 days)
- Removes garrison strength thresholds (`4000`/`2000` limits)
- Surrender ratios: `3×` (leave unmolested), `5×` (surrender with honor)

---

## Tweak 9i — Besiege friendly fiefs
**File:** `menus.txt`

Two approaches:
- Honest: `-40` relation penalty
- Barbaric: `-30` relation + scripted war declaration

Uses variables: `cheat_mode`, `g_player_besiege_town`, `g_encountered_party`  
Scripts: `set_player_relation_with_faction`, `diplomacy_start_war_between_kingdoms`, `player_leave_faction`
