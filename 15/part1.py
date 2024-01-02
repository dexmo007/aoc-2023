initialization_sequence = []

with open('input.txt') as f:
    for line in f:
        initialization_sequence.extend(line.strip().split(','))


def holiday_hash(s: str) -> int:
    current = 0
    for c in s:
        current += ord(c)
        current *= 17
        current %= 256
    return current


result = sum(holiday_hash(step) for step in initialization_sequence)

print(result)
