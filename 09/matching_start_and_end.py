import re

whole_string_is_num = re.compile(r"^\d+$")
print(whole_string_is_num.search("1234567890"))
print(whole_string_is_num.search("12345xyz67890") is None)
