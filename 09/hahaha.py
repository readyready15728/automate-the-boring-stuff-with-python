import re

ha_regex = re.compile(r"(Ha){3}")
print(ha_regex.search("HaHaHa"))
print(ha_regex.search("HaHa"))
