import re

lazy_pattern = re.compile(r"<.*?>")
print(lazy_pattern.search("<To serve man> for dinner.>"))

greedy_re = re.compile(r"<.*>")
print(greedy_re.search("<To serve man> for dinner.>"))
