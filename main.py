import json
import random

def roll_attack_dice(spell_attack_bonus, armor_class):
    attack_roll = random.randint(1, 20)
    crit = (attack_roll == 20)
    hit = crit or (attack_roll + spell_attack_bonus) >= armor_class
    return hit, crit

def roll_damage_dice(dice, sides, elemental_adept, crit=False):
    actual_dice = dice * 2 if crit else dice
    rolls = [random.randint(1, sides) for _ in range(actual_dice)]
    if elemental_adept:
        rolls = [2 if roll == 1 else roll for roll in rolls]
    return rolls

def reroll_damage_dice(elemental_adept):
    new_roll = random.randint(1, 8)
    if elemental_adept and new_roll == 1:
        new_roll = 2
    return new_roll

def has_pair(dice_rolls):
    return len(set(dice_rolls)) < len(dice_rolls)

def reroll_strategy_none(dice_rolls, charisma_modifier, elemental_adept):
    if has_pair(dice_rolls):
        return dice_rolls, {"pair": True, "condition": False, "reroll_all": False}
    return dice_rolls, {"pair": False, "condition": True, "reroll_all": False}

def reroll_strategy_all(dice_rolls, charisma_modifier, elemental_adept):
    if has_pair(dice_rolls):
        return dice_rolls, {"pair": True, "condition": False, "reroll_all": False}
    reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls, {"pair": False, "condition": True, "reroll_all": True}

def reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values):
    if has_pair(dice_rolls):
        return dice_rolls, {"pair": True, "condition": False, "reroll_all": False}
    if keep_condition:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v not in keep_values][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False}
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
        tracking = {"pair": False, "condition": False, "reroll_all": True}
    
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls, tracking

def reroll_strategy_keep_2(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2 then reroll remaining dice, else reroll all
    keep_values = [2]
    keep_condition = any(x in dice_rolls for x in keep_values)
    return reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values)

def reroll_strategy_keep_6(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 6 then reroll remaining dice, else reroll all
    keep_values = [6]
    keep_condition = any(x in dice_rolls for x in keep_values)
    return reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values)

def reroll_strategy_keep_7(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 7 then reroll remaining dice, else reroll all
    keep_values = [7]
    keep_condition = any(x in dice_rolls for x in keep_values)
    return reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values)

def reroll_strategy_keep_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 8 then reroll remaining dice, else reroll all
    keep_values = [8]
    keep_condition = any(x in dice_rolls for x in keep_values)
    return reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values)

def reroll_strategy_keep_2_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2 and 8 then reroll remaining dice, else reroll all
    keep_values = [2, 8]
    keep_condition = all(x in dice_rolls for x in keep_values)
    return reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values)

def reroll_strategy_keep_2_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2 or 8 then reroll remaining dice, else reroll all
    keep_values = [2, 8]
    keep_condition = any(x in dice_rolls for x in keep_values)
    return reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values)

def reroll_strategy_keep_7_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 7 and 8 then reroll remaining dice, else reroll all
    keep_values = [7, 8]
    keep_condition = all(x in dice_rolls for x in keep_values)
    return reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values)

def reroll_strategy_keep_7_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 7 or 8 then reroll remaining dice, else reroll all
    keep_values = [7, 8]
    keep_condition = any(x in dice_rolls for x in keep_values)
    return reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values)

def reroll_strategy_keep_2_and_7_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2, 7 and 8 then reroll remaining dice, else reroll all
    keep_values = [2, 7, 8]
    keep_condition = all(x in dice_rolls for x in keep_values)
    return reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values)

def reroll_strategy_keep_2_or_7_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 2, 7 or 8 then reroll remaining dice, else reroll all
    keep_values = [2, 7, 8]
    keep_condition = any(x in dice_rolls for x in keep_values)
    return reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values)

def reroll_strategy_keep_6_and_7_and_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 6, 7 and 8 then reroll remaining dice, else reroll all
    keep_values = [6, 7, 8]
    keep_condition = all(x in dice_rolls for x in keep_values)
    return reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values)

def reroll_strategy_keep_6_or_7_or_8(dice_rolls, charisma_modifier, elemental_adept):
    # if dice_rolls have 6, 7 or 8 then reroll remaining dice, else reroll all
    keep_values = [6, 7, 8]
    keep_condition = any(x in dice_rolls for x in keep_values)
    return reroll_keep(dice_rolls, charisma_modifier, elemental_adept, keep_condition, keep_values)

def reroll_strategy_keep_decision_tree1(dice_rolls, charisma_modifier, elemental_adept):
    if has_pair(dice_rolls):
        return dice_rolls, {"pair": True, "condition": False, "reroll_all": False}
    
    # if dice_rolls have 7 and 8 then reroll remaining dice
    if 7 in dice_rolls and 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 7 and v != 8][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "7_and_8"}
    # elif dice_rolls have 2 and 8 then reroll remaining dice
    elif 2 in dice_rolls and 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 2 and v != 8][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "2_and_8"}
    # elif dice_rolls have 8 then reroll remaining dice
    elif 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 8][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "8"}
    # elif dice_rolls have 2 then reroll remaining dice
    elif 2 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 2][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "2"}
    # else reroll all
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
        tracking = {"pair": False, "condition": False, "reroll_all": True}
    
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls, tracking

def reroll_strategy_keep_decision_tree2(dice_rolls, charisma_modifier, elemental_adept):
    if has_pair(dice_rolls):
        return dice_rolls, {"pair": True, "condition": False, "reroll_all": False}
    
    # if dice_rolls have 7 or 8 then reroll remaining dice
    if 7 in dice_rolls or 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 7 and v != 8][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "7_or_8"}
    # elif dice_rolls have 6 then reroll remaining dice
    elif 6 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 6][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "6"}
    # else reroll all
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
        tracking = {"pair": False, "condition": False, "reroll_all": True}
    
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls, tracking

def reroll_strategy_keep_decision_tree3(dice_rolls, charisma_modifier, elemental_adept):
    if has_pair(dice_rolls):
        return dice_rolls, {"pair": True, "condition": False, "reroll_all": False}
    
    # if dice_rolls have 7 or 8 then reroll remaining dice
    if 7 in dice_rolls or 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 7 and v != 8][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "7_or_8"}
    # elif dice_rolls have 6 then reroll remaining dice
    elif 6 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 6][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "6"}
    # elif dice_rolls have 2 then reroll remaining dice
    elif 2 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 2][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "2"}
    # else reroll all
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
        tracking = {"pair": False, "condition": False, "reroll_all": True}
    
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls, tracking

def reroll_strategy_keep_decision_tree4(dice_rolls, charisma_modifier, elemental_adept):
    if has_pair(dice_rolls):
        return dice_rolls, {"pair": True, "condition": False, "reroll_all": False}
    
    # Priority 1: If we have 8, always keep it (and any 7s too for maximum value)
    if 8 in dice_rolls:
        if 7 in dice_rolls:
            # Keep both 7s and 8s
            reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 7 and v != 8][:charisma_modifier]
            tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "8_and_7"}
        else:
            # Keep just 8s
            reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 8][:charisma_modifier]
            tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "8"}
    
    # Priority 2: If we have 7 (but no 8), keep it
    elif 7 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 7][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "7"}
    
    # Priority 3: If we have 6 (but no 7 or 8), keep it
    elif 6 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 6][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "6"}
    
    # Fallback: Reroll all lowest dice
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
        tracking = {"pair": False, "condition": False, "reroll_all": True}
    
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls, tracking

def reroll_strategy_keep_decision_tree5(dice_rolls, charisma_modifier, elemental_adept):
    if has_pair(dice_rolls):
        return dice_rolls, {"pair": True, "condition": False, "reroll_all": False}
    
    # Priority 1: If we have 7 or 8, keep both types (like Decision Tree2)
    if 7 in dice_rolls or 8 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 7 and v != 8][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "7_or_8"}
    
    # Priority 2: If we have 6 (but no 7 or 8), keep it (like Decision Tree2)
    elif 6 in dice_rolls:
        reroll_indices = [i for i, v in enumerate(dice_rolls) if v != 6][:charisma_modifier]
        tracking = {"pair": False, "condition": True, "reroll_all": False, "condition": "6"}
    
    # Fallback: Reroll all lowest dice (minimal occurrence)
    else:
        reroll_indices = sorted(range(len(dice_rolls)), key=lambda i: dice_rolls[i])[:charisma_modifier]
        tracking = {"pair": False, "condition": False, "reroll_all": True}
    
    for i in reroll_indices:
        dice_rolls[i] = reroll_damage_dice(elemental_adept)
    return dice_rolls, tracking

def chromatic_orb(spell_level, targets, elemental_adept, charisma_modifier, reroll_strategy, spell_attack_bonus, armor_class):
    dice = 3 + (spell_level - 1)
    sides = 8

    hit, crit = roll_attack_dice(spell_attack_bonus, armor_class)
    if not hit:
        # total_damage, leaps, first_leap_triggered, tracking, crit
        return 0, 0, 0, None, False

    initial_roll = roll_damage_dice(dice, sides, elemental_adept, crit)
    tracking = None
    if charisma_modifier > 0 and reroll_strategy:
        initial_roll, tracking = reroll_strategy(initial_roll, charisma_modifier, elemental_adept)
    
    total_damage = sum(initial_roll)

    leaps = 0
    first_leap = 0
    if has_pair(initial_roll) and targets > 1:
        first_leap = 1
        max_leaps = spell_level

        for _ in range(min(max_leaps, targets - 1)):
            leap_hit, leap_crit = roll_attack_dice(spell_attack_bonus, armor_class)
            if not leap_hit:
                break
            
            leaps += 1
            additional_roll = roll_damage_dice(dice, sides, elemental_adept, leap_crit)
            total_damage += sum(additional_roll)

            if not has_pair(additional_roll):
                break

    return total_damage, leaps, first_leap, tracking, crit

def simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, reroll_strategy, label, spell_attack_bonus, armor_class):
    print(f"Running {simulations} simulation on {label}")
    damages_list = []
    leaps_list = []
    first_leap_list = []
    hit_count = 0
    crit_count = 0
    tracking_occurrence = {
        "pair": 0,
        "condition": 0,
        "reroll_all": 0
    }
    tracking_damage = {
        "pair": [],
        "condition": [],
        "reroll_all": []
    }
    tracking_leaps = {
        "pair": [],
        "condition": [],
        "reroll_all": []
    }
    
    for _ in range(simulations):
        damage, leaps, first_leap, tracking, crit = chromatic_orb(spell_level, targets, elemental_adept, charisma_modifier, reroll_strategy, spell_attack_bonus, armor_class)
        damages_list.append(damage)
        leaps_list.append(leaps)
        first_leap_list.append(first_leap)
        
        if damage > 0:
            hit_count += 1
            if crit:
                crit_count += 1
        
        if tracking:
            if tracking["pair"]:
                tracking_occurrence["pair"] += 1
                tracking_damage["pair"].append(damage)
                tracking_leaps["pair"].append(leaps)
            if tracking["condition"]:
                tracking_occurrence["condition"] += 1
                tracking_damage["condition"].append(damage)
                tracking_leaps["condition"].append(leaps)
            if tracking["reroll_all"]:
                tracking_occurrence["reroll_all"] += 1
                tracking_damage["reroll_all"].append(damage)
                tracking_leaps["reroll_all"].append(leaps)
    
    avg_damage = sum(damages_list) / simulations
    avg_leaps = sum(leaps_list) / simulations
    first_leap = sum(first_leap_list) / simulations
    hit_rate = hit_count / simulations
    crit_rate = crit_count / simulations
    
    tracking_rate = {
        "pair": tracking_occurrence["pair"] / simulations,
        "condition": tracking_occurrence["condition"] / simulations,
        "reroll_all": tracking_occurrence["reroll_all"] / simulations
    }
    tracking_avg_damage = {
        "pair_avg_damage": sum(tracking_damage["pair"]) / len(tracking_damage["pair"]) if tracking_damage["pair"] else 0,
        "condition_avg_damage": sum(tracking_damage["condition"]) / len(tracking_damage["condition"]) if tracking_damage["condition"] else 0,
        "reroll_all_avg_damage": sum(tracking_damage["reroll_all"]) / len(tracking_damage["reroll_all"]) if tracking_damage["reroll_all"] else 0
    }
    tracking_avg_leaps = {
        "pair_avg_leaps": sum(tracking_leaps["pair"]) / len(tracking_leaps["pair"]) if tracking_leaps["pair"] else 0,
        "condition_avg_leaps": sum(tracking_leaps["condition"]) / len(tracking_leaps["condition"]) if tracking_leaps["condition"] else 0,
        "reroll_all_avg_leaps": sum(tracking_leaps["reroll_all"]) / len(tracking_leaps["reroll_all"]) if tracking_leaps["reroll_all"] else 0
    }
    
    return (label, avg_damage, avg_leaps, first_leap, hit_rate, crit_rate, tracking_rate, tracking_avg_damage, tracking_avg_leaps)

def main():
    simulations = 1000000

    proficiency_bonus = 3
    charisma_modifier = 4
    spell_attack_bonus = proficiency_bonus + charisma_modifier
    armor_class = 17

    spell_level = 2
    targets = spell_level + 1
    elemental_adept = True

    print(f"\nSimulating {simulations} Chromatic Orb (Spell level {spell_level}, {targets} targets, {'Elemental Adept' if elemental_adept else 'no Elemental Adept'}, Empowered Spell +{charisma_modifier}, Attack +{spell_attack_bonus} vs AC {armor_class}):\n")
    
    simple_strategies = []
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_none, "Reroll none", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_all, "Reroll all", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_keep_2, "Keep 2", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_keep_6, "Keep 6", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_keep_7, "Keep 7", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_keep_8, "Keep 8", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_keep_2_and_8, "Keep 2 and 8", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_keep_2_or_8, "Keep 2 or 8", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_keep_7_and_8, "Keep 7 and 8", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_keep_7_or_8, "Keep 7 or 8", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_keep_2_and_7_and_8, "Keep 2 and 7 and 8", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_keep_2_or_7_or_8, "Keep 2 or 7 or 8", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_keep_6_and_7_and_8, "Keep 6 and 7 and 8", spell_attack_bonus, armor_class))
    simple_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                      reroll_strategy_keep_6_or_7_or_8, "Keep 6 or 7 or 8", spell_attack_bonus, armor_class))
    
    decision_tree_strategies = []
    decision_tree_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                             reroll_strategy_keep_decision_tree1, "Decision Tree1", spell_attack_bonus, armor_class))
    decision_tree_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                             reroll_strategy_keep_decision_tree2, "Decision Tree2", spell_attack_bonus, armor_class))
    decision_tree_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                             reroll_strategy_keep_decision_tree3, "Decision Tree3", spell_attack_bonus, armor_class))
    decision_tree_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                             reroll_strategy_keep_decision_tree4, "Decision Tree4", spell_attack_bonus, armor_class))
    decision_tree_strategies.append(simulate(simulations, spell_level, targets, elemental_adept, charisma_modifier, 
                                             reroll_strategy_keep_decision_tree5, "Decision Tree5", spell_attack_bonus, armor_class))
    
    # Sort simple strategies by condition_avg_damage ascending
    simple_strategies.sort(key=lambda x: x[7]["condition_avg_damage"], reverse=False)
    # Sort decision tree strategies by avg_damage ascending
    decision_tree_strategies.sort(key=lambda x: x[1], reverse=False)
    
    with open("results.md", "w", encoding="utf-8") as f:
        f.write("# Simulating Chromatic Orb\n")

        f.write("\n")

        f.write(f"- Simulations = {simulations}\n")
        f.write(f"- Proficiency bonus = {proficiency_bonus}\n")
        f.write(f"- Charisma modifier = {charisma_modifier}\n")
        f.write(f"- Spell attack bonus = {spell_attack_bonus}\n")
        f.write(f"- Armor class = {armor_class}\n")
        f.write(f"- Spell level = {spell_level}\n")
        f.write(f"- Targets = {targets}\n")
        f.write(f"- Elemental Adept = {'Yes' if elemental_adept else 'No'}\n")
        f.write(f"- Hit % = {simple_strategies[5][4]:.2f}\n")
        f.write(f"- Crit % = {simple_strategies[5][5]:.2f}\n")
        f.write("- Pair condition + Strategy condition + Reroll all condition = Hit %\n")

        f.write("\n")

        # Simple Strategies Table
        f.write("## Simple Strategies (sorted by 'Strategy condition avg damage' ascending)\n\n")
        f.write("| Strategy | Avg damage | Avg leaps | Pair condition % | Strategy condition % | Reroll all condition % | Strategy condition avg damage | Strategy condition avg leaps |\n")
        f.write("|---|---|---|---|---|---|---|---|\n")
        for label, avg_damage, avg_leaps, first_leap, hit_rate, crit_rate, tracking_rate, tracking_avg_damage, tracking_avg_leaps in simple_strategies:
            f.write(f"| {label} | {avg_damage:.2f} | {avg_leaps:.2f} | {tracking_rate['pair']:.2f} | {tracking_rate['condition']:.2f} | {tracking_rate['reroll_all']:.2f} | {tracking_avg_damage['condition_avg_damage']:.2f} | {tracking_avg_leaps['condition_avg_leaps']:.2f} |\n")

        f.write("\n")
        
        # Decision Tree Strategies Table
        f.write("## Decision Tree Strategies (sorted by 'Avg damage' ascending)\n\n")
        f.write("| Strategy | Avg damage | Avg leaps | Pair condition % | Strategy condition % | Reroll all condition % | Strategy condition avg damage | Strategy condition avg leaps |\n")
        f.write("|---|---|---|---|---|---|---|---|\n")
        for label, avg_damage, avg_leaps, first_leap, hit_rate, crit_rate, tracking_rate, tracking_avg_damage, tracking_avg_leaps in decision_tree_strategies:
            f.write(f"| {label} | {avg_damage:.2f} | {avg_leaps:.2f} | {tracking_rate['pair']:.2f} | {tracking_rate['condition']:.2f} | {tracking_rate['reroll_all']:.2f} | {tracking_avg_damage['condition_avg_damage']:.2f} | {tracking_avg_leaps['condition_avg_leaps']:.2f} |\n")

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump({"simple_strategies": simple_strategies, "decision_tree_strategies": decision_tree_strategies}, f, ensure_ascii=False, indent=4)

    print("\nResults saved to results.md")
    print("Results saved to results.json\n")

if __name__ == "__main__":
    main()