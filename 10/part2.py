
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

TL, T, TR = (-1, -1), (-1, 0), (-1, 1)
L, R = (0, -1), (0, 1)
BL, B, BR = (1, -1), (1, 0), (1, 1)

PIPE_ADJACENT = {
    '|': ((R,), (L,)),
    '-': ((T,), (B,)),
    'L': ((), (L, BL, B)),
    'J': ((R, BR, B), ()),
    '7': ((), (T, TR, R)),
    'F': ((L, TL, T), ()),
}


def within_bounds(y, x):
    return y >= 0 and y < len(field) and x >= 0 and x < len(field[y])


def get_adjacent_tiles(oy, ox):
    for dy, dx in ((0, -1), (-1, 0), (0, 1), (1, 0)):
        y = oy + dy
        x = ox + dx
        if within_bounds(y, x):
            yield (y, x)


def print_field(*, cursor: tuple[int, int] = None):
    print('=' * len(field[0]))
    print('\n'.join(''.join('C' if (y, x) == cursor else tile for x,
          tile in enumerate(row)) for y, row in enumerate(field)))
    print('=' * len(field[0]))


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


# find loop
positions = [(start, None)]
loop = set([start])

while True:
    next_positions = []
    for (y, x), came_from in positions:
        (dy1, dx1), (dy2, dx2) = PIPES[field[y][x]]
        if came_from is None or (y + dy1, x + dx1) != came_from:
            next_positions.append(((y + dy1, x + dx1), (y, x)))
            loop.add((y + dy1, x + dx1))
        if came_from is None or (y + dy2, x + dx2) != came_from:
            next_positions.append(((y + dy2, x + dx2), (y, x)))
            loop.add((y + dy2, x + dx2))
    if len(next_positions) == 2 and next_positions[0][0] == next_positions[1][0]:
        break
    positions = next_positions

# flood fill

start = next(iter(loop))
y, x = start
prev = None
while True:
    pa = PIPE_ADJACENT[field[y][x]]
    pipe = PIPES[field[y][x]]

    delta = pipe[0] if prev is None or (
        y + pipe[1][0], x + pipe[1][1]) == prev else pipe[1]
    d = pipe.index(delta)
    l = pa[d]
    r = pa[1 - d]
    for dy, dx in l:
        if within_bounds(y+dy, x+dx) and (y+dy, x+dx) not in loop:
            field[y+dy][x+dx] = '1'
    for dy, dx in r:
        if within_bounds(y+dy, x+dx) and (y+dy, x+dx) not in loop:
            field[y+dy][x+dx] = '2'
    prev = y, x
    y, x = y + delta[0], x + delta[1]
    if (y, x) == start:
        break


def fill(marker):
    cursor = [(y, x) for y, row in enumerate(field)
              for x, tile in enumerate(row) if tile == marker]
    while cursor:
        oy, ox = cursor.pop()
        for y, x in get_adjacent_tiles(oy, ox):
            if field[y][x] == marker:
                continue
            if (y, x) in loop:
                continue
            field[y][x] = marker
            cursor.append((y, x))


fill('1')
fill('2')


def find_outer_coordinate():
    for x in range(len(field[0])):
        if (0, x) not in loop:
            return 0, x
        if (len(field) - 1, x) not in loop:
            return (len(field) - 1, x)
    for y in range(1, len(field) - 1):
        if (y, 0) not in loop:
            return y, 0
        if (y, len(field[y]) - 1) not in loop:
            return (y, len(field[y]) - 1)
    return None


y, x = find_outer_coordinate()
outer_marker = field[y][x]
inner_marker = '1' if outer_marker == '2' else '2'
enclosed_tiles = sum(
    1 for row in field for tile in row if tile == inner_marker)
print(enclosed_tiles)
