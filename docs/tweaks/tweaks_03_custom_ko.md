# Tweaks 3 — Custom Knighthood Order (CKO)

Source: https://pop3.fandom.com/wiki/Tweaks (Template:Tweaks_3)

---

## Tweak 3a — Training session frequency
**File:** `simple_triggers.txt`

Default: every `18.000000` hours. Controls how often CKO knights and sergeants gain stats and skills.

---

## Tweak 3b — CKO sergeant training parity with knights
**File:** `simple_triggers.txt`

Change `30` to `0` and `32` to `30` to make sergeants train to the same level as knights.

---

## Tweak 3c — Equipping times and costs
**Files:** `scripts.txt`, `conversation.txt`

- Equipping multiplier: `100` (increase to shorten time)
- Cost multiplier: `1000` (decrease for cheaper upgrades)
- Minimum time: `1` day
- Minimum cost: `1000` denars

---

## Tweak 3d — Starting stats and equipment at KO level
**Files:** `troops.txt`, `conversation.txt`

Set CKO starting stats to KO level (30 STR, 21 AGI, 400 proficiencies) and disable training in return.

---

## Tweak 3e — Purchase CKO equipment like other KOs
**File:** `conversation.txt`

Replace `360287970189640027` and `360287970189640084` with `0` to remove the CKO purchase restriction.

---

## Tweak 3f — Grandmaster quest access for CKO
**File:** `conversation.txt`

Increment the 2nd line counter by 1 to enable the grandmaster quest for your CKO without cheatmenu.

---

## Tweak 3g — Sarleon and Ravenstern Armored Warhorses for CKO
**File:** `conversation.txt`

Add item IDs `288230376151711971` and `288230376151711970` to unlock both warhorses for your CKO when acquiring the respective legendary weapons.

---

## Tweak 3h — Unlock any item for CKO
**Files:** `triggers.txt`, `scripts.txt`

Item range: `288230376151711744` to `288230376151713316`.

---

## Tweak 3i — Calanon CKO unlock relation requirement
**File:** `conversation.txt`

Default relation threshold: `70`. Change to adjust how much Calanon relation is needed for CKO unlocks.

---

## Tweak 3j — CKO upgrade unit origins
**File:** `scripts.txt`

Change which units your CKO knights and sergeants upgrade from.  
Culture-specific troop constants: Sarleon `360287970189639779`, Ravenstern `360287970189639798`
