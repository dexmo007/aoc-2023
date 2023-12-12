def parse(line: str):
    return list(map(int, line.split(':')[1].strip().split()))


with open('input.txt') as f:
    times = parse(next(f))
    record_distances = parse(next(f))
    races = list(zip(times, record_distances))

result = 1

for time, record_distance in races:
    winning_ways = 0
    for t in range(1, time - 1):
        speed = t
        distance = speed * (time - t)
        if distance > record_distance:
            winning_ways += 1
    result *= winning_ways

print(result)
