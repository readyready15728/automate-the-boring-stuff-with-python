import random


def is_streak_present(coin_flips, streak_length=6):
    for i in range(len(coin_flips) - streak_length + 1):
        if all(flip == "H" for flip in coin_flips[i : i + streak_length]):
            return True

    return False


number_of_experiments = 10_000
length_of_experiment = 100
successes = 0

for _ in range(number_of_experiments):
    experiment = [random.choice(("H", "T")) for _ in range(length_of_experiment)]
    successes += is_streak_present(experiment)

print(f"Chance of streak: {successes / number_of_experiments:.2%}")
