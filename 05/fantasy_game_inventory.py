def display_inventory(inventory):
    print("Inventory:")

    for k, v in inventory.items():
        print(f"{v} {k}")

    print(f"Total number of items: {sum(inventory.values())}")


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


print("Demonstration of display_inventory():")
stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
display_inventory(stuff)

print()

print("Demonstration of add_to_inventory():")
inv = {"gold coin": 42, "rope": 1}
dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
