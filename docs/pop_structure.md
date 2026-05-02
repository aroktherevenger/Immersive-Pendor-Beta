# Prophesy of Pendor — Internal Structure Reference

## Key Text Files (in your PoP install folder)
These are the compiled outputs that M&B actually reads at runtime.

| File | Contents |
|---|---|
| `troops.txt` | All troop definitions (stats, equipment, faction) |
| `items.txt` | All item definitions (weapons, armor, goods) |
| `parties.txt` | Named party instances on the world map |
| `party_templates.txt` | Party composition templates for spawning |
| `quests.txt` | Quest metadata |
| `dialogs.txt` | All NPC dialogue trees |
| `scenes.txt` | Scene/location metadata |
| `factions.txt` | Faction relations and flags |
| `skills.txt` | Skill metadata |
| `map_icons.txt` | World map icons |
| `menus.txt` | Game menu definitions |
| `mission_templates.txt` | Battle/encounter mission setups |
| `triggers.txt` | Global game event triggers |
| `simple_triggers.txt` | Lightweight periodic triggers |
| `scripts.txt` | Reusable script functions |
| `strings.txt` | Localisation strings |

## PoP-Specific IDs
These are the key faction/troop ID slots that PoP reserves.
Do NOT reuse these IDs for new content.

### Factions (factions.txt order)
0. No faction
1. Commoners
2. Outlaws
3. Kingdom of Pendor
4. Fierdsvain
5. Empire
6. D'Shar Principalities
7. Ravenstern
8. Barclay (minor kingdom)
9. Snake Cult
10. Noldor
11. Jatu Horde
12. Heretics

### Important Troop Ranges
- Slots 0–99: Core player/hero troops
- Slots 100–299: Kingdom of Pendor troops
- Slots 300–499: Fierdsvain troops
- Slots 500–699: Empire troops
- Slots 700–899: D'Shar troops
- Slots 900–1099: Ravenstern troops
- Slots 1100–1299: Snake Cult troops
- Slots 1300–1499: Noldor troops
- Slots 1500–1699: Jatu troops
- Slots 1700+: Mercenaries, bandits, misc

**Safe zone for this mod:** Start new troops at slot 2000+.

## Python Module System Overview
The module system compiles `.py` files into the above `.txt` files.
Each `module_*.py` exports a list named after the module (e.g. `troops`, `items`).
The `process_*.py` scripts read these lists and write the text file format.

## Common Pitfalls
1. **ID shifting**: Never insert into the middle of a list. Always append.
2. **Save compatibility**: Changing a troop/item that exists in a save will corrupt it.
3. **Python 2 only**: The module system requires Python 2.7 — no Python 3.
4. **Mesh names**: Must exactly match mesh names in the `.brf` resource files.
5. **Face keys**: These are 64-bit hex values — use existing ones as templates.
