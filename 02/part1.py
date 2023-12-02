import re

with open('input.txt') as f:
    lines = f.readlines()

max_cubes = {'red': 12, 'green': 13, 'blue': 14}

possible_game_id_sum = 0

for line in lines:
    m = re.match(r'^Game (\d+): (.*)$', line)
    game_id, rounds_raw = m.groups()
    game_id = int(game_id)
    try:
        for round_raw in rounds_raw.split(';'):
            for draw in round_raw.split(','):
                # print(draw.strip())
                # print('======')
                cube_count, cube_color = draw.strip().split(' ')
                cube_count = int(cube_count)
                if cube_count > max_cubes[cube_color]:
                    raise StopIteration
        possible_game_id_sum += game_id
    except StopIteration:
        pass

print(possible_game_id_sum)
