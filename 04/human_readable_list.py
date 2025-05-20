def human_readable_list(l):
    if len(l) == 0:
        return str(l)
    elif len(l) == 1:
        return str(l[0])
    else:
        return f"{', '.join(l[:-1])} and {l[-1]}"


print(human_readable_list(("apples",)))
print(human_readable_list(("apples", "bananas")))
print(human_readable_list(("apples", "bananas", "tofu")))
print(human_readable_list(("apples", "bananas", "tofu", "cats")))
