def collatz(n):
    yield n

    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
            yield n
        else:
            n = int(3 * n + 1)
            yield n


print("Enter number:")

try:
    n = int(input())
except ValueError:
    print("Invalid input")

print(" ".join(map(str, collatz(n))))
