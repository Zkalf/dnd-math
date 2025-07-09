Simulating Chromatic Orb (Spell level 2, on 3 targets, Elemental Adept, Empowered Spell +4).

For all strategies:

- if has pair -> skip reroll
- if condition triggered -> keep specific dice and reroll remaining
- else -> reroll all lowest dice

## Simple Strategies (sorted by condition damage ascending)

| Simulation name | Avg damage | Avg leaps | First leap % | Has pair % | Condition % | Reroll all % | Pair dmg | Condition dmg | Reroll dmg |
|---|---|---|---|---|---|---|---|---|---|
| Reroll none | 39.52 | 1.14 | 0.68 | 0.68 | 0.00 | 0.00 | 49.09 | 0.00 | 0.00 |
| Keep 2 and 7 and 8 | 45.89 | 1.49 | 0.89 | 0.68 | 0.05 | 0.28 | 49.07 | 37.16 | 39.56 |
| Keep 6 and 7 and 8 | 45.94 | 1.49 | 0.89 | 0.68 | 0.03 | 0.29 | 49.08 | 37.38 | 39.51 |
| Reroll all | 46.01 | 1.50 | 0.90 | 0.68 | 0.32 | 0.00 | 49.08 | 39.54 | 0.00 |
| Keep 2 | 46.04 | 1.54 | 0.92 | 0.68 | 0.23 | 0.09 | 49.08 | 39.64 | 39.55 |
| Keep 6 | 46.10 | 1.50 | 0.89 | 0.68 | 0.18 | 0.15 | 49.09 | 40.00 | 39.55 |
| Keep 2 or 7 or 8 | 46.15 | 1.49 | 0.89 | 0.68 | 0.32 | 0.01 | 49.08 | 40.00 | 39.46 |
| Keep 2 or 8 | 46.30 | 1.52 | 0.91 | 0.68 | 0.29 | 0.03 | 49.11 | 40.49 | 39.47 |
| Keep 6 or 7 or 8 | 46.32 | 1.45 | 0.87 | 0.68 | 0.31 | 0.01 | 49.09 | 40.53 | 39.60 |
| Keep 2 and 8 | 46.15 | 1.51 | 0.90 | 0.68 | 0.12 | 0.21 | 49.10 | 40.61 | 39.57 |
| Keep 7 | 46.26 | 1.49 | 0.89 | 0.68 | 0.18 | 0.15 | 49.07 | 41.07 | 39.46 |
| Keep 7 or 8 | 46.57 | 1.48 | 0.88 | 0.68 | 0.27 | 0.05 | 49.09 | 41.57 | 39.65 |
| Keep 7 and 8 | 46.16 | 1.49 | 0.89 | 0.68 | 0.08 | 0.24 | 49.07 | 41.69 | 39.47 |
| Keep 8 | 46.45 | 1.50 | 0.89 | 0.68 | 0.18 | 0.15 | 49.10 | 41.98 | 39.54 |

## Decision Tree Strategies (sorted by average damage ascending)

| Simulation name | Avg damage | Avg leaps | First leap % | Has pair % | Condition % | Reroll all % | Pair dmg | Condition dmg | Reroll dmg |
|---|---|---|---|---|---|---|---|---|---|
| Decision Tree1 | 46.33 | 1.50 | 0.90 | 0.68 | 0.29 | 0.03 | 49.08 | 40.64 | 39.51 |
| Decision Tree2 | 46.56 | 1.48 | 0.88 | 0.68 | 0.31 | 0.01 | 49.07 | 41.36 | 39.48 |
| Decision Tree5 | 46.57 | 1.48 | 0.88 | 0.68 | 0.31 | 0.01 | 49.08 | 41.36 | 39.50 |
| Decision Tree4 | 46.58 | 1.48 | 0.88 | 0.68 | 0.31 | 0.01 | 49.08 | 41.38 | 39.75 |
| Decision Tree3 | 46.59 | 1.48 | 0.88 | 0.68 | 0.32 | 0.00 | 49.09 | 41.32 | 0.00 |
