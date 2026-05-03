# Tweaks 8 — Field & Village Battles

Source: https://pop3.fandom.com/wiki/Tweaks (Template:Tweaks_8)

---

## Tweak 8a — Keep dismounted cavalry in their own group
**File:** `mission_templates.txt`

Decreases trigger counter: 66→62. Optionally replaces lances with:
- Morningstar (entry `1304`) for low strength (< `13`)
- Sword (entry `1190`) for higher strength

---

## Tweak 8b — Reassign dehorsed horse archers to archer group
**File:** `mission_templates.txt`

Moves dehorsed archers to archer divisions when ammo < `5`.  
Replaces lances with sword/morningstar based on strength `13`.  
Trigger counter changes: `mst_lead_charge` 66→67, `mst_village_attack_bandits` 24→26, `mst_village_raid` 27→29

---

## Tweak 8c — Reassign mounted foot units to cavalry group
**Files:** `mission_templates.txt`, `menus.txt`, `scripts.txt`

- Sword item ID: `288230376151712934`
- Long Knight Lance item ID: `288230376151713113`
- Strength requirement: `15`, Level requirement: `35`

---

## Tweak 8d — Whistle for nearest horse
**Files:** `sounds.txt`, `mission_templates.txt`

- Sound file: `horse_whistle.ogg`
- Detection radius: `50` meters
- Activation key: `H`

---

## Tweak 8e — Make horses not get halted by polearms under damage threshold
**Files:** `module.ini`, `mission_templates.txt`

In `module.ini`: `horses_rear_with_attack = 0`  
Damage threshold before rearing: `30` (armored and standard horses), never (undead)  
Rider dropout on rear: `0` (disabled) or `1` (enabled)

---

## Tweak 8f — Change minimum time before enemies can flee
**File:** `scripts.txt` (scripts: `decide_run_away_or_not`, `formation_decide_run_away_or_not`)

- PoP default: `180` seconds
- Native default: `45` seconds

---

## Tweak 8g — Change static preset battlefield sizes
**Files:** `scenes.txt`, `quick_strings.txt`

- Small: `240×240` m
- Normal: `550×550` m
- Large: `840×840` m
- Min: `140×140` m, Max: `840×840` m

---

## Tweak 8h — Match battle size with max troops on battlefield
**File:** `module.ini`

- `battle_size_max`: `530`→`420`
- Hardcap player troops: `280`
- Battle advantage range: `[-12, 12]`

---

## Tweak 8i — Fight battles without party, keep full benefits
**File:** `menus.txt`

- `menu_simple_encounter` submenu counter: 5→6
- `menu_battle_debrief` operation counter: 157→162

---

## Tweak 8j — Swap spawn points of farmers and bandits in village infestations
**File:** `mission_templates.txt`

Swap farmer spawn `1` ↔ bandit spawn `3` for realistic village defense positioning.

---

## Tweak 8k — Disable village battle scenes when fighting lords
**File:** `menus.txt`

- Decrease operation counter: 123→100 (removes 23-operation block)
- Forces lord raids to use field battle scenes instead of village scenes

---

## Tweak 8l — Adjust max party size for village defense resistance
**File:** `menus.txt`

Default threshold: `25` troops. Increase to allow larger parties before villagers counter-attack.
