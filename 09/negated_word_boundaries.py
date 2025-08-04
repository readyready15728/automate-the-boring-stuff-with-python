import re

pattern = re.compile(r"\Bcat\B")
print(pattern.findall("certificate"))
print(pattern.findall("catastrophe"))
