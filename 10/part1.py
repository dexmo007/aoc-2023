
with open('input.txt') as f:
    field = [list(line.strip()) for line in f]

NORTH = (-1, 0)
SOUTH = (1, 0)
WEST = (0, -1)
EAST = (0, 1)

PIPES = {
    '|': (NORTH, SOUTH),
    '-': (WEST, EAST),
    'L': (NORTH, EAST),
    'J': (NORTH, WEST),
    '7': (SOUTH, WEST),
    'F': (SOUTH, EAST),
}


def determine_start_pipe_type(y, x):
    connections = [(dy, dx) for dy, dx in (NORTH, EAST, SOUTH, WEST) if y + dy >= 0 and x + dx >=
                   0 and y+dy < len(field) and x+dx < len(field[y + dy]) and field[y+dy][x+dx] != '.' and (-dy, -dx) in PIPES[field[y+dy][x+dx]]]
    for pipe_symbol, cons in PIPES.items():
        if all(c in cons for c in connections):
            return pipe_symbol
    raise ValueError('start tile pipe type invalid')


def find_and_replace_start():
    for y, row in enumerate(field):
        for x, tile in enumerate(row):
            if tile == 'S':
                field[y][x] = determine_start_pipe_type(y, x)
                return y, x
    raise ValueError('start not found')


start = find_and_replace_start()

# print('\n'.join(''.join(row) for row in field))


distance = 0
positions = [(start, None)]

while True:
    next_positions = []
    for (y, x), came_from in positions:
        (dy1, dx1), (dy2, dx2) = PIPES[field[y][x]]
        if came_from is None or (y + dy1, x + dx1) != came_from:
            next_positions.append(((y + dy1, x + dx1), (y, x)))
        if came_from is None or (y + dy2, x + dx2) != came_from:
            next_positions.append(((y + dy2, x + dx2), (y, x)))
    distance += 1
    if len(next_positions) == 2 and next_positions[0][0] == next_positions[1][0]:
        break
    positions = next_positions
    # print(positions, len(next_positions), next_positions[0][0], next_positions[1][0], len(next_positions) ==
    #       2 and next_positions[0] == next_positions[1])

print(distance)
