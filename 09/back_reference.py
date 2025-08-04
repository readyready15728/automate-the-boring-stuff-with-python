import re

agent_pattern = re.compile(r"Agent (\w)\w*")
print(agent_pattern.sub(r"\1****", "Agent Alice contacted Agent Bob."))
