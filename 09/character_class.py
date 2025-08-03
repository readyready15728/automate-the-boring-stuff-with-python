import re

vowel_pattern = re.compile(r"[aeiouAEIOU]")
print(vowel_pattern.findall("Robocop eats BABY FOOD."))
