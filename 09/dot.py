import re

at_re = re.compile(r".at")
print(at_re.findall("The cat in the hat sat on the flat mat."))
