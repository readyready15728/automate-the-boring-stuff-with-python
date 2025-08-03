import re

no_newline_re = re.compile(r".*")
print(
    no_newline_re.search(
        "Serve the public trust.\nProtect the innocent.\nUphold the law."
    )
)
newline_re = re.compile(r".*", re.DOTALL)
print(
    newline_re.search("Serve the public trust.\nProtect the innocent.\nUphold the law.")
)
