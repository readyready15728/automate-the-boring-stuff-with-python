import re

agent_pattern = re.compile(r"Agent \w+")
print(agent_pattern.sub("CENSORED", "Agent Alice contacted Agent Bob."))
