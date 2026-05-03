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
