# Tweaks 7 — Tournaments & Arena

Source: https://pop3.fandom.com/wiki/Tweaks (Template:Tweaks_7)

---

## Tweak 7a — Change Noldor Tournament rewards
**File:** `menus.txt`

Reward table (based on random roll 0–100):
- `<50` (50%): Qualis Gem `288230376151711870`
- `<60` (10%): 2x Large Pouch of Diamonds `288230376151711875`
- `<70` (10%): Lordly Noldor Rune Armor `288230376151712428`
- `<80` (10%): Masterwork Noldor Warsword `288230376151713090`
- `<90` (10%): Masterwork Noldor Composite Bow `288230376151712865`
- `<96` (6%): Champion Noldor Spirit Horse `288230376151711977`
- `<100` (4%): Champion Noldor Goldleaf Warhorse `288230376151711976`

To make it always give Qualis Gem: find `2 144115188075857282 20` → change `20` to `100`  
Item IDs = `288230376151711744 + entry number of item`

---

## Tweak 7b — Add Noldor Tournament start notification
**Files:** `strings.txt`, `simple_triggers.txt`

1. Increment line 2 of `strings.txt` by 1
2. Add string: `str_noldor_tournament_started The_Noldor_tournament_has_begun!`
3. In `simple_triggers.txt`: replace `648518346341351600 156 1` with the new code block
4. Adjust `216172782113788864` using formula: `216172782113783805 + line of str_noldor_tournament_started`
5. Increase second number after `24.000000` by 5 (130→135)

Requires: "Befriend the Noldor" quest complete + Noldor relation ≥30

---

## Tweak 7c — Change wins required for Mystical Rune Plate
**File:** `conversation.txt`

Find `dlga_start:noldor_give_armor_1 1087 0 4 30 2 144115188075857292 10` → change `10` to desired win count

---

## Tweak 7d — Change tournament frequency and duration
**File:** `simple_triggers.txt`

- Active tournament threshold (add new if fewer than X): `3`
- Chance of new tournament per 24h: `30`%
- Duration range: `12` to `14` days

---

## Tweak 7e — Change tournament participants and rounds
**File:** `scripts.txt`

- Total participants: `64` (change all instances across 6 scripts)
- In `sort_tournament_participant_troops`: use `63` (value - 1)
- Elimination factor: `2` (in `2133 2 1224979098644774913 72057594037927936`)

Scripts to update: `fill_tournament_participants_troop`, `get_num_tournament_participants`, `get_random_tournament_participant`, `add_tournament_participant`, `sort_tournament_participant_troops`, `remove_tournament_participants_randomly`

---

## Tweak 7f — Make tournament bets based on renown
**File:** `menus.txt`

Betting options: 100%, 50%, 20%, 10%, 5% of renown (1:1 ratio, max ~400,000 denars)

---

## Tweak 7g — Change tournament winnings
**File:** `menus.txt` (in `menu_town_tournament_won`)

- Renown: `20`
- Relation with hosting town: `3`
- Base denars: `2000`
- Experience: `250` (hard cap: 29,999)

---

## Tweak 7h — Earn renown from winning arena fights
**File:** `conversation.txt`

Find: `And_of_course_you_won_the_grand_prize_of_the_fights:_{reg10}_denars. 1633 3 1 3`  
Add after it: `936748722493063442 360287970189639680 10 1 3 936748722493063444 144115188075856143 1 1 3`
- `10` = renown per win
- `1` = relation gained per win

---

## Tweak 7i — Change arena fight monetary reward
**File:** `conversation.txt`

Two instances under `dlga_arena_training_melee_intro_reward` and `dlga_arena_training_melee_explain_reward`:  
Find `500 2133 2 72057594037927951 2000` → change `2000` (grand prize)

Two more instances under `dlga_arena_master_fight_result`:  
Find `2133 2 72057594037927946 2000` → change `2000`

---

## Tweak 7j — Choose starting weapon in arena fights
**Files:** `dialog_states.txt`, `variables.txt`, `conversation.txt`

1. Add two dialog states: `arena_master_weapon_type`, `arena_master_choose_weapon_type`
2. Add variable: `g_wp_tpe_active`
3. In `conversation.txt`: increment counter by 5, replace `dlga_arena_master_melee_talk:close_window` with 6 new lines

Weapon type codes: one-handed+shield (`34`), two-handed (`32`/`38`), bow+dagger (`36`), quarterstaff (`33`/`35`/`39`)
