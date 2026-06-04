# Changelog — Immersive Pendor

Everything Immersive Pendor changes versus a stock **Prophesy of Pendor v3.9.5** install.

Where a change comes from a numbered community PoP tweak, the **(Tweak NN)** reference is given.
Features list **Access:** — how to actually reach the content in-game.

---

## [0.3]

### New systems & content

- **Arena practice fights are now once per day.** You can enter the arena training melee a single time per in-game day; after your bout the Arena Master tells you to rest and return on the morrow, and the option reopens at the next day's dawn. Keeps arena training from being an endless same-day XP/gold grind. Tournaments are unaffected. *Access:* talk to the Arena Master in any town and choose to join the melee.

### Changes

- **Random travelling events no longer spoil their outcomes.** Event choices used to list their rewards right in the option text (e.g. "(+3 renown, Sarleon +1)"). Those hints are gone — you now decide blind and live with the consequences.
- **Rewards are revealed afterward in the message log.** Once you make a choice, what you gained shows in the top-left log — now including gold and items, which previously arrived silently.
- **Companion-quest rewards are spelled out in the log too.** Finishing a companion's personal quest now reports the experience gained, any item received, and a note that the companion has grown more skilled — rewards that used to be applied silently.

---

## [0.2]

Bug fixes and balance tweaks for the 0.1 beta.

### Fixes

- **Random travelling events no longer quit to the main menu.** Previously, choosing *any* option in a random world-map event (the wandering Sarleon knight, the desert grave, the Mystmountain toll, and the rest) dropped you to the main menu instead of back to the map. All 30 events now close correctly and return you to your travels.

### Balance

- **Tournament victory prize reduced from 5000 to 2000 denars.** Winning a town tournament paid out an inflated 5000-denar prize; lowered to a more grounded 2000.

---

## [0.1] — Beta

First public beta. Built on Prophesy of Pendor v3.9.5.

---

### New companion quests

Multi-stage personal storylines drawn from each companion's backstory.
**Access (all of them):** recruit the companion and keep them in your party; after roughly a month of service a new line appears when you **talk to them** — that starts the quest. Each plays out through conversation plus a fight or two on the world map.

- **Sir Ansen — "The Falcon":** a bookish hopeful earns his knighthood through a deed of his own. *Access:* recruit Ansen; the arc develops as you speak with him (Sir Rayne plays a part in his dubbing).
- **Sir Rayne — "The Falcon's Right":** restore the lost Order of the Falcon, through a tournament and a contact in Rane's tavern. *Access:* recruit Rayne; talk to him.
- **Leslie — "The Quartermaster's Ledger":** a merchant's past catches up with the company. *Access:* recruit Leslie; the first stage needs a decent **party Trade skill**; talk to Leslie.
- **Diev Wodenssen — "Diev's Reckoning":** hunt the Mystmountain raid band that killed his family, north of Rane. *Access:* recruit Diev; after ~30 days, talk to him.
- **Alyssa — "The Serpent's Shadow":** her old Snake Cult order learns she lives and sends a death-cult band after her (near Janos, then Cez). *Access:* recruit Alyssa; after ~30 days, talk to her.
- **Sir Roland — "The Last Blow":** the Paladin of Astraea strikes at the Snake Cult that orphaned him, near Janos. *Access:* recruit Roland; after ~30 days, talk to him.

---

### New systems & content

- **Random travelling events** — 30 world-map encounters with choices and rewards (gold, items, troops, honor/renown/relation). *Access:* they fire on their own as you travel the world map (roughly once a game-week).
- **Trade agreements between kingdoms** — improve relations and trade between realms. *Access:* as a king, dispatch a companion emissary through your **Minister's** diplomacy options.
- **Petition your king** — urge your liege to declare war on, or make peace with, a rival realm (with a persuasion roll). *Access:* as a vassal, **talk to your king** — new options appear in his menu.
- **Return a fief to your king** — hand back a fief you hold. *Access:* as a vassal, **talk to your king / Minister**.
- **Release a captured king for peace** — ransom an enemy monarch in exchange for peace. *Access:* capture an enemy **king** in battle, then talk to him as your **prisoner**.
- **Feast attendance bonus** — +relation with a feast's host. *Access:* attend a lord's **feast** and greet the host (once per feast).
- **Village goods-delivery task** — carry local goods (grain, wine, fish, tools, wool) to a neighbouring village for pay. *Access:* ask a **village elder** "Do you have any tasks for me?"
- **Village NPCs that appear with the right building** (and help defend the village during raids):
  - **Sheriff** — *Access:* build the **Sheriff** improvement in a village you own. *(Tweaks: Village Sheriff NPC + Sheriff in battles + Sheriff garrison.)*
  - **Pendorian Cleric** — *Access:* build a **Church**. *(Cleric NPC + garrison.)*
  - **Monk** — *Access:* build a **Monastery**.
- **Troop-upgrade button** — upgrade troops directly from the party screen. *Access:* the **Upgrades** button on the party screen.
- **Enterprise report** — lists every town where you own an enterprise and its weekly net income. *Access:* **Camp → Reports → "View enterprise report."**
- **Compliment or insult lords** — flavor dialogue that nudges relation. *Access:* in any conversation with a lord. *(Tweak: Speak menu.)*

---

### Gameplay tweaks

**Character & progression**
- Higher XP gain rates *(Tweak 21f)* and more attribute/skill/weapon points per level.
- Removed luck decay *(Tweak 21b)*.
- Persuasion skill actually matters in dialogue checks *(Tweak 19b)*.
- Dust of Twilight reliably grants +2 Intelligence. *(DustTwilightAlwaysInt)*

**Companions**
- Companions no longer leave the party *(Tweak 16a)*.
- Companion complaints disabled *(Tweak 16c)*.
- Bodyguard companions stand at your side in scenes *(Tweak 16l)*.
- Proper equipment restored for mid/high-tier companions *(Tweak 16p)*.
- Recruit defeated unique-spawn leaders as companions *(Tweak 16n)*.

**Battles, sieges & arena**
- Participate in battles while wounded *(Tweak 10t)*.
- No ammunition reduction on sally-outs *(Tweak 9b)*; sally-out consciousness bug fixed *(Tweak 9c)*.
- More loot from battles *(Tweak 11a)*, ~100% loot share to the player *(Tweak 11a pt.2)*, and fixed loot ordering *(Tweak 11c)*.
- Town militia reinforce villages during bandit attacks. *(TrainPeasantsMilitiaInBattle)*
- Better player party-size formula *(Tweak 1w)*.
- Use your own gear in tournaments *(TournamentOwnGear)*; added a 5,000-denar bet *(TournamentBet5k)*; victory pays 5,000 *(TournamentWinGold)*; bonus XP per kill in tournaments *(TournamentKillXP)* and arena practice *(ArenaKillXP)*; boosted arena rewards *(ArenaRewardBuff)*.

**Lords, relations & prisoners**
- Attack any lord without restrictions *(Tweak 15c)*.
- Take equipment from captured lords *(Tweak 15g)*.
- Reduced lord escape chance *(Tweak 15d)*.
- Give money to poor friendly lords *(Tweak 15n)*.
- Stronger relation gains across the board *(RelationBoostScript)* and boosted relation/honor quest rewards *(Tweaks 5k + 14c)*.
- Prisoner capacity scales with party size and Prisoner Management *(Tweak 19c)*.
- Sell garrisoned prisoners to ransom brokers *(Tweak 12k)*.
- No honor loss for tolling/robbing caravans of factions you're already at war with. *(CaravanWarPenalty)*

**Kingdom, fiefs & economy**
- Faster, cheaper fief improvements *(Tweak 13v)*; lords build improvements more often *(Tweak 13x)*.
- Send troops to any owned walled fief remotely *(Tweak 13l)*.
- Manage a village's garrison directly *(Tweak 13q)*.
- Invest in villages for prosperity growth *(Tweak 12p)*.
- Better enterprise production rates *(Tweak 12d)*; merchant wealth scales with prosperity *(Tweak 12g)*; cheaper tavern wine *(Tweak 12i)*.
- Garrison sheriff/cleric refill cycle. *(GarrisonCycle)*

**Troops, recruitment & orders**
- Knighthood Order upgrade system overhaul *(Tweak 2u)*; KO chapters guaranteed at game start *(Tweak 2g)*; doubled KO rank points from quests *(KORankPointsDouble)*; KO promotion reward tracking fixed *(Tweak 2q)*.
- Custom Knighthood Order (CKO) equipping is cheaper and faster *(Tweak 3c)*.
- Sergeants receive half stats from default training *(Tweak 2t)*.
- Easier capture of unique spawns *(Tweak 1a)*.
- Faster garrison & lord-party training *(Tweak 17b)*.
- Village Blacksmith/School raise the chance of recruiting higher-tier volunteers. *(VillageBuildingRecruitTier)*

**Quests & world**
- Deliver Grain/Cattle quests reimburse the item cost *(QstReimburse)*; peasant-training quest can convert peasants to militia *(QstPeasantMilitia)*.
- Guildmaster auto-offers a new quest when you decline one *(Tweak 14f)*.
- Looters approach aggressively, fixing the stuck looter quest *(Tweak 14g)*.
- Brother Randalf reveals all bandit lairs *(Tweak 17x)*.
- The Inquisition is hostile to Singalians and outlaws *(Tweak 5b)*.
- The Ullr Vetr Manifest persists after Wolfbode is defeated *(Tweak 18k)*.

**Quality of life**
- Drastically reduced food consumption *(Tweak 17a)*.
- Fixed ambient sounds persisting after leaving taverns/arenas *(Tweak 21m)*.

---

*This is an early beta — expect rough edges. Bug reports and feedback are hugely appreciated. Start a new game; saves from unmodified PoP are not compatible.*

*Tweak numbers refer to the community Prophesy of Pendor tweak guides; named items in italics are Immersive Pendor's own additions.*
