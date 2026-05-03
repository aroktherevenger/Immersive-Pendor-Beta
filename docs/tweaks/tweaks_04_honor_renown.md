# Tweaks 4 — Honor & Renown

Source: https://pop3.fandom.com/wiki/Tweaks (Template:Tweaks_4)

---

## Tweak 4a — Disable honor loss when raiding caravans
**File:** `conversation.txt`  
**Credit:** BananaFruit

- Raiding caravans during peace: find `1224979098644774912 0 1 2 936748722493063450 -3` → change `-3` to `0`
- Demanding a toll: find `144115188075855914 1 2 936748722493063450 -1` → change `-1` to `0`

Removes honor penalties for raiding caravans and demanding tolls.

---

## Tweak 4b — Disable honor loss when refusing lord ransom
**File:** `menus.txt`  
**Credit:** BananaFruit

- Find `936748722493063450` near `-5` → change `-5` to `0`

Removes the 5-point honor penalty for refusing to pay ransom for captured lords.

---

## Tweak 4c — Disable honor loss for hostile village actions
**File:** `menus.txt`  
**Credit:** BananaFruit

- Razing village: find `1441151880758558915 1 2 936748722493063450 -1` → change `-1` to `0`
- Stealing cows: find `0 1 2 936748722493063450 -3 3 0 1 2` → change `-3` to `0`
- Stealing supplies: find `0 1 2 936748722493063450 -3 3 0 4 0` → change `-3` to `0`

---

## Tweak 4d — Change starting honor from character creation
**File:** `menus.txt`  
**Credit:** Alex Toews

Each character creation path grants different starting honor. Key strings and their values:
- Minor noble (Stage 1): `100 1 2 936748722493063450 1` — value is `1`
- From minor noble (Stage 4): `52 1 2 936748722493063450 2`
- From merchant captain: `58 1 2 936748722493063450 2`
- From former knight: `16 1 2 936748722493063450 10` and `30 1 2 936748722493063450 3`
- From retired adventurer: `432345564227567650 10 1 2 936748722493063450 3`
- From nomad clan leader: `432345564227567642 10 1 2 936748722493063450 3`
- From physician: `360287970189639680 10 1 2 936748722493063450 3`

---

## Tweak 4e — Change renown gained from battles
**File:** `scripts.txt`  
**Credit:** Alex Toews, Fandom User

In `calculate_renown_value` script:
- Enemy strength multiplier: `100`
- Friendly strength divisor: `100`
- Final ratio divisor: `5`
- Renown cap (squared): `2500` (= cap of 50)

To remove diminishing returns, in `change_troop_renown` script:
- Change `200` to `99999`

---

## Tweak 4f — Remove renown decay
**File:** `simple_triggers.txt`  
**Credit:** BananaFruit

Every 336 hours, renown is reduced by dividing by `200` (≈0.5% loss).  
To disable: change `200` to `99999`
