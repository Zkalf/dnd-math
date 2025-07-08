import random

def fake_initial_roll_dice(number_of_dice, sides, elemental_adept):
    rolls = [8, 7, 6, 2] # Example fixed rolls for testing purposes
    if elemental_adept:
        rolls = [2 if roll == 1 else roll for roll in rolls]
    return rolls

def roll_dice(number_of_dice, sides, elemental_adept):
    rolls = [random.randint(1, sides) for _ in range(number_of_dice)]
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

def empowered_reroll_strategy_nothing(dice_rolls, charisma_modifier, elemental_adept):
    return dice_rolls

def empowered_reroll_strategy_all(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def empowered_reroll_strategy_all_except_2(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 2][:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def empowered_reroll_strategy_below_average(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    reroll_indices = [i for i, v in enumerate(dice_rolls) if v <= 4][:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def empowered_reroll_strategy_below_average_except_2(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    reroll_indices = [i for i, v in enumerate(dice_rolls) if 3 <= v <= 4][:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def empowered_reroll_strategy_never_high(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    if all(v >= 5 for v in dice_rolls):
        return dice_rolls
    reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def empowered_reroll_strategy_keep_8s(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 8][:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def empowered_reroll_strategy_keep_2s_and_8s(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    reroll_indices = [i for i, v in enumerate(dice_rolls) if (v != 2 and v !=8)][:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def empowered_reroll_strategy_keep_7s_and_8s(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    reroll_indices = [i for i, v in enumerate(dice_rolls) if (v != 7 and v != 8)][:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def empowered_reroll_strategy_keep_6s_7s_and_8s(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    reroll_indices = [i for i, v in enumerate(dice_rolls) if (v != 6 and v != 7 and v != 8)][:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def empowered_reroll_strategy_keep_decision_tree(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls
    # If dice_rolls have 8 and 7 then reroll remaining 2 dice
    if 8 in dice_rolls and 7 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 8 and v != 7][:charisma_modifier]
    # elif dice_rolls have 8 and 2 then reroll remaining 2 dice
    elif 8 in dice_rolls and 2 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 8 and v != 2][:charisma_modifier]
    # elif dice_rolls have 8 then reroll remaining 3 dice
    elif 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 8][:charisma_modifier]
    # elif dice_rolls have 2 then reroll remaining 3 dice
    elif 2 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 2][:charisma_modifier]
    # else reroll all
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls

def chromatic_orb(spell_level, number_of_targets, elemental_adept, charisma_modifier, reroll_strategy):
    number_of_damage_dice = 3 + (spell_level - 1)
    type_of_damage_dice = 8

    initial_roll = roll_dice(number_of_damage_dice, type_of_damage_dice, elemental_adept)
    if charisma_modifier > 0 and reroll_strategy:
        initial_roll = reroll_strategy(initial_roll, charisma_modifier, elemental_adept)
    total_damage = sum(initial_roll)

    leaps = 0
    if check_for_pair(initial_roll) and number_of_targets > 1:
        max_leaps = spell_level

        for _ in range(min(max_leaps, number_of_targets - 1)):
            leaps += 1
            additional_roll = roll_dice(number_of_damage_dice, type_of_damage_dice, elemental_adept)
            total_damage += sum(additional_roll)

            if not check_for_pair(additional_roll):
                break

    return total_damage, leaps

def run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, reroll_strategy, label):
    print(f"Running {simulations} simulation on {label}")
    damages_list = []
    leaps_list = []
    first_leap_count = 0
    for _ in range(simulations):
        number_of_damage_dice = 3 + (spell_level - 1)
        type_of_damage_dice = 8
        initial_roll = roll_dice(number_of_damage_dice, type_of_damage_dice, elemental_adept)
        if charisma_modifier > 0 and reroll_strategy:
            initial_roll = reroll_strategy(initial_roll, charisma_modifier, elemental_adept)
        if check_for_pair(initial_roll) and number_of_targets > 1:
            first_leap_count += 1
        damage, leaps = chromatic_orb(spell_level, number_of_targets, elemental_adept, charisma_modifier, reroll_strategy)
        damages_list.append(damage)
        leaps_list.append(leaps)
    avg_damage = sum(damages_list) / simulations
    avg_leaps = sum(leaps_list) / simulations
    first_leap = first_leap_count / simulations
    return (label, avg_damage, avg_leaps, first_leap)

def main():
    simulations = 100000
    spell_level = 2
    number_of_targets = spell_level + 1
    elemental_adept = True
    charisma_modifier = 4
    print(f"\nSimulating Chromatic Orb (Spell level {spell_level}, {number_of_targets} targets, {'Elemental Adept' if elemental_adept else 'no Elemental Adept'}, Empowered Spell +{charisma_modifier}):\n")
    results = []
    results.append(run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_nothing, "Never reroll any dice"))
    results.append(run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_all, "Reroll all dice, if no pair"))
    results.append(run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_all_except_2, "Reroll all dice, except 2s, if no pair"))
    #results.append(run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_below_average, "Reroll dice below average (<=4), if no pair"))
    #results.append(run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_below_average_except_2, "Reroll dice below average (<=4), except 2, if no pair"))
    #results.append(run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_never_high, "Never reroll if all dice are high (>=5), if no pair"))
    results.append(run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_keep_8s, "Reroll all dice except 8s, if no pair"))
    results.append(run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_keep_2s_and_8s, "Reroll all dice except 2s and 8s, if no pair"))
    results.append(run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_keep_7s_and_8s, "Reroll all dice except 7s and 8s, if no pair"))
    results.append(run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_keep_6s_7s_and_8s, "Reroll all dice except 6s, 7s and 8s, if no pair"))
    results.append(run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_keep_decision_tree, "Decision Tree"))

    # Sort results by avg_damage ascending
    results.sort(key=lambda x: x[1], reverse=False)
    # Write markdown table to file
    with open("results.md", "w", encoding="utf-8") as f:
        f.write(f"Simulating Chromatic Orb (Spell level {spell_level}, on {number_of_targets} targets, {'Elemental Adept' if elemental_adept else 'no Elemental Adept'}, Empowered Spell +{charisma_modifier}):\n\n")
        f.write("| Simulation name | Avg damage | Avg leaps | First leap chance |\n")
        f.write("|---|---|---|---|\n")
        for label, avg_damage, avg_leaps, first_leap in results:
            f.write(f"| {label} | {avg_damage:.2f} | {avg_leaps:.2f} | {first_leap:.2f} |\n")
    print("\nResults saved to results.md\n")

if __name__ == "__main__":
    main()