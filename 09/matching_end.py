import re

ends_with_number = re.compile(r"\d$")
print(ends_with_number.search("Your number is 42"))
print(ends_with_number.search("Your number is forty-two.") is None)
