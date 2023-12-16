import math
import re

nodes: dict[str, tuple[str, str]] = {}

with open('input.txt') as f:
    instructions = [0 if instr == 'L' else 1 for instr in next(f).strip()]
    next(f)
    for line in f:
        m = re.match(
            r'([A-Z\d]{3}) = \(([A-Z\d]{3}), ([A-Z\d]{3})\)', line.strip())
        node, left, right = m.groups()
        nodes[node] = (left, right)

steps = 0

positions = [node for node in nodes.keys() if node.endswith('A')]

steps_to_find = list(range(len(positions)))

steps_to_z = [None] * len(positions)

while steps_to_find:
    instr = instructions[steps % len(instructions)]
    steps += 1
    next_steps_to_find = []
    for i in steps_to_find:
        next_node = nodes[positions[i]][instr]
        if next_node.endswith('Z'):
            steps_to_z[i] = steps
            continue
        positions[i] = next_node
        next_steps_to_find.append(i)
    steps_to_find = next_steps_to_find


result = math.lcm(*steps_to_z)

print(result)
