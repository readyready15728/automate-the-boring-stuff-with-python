def print_table(table):
    column_widths = [max(map(len, column)) for column in zip(*table)]
    formatted_rows = []

    for row in table:
        formatted_rows.append(
            " ".join(item.rjust(column_widths[i]) for i, item in enumerate(row))
        )

    print("\n".join(formatted_rows))


table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]

print_table(table_data)
