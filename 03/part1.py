import re

with open('input.txt') as f:
    lines = f.readlines()


def issymbol(c: str):
    return not c.isdigit() and c != '.'


def has_adjacent_symbol(line: str, line_no: int, start: int, end: int):
    if start > 0:
        if issymbol(line[start - 1]):
            return True
    if end < len(line):
        if issymbol(line[end]):
            return True
    for i in range(max(start - 1, 0), min(end + 1, len(line))):
        if line_no < len(lines) - 1 and issymbol(lines[line_no + 1][i]):
            return True
        if line_no > 0 and issymbol(lines[line_no - 1][i]):
            return True
    return False


sum_of_part_numbers = 0

for line_no, line in enumerate(lines):
    line = line.strip()
    for m in re.finditer(r'\d+', line):
        start, end = m.span()
        if has_adjacent_symbol(line, line_no, start, end):
            sum_of_part_numbers += int(m.group(0))

print(sum_of_part_numbers)
