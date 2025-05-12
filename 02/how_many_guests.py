name = None

while not name:
    print("Enter your name:")
    name = input()

print("How many guests will you have?")
num_of_guests = int(input())

if num_of_guests:
    print("Be sure to have room for all your guests.")

print("Done")
