import re

initialization_sequence = []

with open('input.txt') as f:
    for line in f:
        initialization_sequence.extend(line.strip().split(','))


def holiday_hash(s: str) -> int:
    current = 0
    for c in s:
        current = ((current + ord(c)) * 17) % 256
    return current


boxes = [{} for _ in range(256)]


def HASHMAP():
    for step in initialization_sequence:
        # equals operation
        m = re.match(r'([a-z]+)=(\d+)', step)
        if m:
            label, focal_length = m.groups()
            boxes[holiday_hash(label)][label] = int(focal_length)
            continue
        # dash operation
        m = re.match(r'([a-z]+)-', step)
        if m:
            label = m.group(1)
            boxes[holiday_hash(label)].pop(label, None)
            continue
        raise ValueError('invalid operation')


def get_focusing_power():
    focusing_power = 0
    for box_i, box in enumerate(boxes):
        for slot, focal_length in enumerate(box.values()):
            focusing_power += (box_i + 1) * (slot + 1) * focal_length
    return focusing_power


HASHMAP()


print(get_focusing_power())
