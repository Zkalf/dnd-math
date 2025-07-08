import random

def roll_damage_dice(dice, sides, elemental_adept):
    rolls = [random.randint(1, sides) for _ in range(dice)]
    if elemental_adept:
        rolls = [2 if roll == 1 else roll for roll in rolls]
    return rolls

def check_for_pair(dice_rolls):
    return len(set(dice_rolls)) < len(dice_rolls)

def reroll_damage_dice(elemental_adept):
    new_roll = random.randint(1, 8)
    if elemental_adept and new_roll == 1:
        new_roll = 2
    return new_roll

def empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values):
    if check_for_pair(dice_rolls):
        return dice_rolls
    if keep_condition:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v not in keep_values][:charisma_modifier]
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def empowered_reroll_strategy_none(dice_rolls, charisma_modifier, elemental_adept):
    return dice_rolls

def empowered_reroll_strategy_all(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def empowered_reroll_strategy_keep_2(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  2 in dice_rolls, [2])

def empowered_reroll_strategy_keep_6(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 6 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  6 in dice_rolls, [6])

def empowered_reroll_strategy_keep_7(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 7 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  7 in dice_rolls, [7])

def empowered_reroll_strategy_keep_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 8 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  8 in dice_rolls, [8])

def empowered_reroll_strategy_keep_2_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2 and 8 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  2 in dice_rolls and 8 in dice_rolls, [2, 8])

def empowered_reroll_strategy_keep_2_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2 or 8 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  2 in dice_rolls or 8 in dice_rolls, [2, 8])

def empowered_reroll_strategy_keep_7_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 7 and 8 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  7 in dice_rolls and 8 in dice_rolls, [7, 8])

def empowered_reroll_strategy_keep_7_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 7 or 8 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  7 in dice_rolls or 8 in dice_rolls, [7, 8])

def empowered_reroll_strategy_keep_2_and_7_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2, 7 and 8 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  2 in dice_rolls and 7 in dice_rolls and 8 in dice_rolls, [2, 7, 8])

def empowered_reroll_strategy_keep_2_or_7_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2, 7 or 8 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  2 in dice_rolls or 7 in dice_rolls or 8 in dice_rolls, [2, 7, 8])

def empowered_reroll_strategy_keep_6_and_7_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 6, 7 and 8 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  6 in dice_rolls and 7 in dice_rolls and 8 in dice_rolls, [6, 7, 8])

def empowered_reroll_strategy_keep_6_or_7_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 6, 7 or 8 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  6 in dice_rolls or 7 in dice_rolls or 8 in dice_rolls, [6, 7, 8])

def empowered_reroll_strategy_keep_5_and_6_and_7_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 5, 6, 7 and 8 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  5 in dice_rolls and 6 in dice_rolls and 7 in dice_rolls and 8 in dice_rolls, [5, 6, 7, 8])

def empowered_reroll_strategy_keep_5_or_6_or_7_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 5, 6, 7 or 8 then reroll remaining dice, else reroll all
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, 
                                  5 in dice_rolls or 6 in dice_rolls or 7 in dice_rolls or 8 in dice_rolls, [5, 6, 7, 8])

def empowered_reroll_strategy_keep_decision_tree1(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    # if dice_rolls have 7 and 8 then reroll remaining dice
    if 7 in dice_rolls and 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 7 and v != 8][:charisma_modifier]
    # elif dice_rolls have 2 and 8 then reroll remaining dice
    elif 2 in dice_rolls and 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 2 and v != 8][:charisma_modifier]
    # elif dice_rolls have 8 then reroll remaining dice
    elif 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 8][:charisma_modifier]
    # elif dice_rolls have 2 then reroll remaining dice
    elif 2 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 2][:charisma_modifier]
    # else reroll all
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def empowered_reroll_strategy_keep_decision_tree2(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    # if dice_rolls have 7 or 8 then reroll remaining dice
    if 7 in dice_rolls or 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 7 and v != 8][:charisma_modifier]
    # elif dice_rolls have 2 then reroll remaining dice
    elif 2 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 2][:charisma_modifier]
    # else reroll all
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def chromatic_orb(spell_level, targets, elemental_adept, charisma_modifier, reroll_strategy):
    dice = 3 + (spell_level - 1)
    sides = 8

    initial_roll = roll_damage_dice(dice, sides, elemental_adept)
    if charisma_modifier > 0 and reroll_strategy:
        initial_roll = reroll_strategy(initial_roll, charisma_modifier, elemental_adept)
    total_damage = sum(initial_roll)

    leaps = 0
    first_leap_triggered = 0
    if check_for_pair(initial_roll) and targets > 1:
        first_leap_triggered = 1
        max_leaps = spell_level

        for _ in range(min(max_leaps, targets - 1)):
            leaps += 1
            additional_roll = roll_damage_dice(dice, sides, elemental_adept)
            total_damage += sum(additional_roll)

            if not check_for_pair(additional_roll):
                break

    return total_damage, leaps, first_leap_triggered

def simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, reroll_strategy, label):
    print(f"Running {simulations} simulation on {label}")
    damages_list = []
    leaps_list = []
    first_leap_list = []
    for _ in range(simulations):
        damage, leaps, first_leap_triggered = chromatic_orb(spell_level, targets, elemental_adept, charisma_modifier, reroll_strategy)
        damages_list.append(damage)
        leaps_list.append(leaps)
        first_leap_list.append(first_leap_triggered)
    avg_damage = sum(damages_list) / simulations
    avg_leaps = sum(leaps_list) / simulations
    first_leap = sum(first_leap_list) / simulations
    return (label, avg_damage, avg_leaps, first_leap)

def main():
    simulations = 100000
    spell_level = 2
    targets = spell_level + 1
    elemental_adept = True
    charisma_modifier = 4
    print(f"\nSimulating {simulations} Chromatic Orb (Spell level {spell_level}, {targets} targets, {'Elemental Adept' if elemental_adept else 'no Elemental Adept'}, Empowered Spell +{charisma_modifier}):\n")
    results = []
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_none, "Reroll none"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_all, "Reroll all"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_2, "Keep 2"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_6, "Keep 6"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_7, "Keep 7"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_8, "Keep 8"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_2_and_8, "Keep 2 and 8"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_2_or_8, "Keep 2 or 8"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_7_and_8, "Keep 7 and 8"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_7_or_8, "Keep 7 or 8"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_2_and_7_and_8, "Keep 2 and 7 and 8"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_2_or_7_or_8, "Keep 2 or 7 or 8"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_6_and_7_and_8, "Keep 6 and 7 and 8"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_6_or_7_or_8, "Keep 6 or 7 or 8"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_5_and_6_and_7_and_8, "Keep 5 and 6 and 7 and 8"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_5_or_6_or_7_or_8, "Keep 5 or 6 or 7 or 8"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_decision_tree1, "Decision Tree1"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_decision_tree2, "Decision Tree2"))
    
    # Sort results by avg_damage ascending
    results.sort(key=lambda x: x[1], reverse=False)
    # Write markdown table to file
    with open("results.md", "w", encoding="utf-8") as f:
        f.write(f"Simulating Chromatic Orb (Spell level {spell_level}, on {targets} targets, {'Elemental Adept' if elemental_adept else 'no Elemental Adept'}, Empowered Spell +{charisma_modifier}).\n\n")
        f.write("For all strategies:\n\n")
        f.write("- if no pair\n")
        f.write("- after strategy reroll remaining\n")
        f.write("- else reroll all\n\n")
        f.write("| Simulation name | Avg damage | Avg leaps | First leap chance |\n")
        f.write("|---|---|---|---|\n")
        for label, avg_damage, avg_leaps, first_leap in results:
            f.write(f"| {label} | {avg_damage:.2f} | {avg_leaps:.2f} | {first_leap:.2f} |\n")

    print("\nResults saved to results.md\n")

if __name__ == "__main__":
    main()