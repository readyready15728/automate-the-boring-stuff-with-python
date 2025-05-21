# Formula shamelessly cribbed from:
#
# https://www.askamathematician.com/2010/07/q-whats-the-chance-of-getting-a-run-of-k-successes-in-n-bernoulli-trials-why-use-approximations-when-the-exact-answer-is-known/
# https://web.archive.org/web/20250303004627/https://www.askamathematician.com/2010/07/q-whats-the-chance-of-getting-a-run-of-k-successes-in-n-bernoulli-trials-why-use-approximations-when-the-exact-answer-is-known/

import math


def custom_comb(a, b):
    if a < b:
        return 0
    else:
        return math.comb(a, b)


def s(n, k, p, upper_limit=100):
    q = 1 - p
    left_sum = sum(
        custom_comb(n - (t + 1) * k, t) * (-q * p**k) ** t for t in range(upper_limit)
    )
    right_sum = sum(
        custom_comb(n - t * k, t) * (-q * p**k) ** t for t in range(1, upper_limit)
    )
    return p**k * left_sum - right_sum


print(f"Chance of streak: {s(100, 6, 0.5):.2%}")
