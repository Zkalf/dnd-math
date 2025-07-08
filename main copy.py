import random

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
    damages_list = []
    leaps_list = []
    first_leap_count = 0
    for _ in range(simulations):
        # First leap simulation, not used in full simulation
        number_of_damage_dice = 3 + (spell_level - 1)
        type_of_damage_dice = 8
        initial_roll = roll_dice(number_of_damage_dice, type_of_damage_dice, elemental_adept)
        if charisma_modifier > 0 and reroll_strategy:
            initial_roll = reroll_strategy(initial_roll, charisma_modifier, elemental_adept)
        if check_for_pair(initial_roll) and number_of_targets > 1:
            first_leap_count += 1
        # Run the full simulation
        damage, leaps = chromatic_orb(spell_level, number_of_targets, elemental_adept, charisma_modifier, reroll_strategy)
        damages_list.append(damage)
        leaps_list.append(leaps)
    avg_damage = sum(damages_list) / simulations
    avg_leaps = sum(leaps_list) / simulations
    first_leap = first_leap_count / simulations
    print(f"{label}")
    print(f"  Average damage dealt: {avg_damage:.2f}")
    print(f"  Average number of leaps: {avg_leaps:.2f}")
    print(f"  First leap chance: {first_leap:.2f}\n")

def main():
    simulations = 100000
    spell_level = 2
    number_of_targets = spell_level + 1
    elemental_adept = True
    charisma_modifier = 4
    print(f"Simulating Chromatic Orb (Spell level {spell_level}, on {number_of_targets} targets, {'Elemental Adept' if elemental_adept else 'no Elemental Adept'}, Empowered Spell +{charisma_modifier}):\n")
    run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_nothing, "Never reroll any dice")
    run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_all, "Reroll all dice, if no pair")
    run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_all_except_2, "Always reroll, except dice showing 2, if no pair")
    #run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_below_average, "Reroll dice below average (<=4), if no pair")
    #run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_below_average_except_2, "Reroll dice below average (<=4), except 2, if no pair")
    #run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_never_high, "Never reroll if all dice are high (>=5), if no pair")
    run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_keep_8s, "Reroll all dice except 8s, if no pair")
    run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_keep_2s_and_8s, "Reroll all dice except 2s and 8s, if no pair")
    run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_keep_7s_and_8s, "Reroll all dice except 7s and 8s, if no pair")
    run_simulation(simulations, spell_level, number_of_targets, elemental_adept, charisma_modifier, empowered_reroll_strategy_keep_6s_7s_and_8s, "Reroll all dice except 6s, 7s and 8s, if no pair")

if __name__ == "__main__":
    main()