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
