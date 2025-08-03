import re

name_pattern = re.compile(r"First Name: (.*) Last Name: (.*)")
name_match = name_pattern.search("First Name: Al Last Name: Sweigart")
print(name_match.group(1))
print(name_match.group(2))
