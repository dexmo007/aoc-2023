import math


def parse(line: str):
    return int(line.split(':')[1].replace(' ', ''))


with open('input.txt') as f:
    time = parse(next(f))
    record_distance = parse(next(f))


def find_record_t(T, dr):
    return (math.floor(1 + T/2 - math.sqrt(T**2/4-dr)), math.ceil(T/2 + math.sqrt(T**2/4-dr) - 1))


min_wait, max_wait = find_record_t(time, record_distance)

winning_ways = max_wait - min_wait + 1


print(winning_ways)
