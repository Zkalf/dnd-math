# roll 4d8 where 1 become 2
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

def main():
    simulations = 100000
    damage = 0
    leaps = 0
    for _ in range(simulations):
        number_of_dice = 4
        sides = 8
        elemental_adept = True
        rolls = roll_dice(number_of_dice, sides, elemental_adept)
        if check_for_pair(rolls):
            leaps += 1
        else:
            reroll_indices = sorted(range(len(rolls)), key=lambda i: rolls[i])
            for i in reroll_indices:
                rolls[i] = reroll_damage_dice(elemental_adept)
            leaps += 1 if check_for_pair(rolls) else 0
        damage += sum(rolls)
    avg_leap = leaps / simulations
    avg_dmg = damage / simulations
    print(f"{avg_leap:.2f}")
    print(f"{avg_dmg:.2f}")

if __name__ == "__main__":
    main()