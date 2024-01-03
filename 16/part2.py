
grid = []

with open('input.txt') as f:
    for line in f:
        grid.append(line.strip())


def get_next_beam_directions(y, x, dy, dx):
    if y < 0 or y >= len(grid):
        return
    if x < 0 or x >= len(grid[y]):
        return
    tile = grid[y][x]
    if tile == '\\':
        yield (dx, dy)
        return
    if tile == '/':
        yield (-dx, -dy)
        return
    if tile == '|' and dx != 0:
        yield (-1, 0)
        yield (1, 0)
        return
    if tile == '-' and dy != 0:
        yield (0, -1)
        yield (0, 1)
        return
    yield (dy, dx)


def energize(start, direction):
    queue = [(start, d) for d in get_next_beam_directions(*start, *direction)]
    beam = set()

    while queue:
        (oy, ox), (dy, dx) = queue.pop()
        if ((oy, ox), (dy, dx)) in beam:
            continue
        beam.add(((oy, ox), (dy, dx)))
        y, x = oy + dy, ox + dx
        for new_dy, new_dx in get_next_beam_directions(y, x, dy, dx):
            queue.append(((y, x), (new_dy, new_dx)))

    return len(set(pos for pos, _ in beam))


def energize_all():
    for x in range(len(grid[0])):
        yield energize((0, x), (1, 0))
        yield energize((len(grid) - 1, x), (-1, 0))
    for y in range(len(grid)):
        yield energize((y, 0), (0, 1))
        yield energize((y, len(grid[y]) - 1), (0, -1))


max_energized = max(energize_all())

print(max_energized)
