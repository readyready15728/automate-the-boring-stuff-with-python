import re

consonant_pattern = re.compile(r"[^aeiouAEIOU]")
print(consonant_pattern.findall("RoboCop eats BABY FOOD."))
