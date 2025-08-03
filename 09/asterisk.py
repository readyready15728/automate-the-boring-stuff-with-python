import re

pattern = re.compile(r"Eggs( and spam)*")
print(pattern.search("Eggs"))
print(pattern.search("Eggs and spam"))
print(pattern.search("Eggs and spam and spam"))
print(pattern.search("Eggs and spam and spam and spam"))
