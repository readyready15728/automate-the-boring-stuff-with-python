import re

pattern = re.compile(r"(\d{3}-)?\d{3}-\d{4}")
match1 = pattern.search("My number is 415-555-4242")
print(match1.group())
match2 = pattern.search("My number is 555-4242")
print(match2.group())
