import math


def parse(line: str):
    return list(map(int, line.split(':')[1].strip().split()))


with open('input.txt') as f:
    times = parse(next(f))
    record_distances = parse(next(f))
    races = list(zip(times, record_distances))

result = 1


def find_record_t(T, dr):
    return (math.floor(1 + T/2 - math.sqrt(T**2/4-dr)), math.ceil(T/2 + math.sqrt(T**2/4-dr) - 1))


for time, record_distance in races:
    min_wait, max_wait = find_record_t(time, record_distance)
    winning_ways = max_wait - min_wait + 1
    result *= winning_ways

print(result)
