import re

greedy_pattern = re.compile(r"(Ha){3,5}")
print(greedy_pattern.search("HaHaHaHaHa"))

lazy_pattern = re.compile(r"(Ha){3,5}?")
print(lazy_pattern.search("HaHaHaHaHa"))
