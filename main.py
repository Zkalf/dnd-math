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

def empowered_reroll_strategy_none(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls, {"has_pair": True, "condition_triggered": False, "reroll_all": False}
    return dice_rolls, {"has_pair": False, "condition_triggered": False, "reroll_all": False}

def empowered_reroll_strategy_all(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls, {"has_pair": True, "condition_triggered": False, "reroll_all": False}
    reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls, {"has_pair": False, "condition_triggered": False, "reroll_all": True}

def empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values):
    if check_for_pair(dice_rolls):
        return dice_rolls, {"has_pair": True, "condition_triggered": False, "reroll_all": False}
    if keep_condition:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v not in keep_values][:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": True, "reroll_all": False}
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": False, "reroll_all": True}
    
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls, tracking

def empowered_reroll_strategy_keep_2(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2 then reroll remaining dice, else reroll all
    keep_values = [2]
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, any(x in dice_rolls for x in keep_values), keep_values)

def empowered_reroll_strategy_keep_6(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 6 then reroll remaining dice, else reroll all
    keep_values = [6]
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, any(x in dice_rolls for x in keep_values), keep_values)

def empowered_reroll_strategy_keep_7(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 7 then reroll remaining dice, else reroll all
    keep_values = [7]
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, any(x in dice_rolls for x in keep_values), keep_values)

def empowered_reroll_strategy_keep_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 8 then reroll remaining dice, else reroll all
    keep_values = [8]
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, any(x in dice_rolls for x in keep_values), keep_values)

def empowered_reroll_strategy_keep_2_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2 and 8 then reroll remaining dice, else reroll all
    keep_values = [2, 8]
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, all(x in dice_rolls for x in keep_values), keep_values)

def empowered_reroll_strategy_keep_2_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2 or 8 then reroll remaining dice, else reroll all
    keep_values = [2, 8]
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, any(x in dice_rolls for x in keep_values), keep_values)

def empowered_reroll_strategy_keep_7_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 7 and 8 then reroll remaining dice, else reroll all
    keep_values = [7, 8]
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, all(x in dice_rolls for x in keep_values), keep_values)

def empowered_reroll_strategy_keep_7_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 7 or 8 then reroll remaining dice, else reroll all
    keep_values = [7, 8]
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, any(x in dice_rolls for x in keep_values), keep_values)

def empowered_reroll_strategy_keep_2_and_7_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2, 7 and 8 then reroll remaining dice, else reroll all
    keep_values = [2, 7, 8]
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, all(x in dice_rolls for x in keep_values), keep_values)

def empowered_reroll_strategy_keep_2_or_7_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2, 7 or 8 then reroll remaining dice, else reroll all
    keep_values = [2, 7, 8]
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, any(x in dice_rolls for x in keep_values), keep_values)

def empowered_reroll_strategy_keep_6_and_7_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 6, 7 and 8 then reroll remaining dice, else reroll all
    keep_values = [6, 7, 8]
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, all(x in dice_rolls for x in keep_values), keep_values)

def empowered_reroll_strategy_keep_6_or_7_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 6, 7 or 8 then reroll remaining dice, else reroll all
    keep_values = [6, 7, 8]
    return empowered_reroll_keep(dice_rolls, charisma_modifier, elemental_adept, any(x in dice_rolls for x in keep_values), keep_values)

def empowered_reroll_strategy_keep_decision_tree1(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls, {"has_pair": True, "condition_triggered": False, "reroll_all": False}
    
    # if dice_rolls have 7 and 8 then reroll remaining dice
    if 7 in dice_rolls and 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 7 and v != 8][:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": True, "reroll_all": False, "condition": "7_and_8"}
    # elif dice_rolls have 2 and 8 then reroll remaining dice
    elif 2 in dice_rolls and 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 2 and v != 8][:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": True, "reroll_all": False, "condition": "2_and_8"}
    # elif dice_rolls have 8 then reroll remaining dice
    elif 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 8][:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": True, "reroll_all": False, "condition": "8"}
    # elif dice_rolls have 2 then reroll remaining dice
    elif 2 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 2][:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": True, "reroll_all": False, "condition": "2"}
    # else reroll all
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": False, "reroll_all": True}
    
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls, tracking

def empowered_reroll_strategy_keep_decision_tree2(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls, {"has_pair": True, "condition_triggered": False, "reroll_all": False}
    
    # if dice_rolls have 7 or 8 then reroll remaining dice
    if 7 in dice_rolls or 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 7 and v != 8][:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": True, "reroll_all": False, "condition": "7_or_8"}
    # elif dice_rolls have 6 then reroll remaining dice
    elif 6 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 6][:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": True, "reroll_all": False, "condition": "6"}
    # else reroll all
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": False, "reroll_all": True}
    
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls, tracking

def empowered_reroll_strategy_keep_decision_tree3(dice_rolls, charisma_modifier, elemental_adept):
    if check_for_pair(dice_rolls):
        return dice_rolls, {"has_pair": True, "condition_triggered": False, "reroll_all": False}
    
    # if dice_rolls have 7 or 8 then reroll remaining dice
    if 7 in dice_rolls or 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 7 and v != 8][:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": True, "reroll_all": False, "condition": "7_or_8"}
    # elif dice_rolls have 6 then reroll remaining dice
    elif 6 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 6][:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": True, "reroll_all": False, "condition": "6"}
    # elif dice_rolls have 2 then reroll remaining dice
    elif 2 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 2][:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": True, "reroll_all": False, "condition": "2"}
    # else reroll all
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
        tracking = {"has_pair": False, "condition_triggered": False, "reroll_all": True}
    
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls, tracking

def chromatic_orb(spell_level, targets, elemental_adept, charisma_modifier, reroll_strategy):
    dice = 3 + (spell_level - 1)
    sides = 8

    initial_roll = roll_damage_dice(dice, sides, elemental_adept)
    tracking_info = None
    if charisma_modifier > 0 and reroll_strategy:
        initial_roll, tracking_info = reroll_strategy(initial_roll, charisma_modifier, elemental_adept)
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

    return total_damage, leaps, first_leap_triggered, tracking_info

def simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, reroll_strategy, label):
    print(f"Running {simulations} simulation on {label}")
    damages_list = []
    leaps_list = []
    first_leap_list = []
    tracking_stats = {
        "has_pair": 0,
        "condition_triggered": 0,
        "reroll_all": 0
    }
    
    for _ in range(simulations):
        damage, leaps, first_leap_triggered, tracking_info = chromatic_orb(spell_level, targets, elemental_adept, charisma_modifier, reroll_strategy)
        damages_list.append(damage)
        leaps_list.append(leaps)
        first_leap_list.append(first_leap_triggered)
        
        if tracking_info:
            if tracking_info["has_pair"]:
                tracking_stats["has_pair"] += 1
            if tracking_info["condition_triggered"]:
                tracking_stats["condition_triggered"] += 1
            if tracking_info["reroll_all"]:
                tracking_stats["reroll_all"] += 1
    
    avg_damage = sum(damages_list) / simulations
    avg_leaps = sum(leaps_list) / simulations
    first_leap = sum(first_leap_list) / simulations
    
    # Convert tracking stats to percentages
    tracking_percentages = {
        "has_pair": tracking_stats["has_pair"] / simulations,
        "condition_triggered": tracking_stats["condition_triggered"] / simulations,
        "reroll_all": tracking_stats["reroll_all"] / simulations
    }
    
    return (label, avg_damage, avg_leaps, first_leap, tracking_percentages)

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
                            empowered_reroll_strategy_keep_decision_tree1, "Decision Tree1"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_decision_tree2, "Decision Tree2"))
    results.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                            empowered_reroll_strategy_keep_decision_tree3, "Decision Tree3"))

    # Sort results by avg_damage ascending
    results.sort(key=lambda x: x[1], reverse=False)
    # Write markdown table to file
    with open("results.md", "w", encoding="utf-8") as f:
        f.write(f"Simulating Chromatic Orb (Spell level {spell_level}, on {targets} targets, {'Elemental Adept' if elemental_adept else 'no Elemental Adept'}, Empowered Spell +{charisma_modifier}).\n\n")
        f.write("For all strategies:\n\n")
        f.write("- if has pair -> skip reroll\n")
        f.write("- if condition triggered -> keep specific dice and reroll remaining\n")
        f.write("- else -> reroll all lowest dice\n\n")
        f.write("| Simulation name | Avg damage | Avg leaps | First leap % | Has pair % | Condition triggered % | Reroll all % |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        for label, avg_damage, avg_leaps, first_leap, tracking in results:
            f.write(f"| {label} | {avg_damage:.3f} | {avg_leaps:.3f} | {first_leap:.3f} | {tracking['has_pair']:.3f} | {tracking['condition_triggered']:.3f} | {tracking['reroll_all']:.3f} |\n")

    print("\nResults saved to results.md\n")

if __name__ == "__main__":
    main()