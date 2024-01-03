
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


# starting in the top left heading to the right
queue = [((0, 0), d) for d in get_next_beam_directions(0, 0, 0, 1)]
beam = set()

while queue:
    (oy, ox), (dy, dx) = queue.pop()
    if ((oy, ox), (dy, dx)) in beam:
        continue
    beam.add(((oy, ox), (dy, dx)))
    y, x = oy + dy, ox + dx
    for new_dy, new_dx in get_next_beam_directions(y, x, dy, dx):
        queue.append(((y, x), (new_dy, new_dx)))


print(len(set(pos for pos, _ in beam)))
