stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


def display_inventory(inventory):
    print("Inventory:")

    for k, v in inventory.items():
        print(f"{v} {k}")

    print(f"Total number of items: {sum(inventory.values())}")


display_inventory(stuff)
