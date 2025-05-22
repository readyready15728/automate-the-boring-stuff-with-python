birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}

while True:
    print("Enter a name (blank to quit):")
    name = input()

    if name == "":
        break
    elif name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name}")
    else:
        print(f"I do not have birthday information for {name}")
        print("What is their birthday?")
        b_day = input()
        birthdays[name] = b_day
        print("Birthday database updated.")
