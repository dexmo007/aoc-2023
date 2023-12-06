import re

with open('input.txt') as f:
    lines = f.readlines()


def find_adjacent_gears(line: str, line_no: int, start: int, end: int):
    if start > 0:
        if line[start - 1] == '*':
            yield (line_no, start - 1)
    if end < len(line):
        if line[end] == '*':
            yield (line_no, end)
    for i in range(max(start - 1, 0), min(end + 1, len(line))):
        if line_no < len(lines) - 1 and lines[line_no + 1][i] == '*':
            yield (line_no + 1, i)
        if line_no > 0 and lines[line_no - 1][i] == '*':
            yield (line_no - 1, i)


gears = {}

for line_no, line in enumerate(lines):
    line = line.strip()
    for m in re.finditer(r'\d+', line):
        start, end = m.span()
        for gear in find_adjacent_gears(line, line_no, start, end):
            parts = gears.get(gear, [])
            parts.append(m.group(0))
            gears[gear] = parts

sum_of_gear_ratios = sum((int(parts[0]) * int(parts[1])
                         for parts in gears.values() if len(parts) == 2))

print(sum_of_gear_ratios)
