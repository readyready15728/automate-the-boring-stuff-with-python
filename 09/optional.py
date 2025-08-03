import re

pattern = re.compile(r"42!?")
print(pattern.search("42!"))
print(pattern.search("42"))
