import math

with open('input.txt') as f:
    lines = f.readlines()

sum_of_powers_of_sets = 0

for line in lines:
    rounds_raw = line.split(':')[1]
    min_required_cubes = {c: 0 for c in ('blue', 'red', 'green')}
    for round_raw in rounds_raw.split(';'):
        for draw in round_raw.split(','):
            cube_count, cube_color = draw.strip().split(' ')
            cube_count = int(cube_count)
            min_required_cubes[cube_color] = max(
                min_required_cubes[cube_color], cube_count)
    sum_of_powers_of_sets += math.prod(min_required_cubes.values())

print(sum_of_powers_of_sets)
