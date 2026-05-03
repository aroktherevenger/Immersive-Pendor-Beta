# Tweaks 5 — Relations & Diplomacy

Source: https://pop3.fandom.com/wiki/Tweaks (Template:Tweaks_5)

---

## Tweak 5a — Remove faction relation caps
**File:** `simple_triggers.txt`

Every 168 hours, relations are capped at these values:
- Rogue Knights: `10`, Heretics: `-15`, Jatu: `2`, Snake Cult: `-5`
- Adventurer Companies: `10`, Mystmountain: `10`, D'Shar Raiders: `10`, Singalians: `10`

Find the trigger at `168.000000` with ID `214`, locate each cap value and change it. Or reduce the `214` counter to `165` and delete the entire cap block to remove all caps.

---

## Tweak 5b — Make Inquisition hostile to Singalians and Outlaws
**File:** `factions.txt` (use Morgh's Editor)

Set Inquisition (#43) relations:
- Outlaws (#2): `-0.1`
- Singalians (#40): `-0.2`

Also set reciprocal values on Outlaws and Singalians toward Inquisition. Requires new game.

---

## Tweak 5c — Change relation gained/lost in battle
**File:** `menus.txt`

- Battle relation gain: find `2110 2 1224979098644774939 4` → change `4`
- King/queen penalty vs opposed faction: find two instances of `-10` → change both

---

## Tweak 5d — Adjust cost of buying peace
**File:** `conversation.txt`

Find `72057594037927952 1224979098644774915 50` → change `50` (the multiplier)
- `50` = default PoP cost
- `5` = 1/10th the cost
- `0` = free peace

---

## Tweak 5e — Remove relation hit for assigning fiefs to non-claimants
**File:** `conversation.txt`

Find `2107 2 1224979098644774919 -1` → change `-1` to `0`

---

## Tweak 5f — Change relation with vassals on fief distribution
**File:** `scripts.txt` (script: `give_center_to_lord`)

- Recipient relation gain: `10`
- Other lords range: `-5` (min) to `3` (max)

---

## Tweak 5g — Remove relation hit with fiefless/defeated vassals
**Files:** `scripts.txt`, `simple_triggers.txt`

- In `scripts.txt`: find `1224979098644774922 1224979098644774927 -1 2105 2` → change `-1`
- In `simple_triggers.txt`: find two instances with `-2` and `-1` → change to `0`

---

## Tweak 5h — Change relation penalty for rejecting vassalage
**Files:** `menus.txt`, `simple_triggers.txt`

- In `menus.txt`: find `mno_faction_reject` lines with `-3` and `-10` → change to `0`
- To fully disable: in `simple_triggers.txt` find trigger `32.000000` → replace content with `0.000000 0`

---

## Tweak 5i — Change village school relation frequency and amount
**File:** `simple_triggers.txt`

Find `26 2105 2 1224979098644774913 1` → change the `1` (relation amount)
The preceding `168.000000` controls frequency in hours (default = weekly).

---

## Tweak 5j — Change gift system values for enemy lord relations
**File:** `conversation.txt`

- Relation requirement cap: find in `dlga_lady_restore_relation_2` → change `0` to `100` to always allow
- Gift relation increases: three lines ending with `1`, `2`, `3`
- Gift prices: find in `dlga_lady_restore_relation_3` → values `1000`, `2000`, `3000`

---

## Tweak 5k — Modify quest and lord interaction relation points
**File:** `conversation.txt`

Search for code pairs:
- `936748722493063444` and `144115188075856143` — town/village quests (1–8 points each, 20 entries)
- `936748722493063443` and `144115188075855892` — lord interactions (-30 to +50, 83 entries)
