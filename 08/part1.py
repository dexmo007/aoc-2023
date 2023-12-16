import re

nodes = {}

with open('input.txt') as f:
    instructions = [0 if instr == 'L' else 1 for instr in next(f).strip()]
    next(f)
    for line in f:
        m = re.match(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line.strip())
        node, left, right = m.groups()
        nodes[node] = (left, right)

steps = 0
position = 'AAA'

while position != 'ZZZ':
    instr = instructions[steps % len(instructions)]
    position = nodes[position][instr]
    steps += 1

print(steps)
