from itertools import combinations

# Probabilities for faces 2-8
probs = [2/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]

# Enumerate all 4-combinations of faces
total_prob = 0
for combo in combinations(range(7), 4):
    p = 1
    for idx in combo:
        p *= probs[idx]
    total_prob += 24 * p  # 24 = 4! permutations

print(f"P(all different) = {total_prob:.4f}")
print(f"P(at least one pair) = {1 - total_prob:.4f}")