import re

pattern = re.compile(r"\d{3}")
print(pattern.findall("1234"))
print(pattern.findall("12345"))
print(pattern.findall("123456"))
