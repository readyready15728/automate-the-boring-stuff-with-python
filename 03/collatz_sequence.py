import sys


def collatz(x):
    while x != 1:
        if x % 2 == 0:  # x is even
            x /= 2
        else:  # x is odd
            x = 3 * x + 1

        x = int(x)  # Conversion necessary due to division operation
        yield x

    # yield x  # The terminal 1 counts as part of the sequence


print("Enter number: ", end="")

try:
    seed = int(input())
except ValueError:
    print("Invalid input")
    sys.exit(1)

for x in collatz(seed):
    print(x)
