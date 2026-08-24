# Changelog — Immersive Pendor

Everything Immersive Pendor changes versus a stock **Prophesy of Pendor v3.9.5** install.

Where a change comes from a numbered community PoP tweak, the **(Tweak NN)** reference is given.
Features list **Access:** — how to actually reach the content in-game.

---

## [0.43]

### Requirements & installation — read this first

**"The Complete Arsenal of Al-Aziz" is now required, and the install order has changed.** Al-Aziz is no longer a separate compatibility patch bolted on the side — its items, weapons and armours, its rune-forge dialogue and its gem-socketing menus are part of Immersive Pendor from this version on. Install these three in this exact order, overwriting when prompted:

1. Prophesy of Pendor v3.9.5 (clean)
2. The Complete Arsenal of Al-Aziz
3. Immersive Pendor 0.43 — **always last**

Installing 0.43 *without* Al-Aziz will break the game: our scripts and menus reference items that only Al-Aziz adds. Do not re-install Al-Aziz after step 3 either — it would overwrite Immersive Pendor's dialogue, menus and scripts; if you do, simply copy the 0.43 files over the top again. Do not copy `item_kinds1.txt` from Immersive Pendor either — it is deliberately not in the download, because Al-Aziz's copy from step 2 is the correct one and overwriting it would delete its 78 items. All credit for the Al-Aziz content belongs to its author; none of its files are redistributed here.

**Access:** Azziz's rune-forge shop and its gem-socketing menus, plus the new items appearing in loot and merchant stock.

**Start a new game.** Al-Aziz adds 78 items on top of the changes Immersive Pendor already makes. Saves from 0.42 or earlier will not behave correctly.

### Balance

- **Lord relation rewards rebalanced.** Gains in standing with lords were being boosted twice over by two separate tweaks that stacked on each other, ending up at roughly three times the base game instead of the intended fifty percent more. There is now a single rule: every gain is base game +50%, the same rule honour already used. In practice the dialogue rewards you actually see are unchanged — it was the hidden second multiplier that went away — with two exceptions. Backing a pretender now grants a large boost rather than slamming your standing to the maximum, and the smallest routine lord tasks (deliver a message, collect taxes, raise troops, hunt a fugitive, scout waypoints, meet a spy) go from +2 back to +1. Relation *penalties* are unchanged and remain softer than the base game.

### Quality of life

- **Faction relation messages now tell you where you stand.** They used to report only the swing — *"The Noldor think better of you (+5)"* — so keeping track of your actual standing meant doing it by hand. They now report the resulting figure as well: *"The Noldor think better of you (+5). Now 35."* Handy everywhere, and especially for the Noldor, where the thresholds genuinely gate things. **Access:** the message that appears whenever your standing with a faction changes.

### Fixes

- **Companion quest journals no longer show unrelated text.** Accepting Alyssa's, Diev's or Sir Roland's personal quest put a stray line in the quest notes — usually a faction name such as "The Kingdom of Ravenstern" — where the description of your task should have been. This was left over from the 0.42 quest-numbering repair, which made the three quests appear in the journal but never gave them their opening entry. All three now open with a proper description of what you have been asked to do. Only Alyssa's was reported; Diev's and Sir Roland's carried the same fault and were fixed alongside it. **Access:** the quest notes screen, right after accepting any of the three.

---

## [0.42]

### Fixes
- **Talking to a captured or hostile lord no longer jumps your relationship with him to the maximum.** A stray reference in the lord-comment dialogue was slamming your standing with such a lord to 100 whenever he remarked on your relationship — including the scornful remarks from cruel or ill-tempered lords, which are meant to *cost* you standing. Those exchanges now shift your relationship as intended.
- **Alyssa's companion quest, “The Serpent's Shadow,” now shows its journal description, and the tavern Order-rivalry quest starts correctly.** A numbering slip in the companion questlines had shifted several quest hooks by one, so Alyssa's quest tracked with no description telling you what to do, and accepting the tavern rivalry quest mistakenly started the freelancer enlistment quest instead. Every companion-arc quest (Ansen, Rayne, Leslie, Diev, Alyssa, Roland, and the tavern rivalry) now points to the right quest.
- **Fixed an endless stream of Snowcat raider parties spawning near Rane during Ansen's questline.** The same numbering slip meant the game never registered that it had already spawned the trial raiders, so it kept spawning fresh ones every game-hour — and defeating them never advanced the quest. Now a single raider party appears for the trial, and defeating it moves the quest forward. *(Any surplus parties already spawned into an existing save will remain until you clear them; a new game starts clean.)*
- *Internal: restored consistent line endings in several data files; no gameplay change.*

### Changes
- **Defeated unique enemy commanders can no longer be pressed into your service as companions.** When you captured one of the game's unique “named” spawn leaders, a dialogue option let you recruit them into your own company; that option has been removed. Unique spawn leaders can still be ransomed, released on their word of honour, or executed.

---

## [0.41]

---

## [0.40]

### New systems & content
- **Companions can now be sent to the Noldor for paid training, using pouches of diamonds.** Once your standing with the Noldor is high enough, you can offer a companion diamonds to fund a stint of training in their halls. A Small Pouch grants a solid burst of experience and a flat boost to every weapon skill; a Medium Pouch grants substantially more of both plus a point each of Strength and Dexterity; a Large Pouch grants the most of all, plus a point each of Strength, Dexterity, Intelligence, and Charisma. The pouches must be sitting in your inventory before the option appears. *Access:* speak to a companion and choose to discuss their training; requires Noldor relation of at least 15 and the relevant pouch of diamonds on hand. *(Tweak by Dimasik & Dalion.)*
- **Ranged troops that run dry can now be reassigned to another division instead of standing idle.** Archers, crossbowmen, and arquebusiers who empty their ammunition in battle can be automatically shifted into a division of your choosing — infantry, cavalry, wherever you need the extra bodies — rather than lingering uselessly at the back of the field with nothing left to shoot. *Access:* toggle "Reassign archers with empty ammo to division" in the mod options menu. *(Tweak by Vetrogor & Caba'drin.)*

### Balance
- **Reduced the arena's champion-tier victory reward** (renown, gold, and experience all cut roughly in half) **and lowered the maximum tournament bet** from 5000 to 4000 denars.
- **Attribute points per level reverted to 1 (was 2).** Leveling up now grants a single attribute point (Strength, Agility, Intelligence, or Charisma) per level, matching the original pace.

### Fixes
- **Enlisting under a lord no longer inflates his army size or leaves you with a mystery horde.** A bug in how post-battle prisoners and loot were handled while serving as a freelancer meant a leftover batch of troops from an earlier fight kept getting folded into whichever ally you had just fought beside, making his displayed strength balloon to two or three times its real size — then vanish just as suddenly once he was beaten, with the loss screen sometimes showing the enemy holding hundreds of prisoners who were never really there. Fixed at the source, so a lord's numbers now always reflect his actual troops.
- **As a freelancer, prisoners and loot after a battle now go to your commander, not you.** Since you're serving under someone else's command, you no longer see the prisoner-capture or loot screens after a fight while enlisted.
- **Fixed the Diev and Alyssa companion quests not appearing in your journal after accepting them.** A bookkeeping error meant these two quests (and a few related ones) never got properly recorded, so they were silently missing from your quest log even though you had agreed to help. They now appear and track correctly like every other companion quest.
- *Internal: corrected file-encoding line endings in two data files; no gameplay change.*

---

## [0.39]

### New systems & content
- **Forty-five unique travelling encounters, each happening only once per savegame.** As you ride across the map you will stumble across all manner of people and situations — a Noldor wanderer at a forest edge, a freshly-looted battlefield, Fierdsvain skalds, Snake Cult prisoners, dying soldiers, inquisition hunts, D'Shar traders, ancient High-Kingdom ruins, and much more. Fifteen new encounters have been added this version, bringing the total to forty-five. Each one is drawn without repetition, so across any single playthrough every encounter fires at most once — and every new game deals you a different hand. *Access:* events occur automatically while travelling the campaign map, roughly once every week of game time.
- **Every encounter offers three meaningfully different choices.** Each of the forty-five events now presents at least three options, each with a genuinely distinct trade-off — so you are never choosing between two versions of the same thing. Whether you pay coin, spend time, risk your honour, pick a fight, or ride on, the outcomes differ in kind, not just in degree.
- **Three more travelling encounters can be settled with a field duel — twelve in total now.** On top of the original five, a young Knight of the Lion who wants to test his arm, a Knight of Eventide willing to cross blades in earnest, a Mettenheim deserter who fancies himself a swordsman, and a brigand holding the road can all be challenged to single combat. Win and you walk away with honour and experience; lose and you may part with gold or take a blow to your reputation. *Access:* the duel option appears as one of the choices when each encounter fires.
- **Your chance of winning a wager now depends on your character's skills.** The D'Shar Windrider horse-race and the Fierdsvain bard's flyting both used to be straight coin-flips. Now your odds scale with your abilities: riding skill raises your win chance in the race (starting at 40%, rising 4 percentage points per skill level, capping at 85%), and Charisma raises it in the flyting (30% base, +2 per point, same 85% cap). A capable rider or a silver-tongued general will win more often than not; a lumbering warrior had better think twice before laying money down.

### Changes
- **Enlisting with a lord now depends on your renown.** Any lord will still hear your offer to take up arms in his service, but the greater the lord, the greater the name he expects of a recruit. A realm's lesser lords take any willing fighter; its middle nobles want 200 renown, its great nobles 300, and its reigning monarch 400. Approach a lord above your standing and he will send you off to win a reputation first. *Access:* speak to any kingdom lord and choose "I wish to take up arms in your service."
- **Freelancer sparring now happens in the open field, with real weapons.** When you spar with one of your unit's soldiers while enlisted, the bout now takes place on an open training field instead of the town arena, and both of you fight in your own equipment rather than blunted practice arms. It is still a knockout match — nobody is killed — and is still limited to once a day. *Access:* while enlisted, open **"What do you need to do, soldier?"** and choose **"Spar with a soldier of your unit."**

### Balance
- **Freelancer spar experience cut by half.** Winning a daily spar now grants half the experience it did before, so training between battles no longer levels you up unusually fast.

### Fixes
- **Losing your commander's army no longer leaves you stranded in service.** If the lord you are enlisted under has his party destroyed, your service now ends cleanly and at once — you are released as a free soldier with no penalty, instead of staying bound to a commander who no longer has an army (which also produced a stream of error messages).
- **Losing a sparring match or field duel no longer freezes the result screen.** When you lost a training bout or a travelling-encounter duel, clicking "Continue" on the result screen did nothing and trapped you there. The screen now returns you to the map correctly whether you win or lose.
- **Completing freelancer service no longer leaves a stale quest entry in your journal.** Ending your enlistment — whether by honourable discharge, desertion, or your lord's army being destroyed — now clears the quest from your journal and its notes completely, instead of leaving a concluded entry sitting there permanently.

---

## [0.38]

### New systems & content
- **Freelancer pay now rises with rank.** Each promotion increases your weekly wage by 25%, so climbing the ranks as a soldier is properly rewarded.
- **New achievement — "Seasoned Sellsword".** Serve a cumulative total of 90 days as an enlisted freelancer (counted across all your enlistments, kept if you leave and sign on again) to earn this achievement and a permanent **+1 Strength**. It unlocks with the usual achievement notice and gets its own entry on your achievements screen. *Access:* enlist with any kingdom lord and keep serving — the reward is granted automatically once your total service reaches 90 days.

### Changes
- **Honor you earn is increased by 50%.** Every honor *gain* — from quests, conduct in battle, freeing prisoners, and the like — is now boosted by half again (×1.5). Honor losses are unchanged.

### Fixes
- **Releasing Noldor prisoners no longer grants a broken, astronomical amount of honor.** Freeing captured Noldor — and a couple of other reward conversations, including tournament preparations — used a faulty honor reward that handed out a meaningless, enormous number. You now correctly receive a modest amount of honor for each Noldor Noble you free, as intended.

---

## [0.37]

### New systems & content

- **Freelancer — train with your own unit between battles.** While enlisted in a lord's warband, you can now spar with one of your comrades-in-arms. Choose which of your unit's soldiers to face and meet them one-on-one in the practice ring with blunted arms; win the bout and you come away with a little hard-earned experience. You can spar once a day, win or lose — enough to keep your blade sharp without turning it into a grind.
  - *Access:* while enlisted, open the **"What do you need to do, soldier?"** menu and choose **"Spar with a soldier of your unit"**, then pick your opponent.

### Changes

- **Freelancer — your rank is now remembered for each kingdom.** Leaving a lord's service and signing on again used to send you back to the lowest rank every time, even with the same realm. Now your hard-won rank is kept per kingdom: rejoin a lord of a realm you have served before and you resume where you left off, while taking service with a new kingdom still starts you fresh as one of their recruits.

---

## [0.36]

### New systems & content

- **You can now switch tournaments between your own gear and standard Prophesy of Pendor rules.** Immersive Pendor has you fight tournaments in your own equipment. If you would rather have the classic experience, a new Camp-menu toggle switches tournaments back to the **standard Prophesy of Pendor setup** — the standardised weapons and team-coloured tunics of unmodified Pendor — and back to your own gear again whenever you like. The choice is remembered per character and takes effect at your next tournament.
  - *Access:* from the **Camp** menu, click the **"Tournaments: …"** line (just below "POP options") to switch between the two styles.

---

## [0.35]

### New systems & content
- **Freelancer — enlist and serve in a lord's warband.** You can now take up arms as a common soldier under any of the five kingdoms. You enlist as that culture's basic recruit, are issued their equipment, and follow your commander across the campaign map — fighting at his side in both field battles and sieges. Earn weekly wages, rise through the kingdom's regular troop tree with promotions of your own choosing, and leave honourably or desert when you have had enough.
  - *Access:* speak to any kingdom lord and choose **"I wish to take up arms in your service."** While enlisted, manage your service (request a discharge, or desert) from the **Camp** menu.
  - *Beta note:* this is a brand-new system — feedback is welcome, especially on which side you fight on during **sieges**. A new save is recommended.

### Changes

- **Troops across every major faction have been re-equipped and rebalanced.** Soldiers of Sarleon, Ravenstern, the Empire, the D'Shar, the Fierdsvain, and Pendor's own forces — along with mercenaries, nobles, squires, knights, and many unique troops — have had their equipment loadouts reworked, with adjusted attributes, weapon proficiencies, and skills across a wide range of them. Close to two hundred troop types are affected, so field battles, garrisons, and the recruits you raise feel noticeably different to fight beside and against. Your companions' own loadouts are left as they were, and existing saves load normally — the changes take effect as troops are spawned.
- **Several troop upgrade paths have been revised.** Some faction lines now branch differently as they advance: a few gain a second upgrade choice (Sarleon and Ravenstern noblemen, Fierdsvain noblewomen, Empire militia, Pendor swordsmen, D'Shar conscripts), others are streamlined to a single path, and the regional squire lines were reorganised.

---

## [0.34]

### Changes
- **Travelling encounters reworked so every choice matters.**
  - Encounters that involve sharing your camp, keeping a vigil, tending a wounded knight, or escorting a caravan now **cost in-game time**, to match what you are actually doing.
  - New outcomes where the story supports them — **take a captive for ransom** (bind a shipwrecked Vanskerry raider) or **hire a wandering sell-sword** (a masterless Singalian heading north for work).
  - Empty courtesies — saluting, bowing, swapping idle news — no longer hand out honor or renown for free. Only choices with a real cost or consequence are rewarded.
  - *Access:* these fire on their own as you travel the world map.

### Balance
- **Encounter rewards rebalanced.** Coin offered or demanded is now a meaningful sum, not a token handful of denars — and every reward is *earned*, paid for in gold, time, honor, or by passing up a bigger prize. Greedy or dishonourable choices carry an honor cost; charity, duty, and respect for the fallen are what earn honor.

### Fixes
- Reworked several encounters whose options did not make sense, or where one choice was strictly better than the rest, so each option now stands on its own.

---

## [0.33]

### Fixes

- **Pre-battle deployment now keeps your troops on their assigned positions.** When you take up a prepared battle plan, your divisions — cavalry included — hold the spots you set for them instead of charging off or snapping back into the default formation. Each division then responds to your orders independently, so the troops you haven't committed yet stay where you placed them. Choosing to charge in as usual is unchanged and uses normal formations. *Access:* Camp → "Plan your battle formations", then pick a plan when you charge into a field battle.

---

## [0.32]

### New systems & content

- **You can now plan where your troops form up before a battle.** From the Camp menu, open "Plan your battle formations" and set where each division stands relative to you — infantry in front, cavalry to your left, companions on your right, archers behind, and so on. Then, when you charge into a field battle, your captains ask how to form up: **charge in as usual**, or **take up one of your prepared battle plans** — and your troops form on that arrangement around you and hold it. The number of battle plans you can keep grows with your **Tactics** skill: 1 plan at Tactics 2, 2 at Tactics 5, 3 at Tactics 10. *Access:* Camp → "Plan your battle formations" to build your plans; then pick one from the menu that appears when you charge the enemy.
- **Knighthood-order knights in taverns will now hire you against their rivals.** When you meet a wandering Order knight in a town tavern, you can offer to drive off a rival Order that has been harassing them. Accept, and that rival's patrol appears nearby; defeat it and the deed is done on the spot, no need to report back. Earns you standing and favor with the knight's Order, a little honor, and experience. Each Order will only ask again after some time has passed. *Access:* talk to a knighthood-order knight in any town tavern and choose "Is there a rival Order you'd have me drive off?"

---

## [0.31]

### New systems & content

- **You're now told when a companion is ready to open up.** When a companion you've kept in your party becomes ready to begin their personal quest, a message appears letting you know they have something on their mind — so you no longer have to guess when their month-of-service timer is up. *Access:* keep the companion in your party; watch for the notice, then talk to them.

### Fixes

- **The arena's once-a-day limit is now tracked per town.** Previously, fighting the arena melee in one town locked the arena everywhere for the rest of the day. Each town now keeps its own daily count, so a bout in Rane no longer stops you fighting in Senderfall the same day. (Refines the 0.3 once-per-day arena.)
- **Sarleon's villages no longer start under the wrong faction.** With the "villages aren't auto-granted along with their town" tweak active, Balanli and Azgad began a new game owned by Ravenstern lords until Sarleon next changed hands. They now start correctly under Sarleon. *(Tweak 13f.)*

### Balance

- **Arena practice champion prize reduced from 5000 to 2000 denars.** Winning the arena training melee paid an inflated 5000-denar grand prize; lowered to 2000. The lower placing prizes are unchanged.
- **Tournament victory prize raised from 2000 to 4000 denars.** The 0.2 reduction to 2000 was too steep; settled at 4000.

---

## [0.3]

### New systems & content

- **Arena practice fights are now once per day.** You can enter the arena training melee a single time per in-game day; after your bout the Arena Master tells you to rest and return on the morrow, and the option reopens at the next day's dawn. Keeps arena training from being an endless same-day XP/gold grind. Tournaments are unaffected. *Access:* talk to the Arena Master in any town and choose to join the melee.

### Changes

- **Random travelling events no longer spoil their outcomes.** Event choices used to list their rewards right in the option text (e.g. "(+3 renown, Sarleon +1)"). Those hints are gone — you now decide blind and live with the consequences.
- **Rewards are revealed afterward in the message log.** Once you make a choice, what you gained shows in the top-left log — now including gold and items, which previously arrived silently.
- **Companion-quest rewards are spelled out in the log too.** Finishing a companion's personal quest now reports the experience gained, any item received, and a note that the companion has grown more skilled — rewards that used to be applied silently.
- **Honor and faction-standing changes now show the amount.** Messages used to just say "You gain honor." or "{Faction} relation increased." — now they read "You gain 2 honor." and "Kingdom of Sarleon thinks better of you (+1)", so every reward states exactly how much (this applies game-wide, not just to the new content).
- **Travelling events resolve cleanly on the spot.** Options that sounded like they sent you off on an untracked errand (escort the merchant, take the girl to town, send the prisoner to the Inquisition) are reworded so the outcome clearly happens then and there — no more "we'll do X" with nothing to follow up on.

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
