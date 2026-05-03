# Tweaks 6 — Morale

Source: https://pop3.fandom.com/wiki/Tweaks (Template:Tweaks_6)

---

## Tweak 6a — Change morale penalty when out of food
**File:** `simple_triggers.txt`  
**Credit:** VonDegurechaff

Find `1 2 936748722493063451 -3 2133 2` → change `-3` to desired penalty (or `0` to disable)  
The `14.000000` before it controls frequency in hours.

---

## Tweak 6b — Change base party morale
**File:** `scripts.txt` (script: `get_player_party_morale_values -1`)  
**Credit:** TheMageLord

- Morale penalty per hero: `1` (set to `0` to remove)
- Leadership bonus when ruling: `18` (vanilla: `15`)
- Leadership bonus when not ruling: `15` (vanilla: `12`)
