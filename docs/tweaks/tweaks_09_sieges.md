# Tweaks 9 — Sieges

Source: https://pop3.fandom.com/wiki/Tweaks (Template:Tweaks_9)

> **Format:** Each tweak includes the exact `search:` and `replace:` strings
> needed by the MCP server `apply_tweak` tool.

---

## Tweak 9b — Disable ammo reduction on sally-outs
**File:** `mission_templates.txt`

```
search:  1 1 3 936748722493063848 0 6
replace: 0
```

---

## Tweak 9c — Fix sally-out consciousness bug
**File:** `mission_templates.txt`

Remove this operation (counter must also decrease by 1, from 12→11):
```
search:  2147484654 1 0
replace: (delete the line)
```

---

## Tweak 9f — Change ammo refill rates in siege defense
**File:** `mission_templates.txt`

- AI refill: variable `144115188075856381` — change timer value `60` to desired seconds
- Player refill: variable `144115188075856383` — change timer value `180` to desired seconds

---

## Tweak 9g — Spread defending ranged reinforcements equally
**Files:** `scripts.txt`, `mission_templates.txt`

```
search:  33 3 1224979098644774914 1 3
replace: 30 2 1224979098644774914 1
```
(92 occurrences — use occurrence=0 to replace all)

---

## Tweak 9h — Remove garrison strength threshold for surrender
**Files:** `conversation.txt`, `scripts.txt`

Surrender ratios:
- `3` = leave unmolested
- `5` = surrender with honor

Remove garrison minimums: find `4000` and `2000` thresholds in surrender logic and delete those condition blocks.

Food supply defaults:
- Town: `50000` (100 days)
- Castle: `1500` (30 days)

---

## Tweak 9i — Besiege friendly fiefs
**File:** `menus.txt`

Honest approach relation penalty:
```
search:  (relation block near g_player_besiege_town honest path)
value:   -40
```
Barbaric approach:
```
value:   -30
```
Scripts involved: `set_player_relation_with_faction`, `diplomacy_start_war_between_kingdoms`, `player_leave_faction`

---

## Notes on tweaks 9a, 9d, 9e
These require counter adjustments alongside text changes — they must be done manually with a hex/text editor as the counter changes are positional, not searchable text substitutions. Document them separately when applying.
