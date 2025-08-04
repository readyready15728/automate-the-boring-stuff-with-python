import re

pattern = re.compile(r"robocop", re.I)
print(pattern.search("RoboCop is part man, part machine, all cop."))
print(pattern.search("ROBOCOP protects the innocent."))
print(pattern.search("Have you seen robocop?"))
