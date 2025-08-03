def add_commas(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return str(items[0])
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        return ", ".join(map(str, items[:-1])) + f", and {items[-1]}"


print(add_commas([]))
print(add_commas(["apples"]))
print(add_commas(["apples", "bananas"]))
print(add_commas(["apples", "bananas", "tofu"]))
print(add_commas(["apples", "bananas", "tofu", "cats"]))
