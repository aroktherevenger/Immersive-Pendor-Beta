# New Mechanics — Immersive Pendor

How the bigger new systems work in-game. What changed in each version is in the [changelog](CHANGELOG.md).

## Enlisting as a soldier (Freelancer)

You can join a lord's army as a common soldier, draw his pay and climb the ranks. Talk to a lord and choose **"I wish to take up arms in your service, my lord."** If he turns you down saying your name is unknown to him, you don't have enough renown yet. You can see your renown on the Character screen.

**Renown you need, by who you ask:**

| Who | Renown needed |
|---|---|
| A king (Ulric, Gregory IV, Kadan Bahadur Khan, Koningur Valdis, Marius Imperator) | 400 |
| A Duke (Sarleon, Ravenstern), Caliph (D'Shar), Earl (Fierdsvain) or Dux (Empire) | 300 |
| A Baron (Sarleon), Count (Ravenstern), Jarl (Fierdsvain), Legatus (Empire) or Bey (D'Shar); also Lord Hraven the Bold and Lord Ingvarr the Lame (Fierdsvain), Lord Brutus and Lord Decimus (Empire), and Kaivan, Faridar, Kalandar, Farhad and Jehangir Khan (D'Shar) | 200 |
| Any other lord of the five kingdoms (most plain "Lord ..." titles, and the other D'Shar Khans) | none |

**The offer only appears if:**
- you are not a vassal or ruler of any kingdom,
- you are not a member of a Knight Order,
- your relation with that lord is 0 or higher,
- you are not currently under a mercenary contract,
- you are not already enlisted with someone.

### Getting promoted

Promotion comes from **experience**. Every kind of XP counts: battles, sparring, and the 70 XP you get each week with your pay.

- **When it happens:** once a week, on payday. If the XP you have earned since you enlisted (or since your last promotion) has reached what your current rank needs, a menu says **"You have earned a promotion"**. You pick one of the two soldier types your current one upgrades to, and you get that soldier's equipment.
- **How much you still need:** click anywhere on the world map while enlisted to open your soldier menu. Its first line shows your rank and **"… XP to your next promotion"**. Higher ranks need more XP.
- **Sparring:** in the same menu, **"Spar with a soldier of your unit"** starts a one-on-one fight with a soldier type from your lord's army, once per day. Win and you gain XP equal to half of your opponent's level × 15 (at most 125 XP). Lose and you gain nothing; you can try again the next day.
- **Staying longer:** time alone does not promote you, but every week of service pays your wage plus 70 XP. Each promotion raises your weekly pay by 25 %. After 30 days of service the menu also lets you **muster out with honour** or **take your leave and keep your arms**.
- If your soldier type has no upgrade left, there are no further promotions.

## Trade agreements between kingdoms

Kingdoms now sign trade agreements with each other. You can see them in **Notes → Factions**: each kingdom's page says which kingdoms it has (or has no) trade agreement with.

**What an agreement does for both kingdoms**
- **Caravans only travel between kingdoms that are at peace and have a trade agreement.** With one, each kingdom's caravans can go to the other's towns to trade.
- Every time a caravan trades in a town, that town collects tariffs and gets two small chances of **+1 prosperity** (better chances when the town is short of goods). More caravans means richer, more prosperous **towns** on both sides.
- **Villages are not affected directly.** A village's prosperity comes from its own farmers taking goods to their market town, and that does not depend on trade agreements.
- Between the five AI kingdoms, trade partners also gain **+1 relation with each other every week** (up to 50), and AI kingdoms at peace without an agreement have a weekly chance to sign one (higher when they get along).
- **Declaring war cancels the agreement.** At the start of a new game, every main kingdom has an agreement with every kingdom it is at peace with.

**Can the player king make trade agreements?** Yes, once you rule your own kingdom:
1. Talk to your minister and choose **"I wish to dispatch an emissary."**, then pick the kingdom.
2. The first time, send your goodwill (**"That I wish to express my goodwill, as one monarch to another."**). The other ruler must recognise your kingdom first.
3. After that, while you are at peace with them and have no agreement yet, the option **"That we propose a trade agreement with him."** appears. Your emissary travels there and comes back with a yes or a no. If they accept, the agreement is signed.

Your own kingdom's agreements open the caravan routes like any other, so they help your **towns'** trade and prosperity. They do not raise your villages' base prosperity, and your kingdom does not get the weekly +1 relation or the automatic signings, which are only between the five AI kingdoms.

## Your wife can ride with you

Talk to your wife at home and pick **"Ride with me for a while."** She joins your party as a companion.
On the road, open the Party screen, select her and press Talk. You can look at her equipment or send her home.

- She brings armour but no weapon. Give her one before a fight.
- Like any hero in your party she draws a weekly wage. A Noldor wife costs about 134 denars a week at Leadership 0.
- If you are defeated she slips away and goes home. If she has no home yet, she stays with you.
- She can't ride with you while she is your minister. Making her minister sends her back to court.
- Household storage, feasts and outfit changes are only offered at home.
- Send her home before you remove the mod.

## Hire elite troops from a Master-at-Arms

In seven towns a Master-at-Arms stands by the castle gate, next to the gate guard. Talk to him there, or pick
**"Visit the Master-at-Arms."** in the town menu, then **"I am looking for fighting men."**

| Town | Troop | Town relation needed | Price a head |
|---|---|---|---|
| Javiksholm | Valdis Huscarl | 60 | 2,500 |
| Janos | Empire Centurion | 70 | 3,500 |
| Marleons | Marleons Heavy Cavalry | 50 | 2,500 |
| Poinsbruk | Iceguard Ranger | 60 | 2,500 |
| Singal | Singalian Temptress | 50 | 2,500 |
| Cez | Guardian Empire Knight | 60 | 3,000 |
| Ishkoman | D'Shar Djaha Archer | 50 | 2,000 |

- He has 2 men ready, or 3 once your relation with the town is 20 above the need (Janos: 15 above).
- Once a week he has new men ready: 7 days after his last batch, the stock is full again. He tells you how many days are left.
- Below the needed relation he tells you what you need. Win in the town's arena and do work for its guild master to raise it.
- Hire one, or as many as your gold, party room and his stock allow, in one go.
- He doesn't deal with you while you are at war with the town's owner, and he isn't there if you sneak in.
- The men draw the normal weekly wage for their troop.

## Autoresolve and your party's skills

When you choose **"Order your troops to attack without you."**, three party skills now change the result. The same rules apply when you join someone else's battle, in sieges, and in battles between AI parties on the map.

| Skill | In autoresolve |
|---|---|
| Tactics | Your party's Tactics minus the enemy's: each level makes your side hit 1% harder and take 1% less, up to 15%. The enemy's edge works the same way against you. |
| Surgery | Each level brings back 2% of your killed as wounded. They rejoin your party wounded, never past its size limit. |
| Prisoner Management | When you win, each level captures 1% more of the enemy's fallen (they show up as prisoners after the battle). |

- Everyone else uses the same rules: lords have Tactics, bandits usually none.
- Surgery only brings back men of your own party, never those of an allied lord fighting with you.
- What it does in an even fight (30 Sellswords against 30, measured in the engine): maxed Tactics against none takes you from about 1 win in 4 to about 1 in 2. Party Surgery 14 brings back about half of your fallen as wounded instead of a third.
- Leadership, First Aid, Looting, Engineer and Persuasion don't change autoresolve. Looting already works the same after both kinds of battle.
- When you fight the battle yourself, the skills work as before.
