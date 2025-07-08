import random

def simulate_coin_tosses(simulations):
    coin_toss = 0
    for _ in range(simulations):
        coin_toss += random.randint(0, 1)
    print(f"Simulations: {simulations}")
    print(f"Coin tosses: {coin_toss}")
    print(f"Probability of heads: {coin_toss / simulations:.3f}")
    print("---")

simulate_coin_tosses(1)
simulate_coin_tosses(10)
simulate_coin_tosses(100)
simulate_coin_tosses(1000)
simulate_coin_tosses(10000)
simulate_coin_tosses(100000)
simulate_coin_tosses(1000000)