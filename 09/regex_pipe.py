import re

pattern = re.compile(r"Cat(erpillar|astrophe|ch|egory)")
match = pattern.search("Catch me if you can.")

print(match.group())
print(match.group(1))
