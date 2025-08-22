from pathlib import Path

p = Path("spam.txt")
p.write_text("Hello, world!")
print(p.read_text())
