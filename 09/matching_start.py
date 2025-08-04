import re

begins_with_hello = re.compile(r"^Hello")
print(begins_with_hello.search("Hello, world!"))
print(begins_with_hello.search('He said "Hello."') is None)
