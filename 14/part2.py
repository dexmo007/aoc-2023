
platform = []

with open('input.txt') as f:
    for line in f:
        platform.append(list(line.strip()))


def print_platform():
    for row in platform:
        print(''.join(row))


def roll(y, x, dy, dx):
    if x + dx < 0 or x + dx >= len(platform[0]):
        return
    if y + dy < 0 or y + dy >= len(platform):
        return
    if platform[y + dy][x + dx] != '.':
        return
    platform[y + dy][x + dx] = 'O'
    platform[y][x] = '.'
    roll(y + dy, x + dx, dy, dx)


def tilt(dy, dx, y_iter, x_iter):
    for y in y_iter:
        for x in x_iter:
            if platform[y][x] != 'O':
                continue
            roll(y, x, dy, dx)


y_len = len(platform)
x_len = len(platform[0])


def cycle():
    tilt(-1, 0, range(y_len), range(x_len))
    tilt(0, -1, range(y_len), range(x_len))
    tilt(1, 0, range(y_len - 1, -1, -1), range(x_len))
    tilt(0, 1, range(y_len), range(x_len - 1, -1, -1))


def get_hash():
    return hash('\n'.join(''.join(row)
                          for row in platform))


def get_load():
    total_load = 0
    for y, row in enumerate(platform):
        for c in row:
            if c != 'O':
                continue
            total_load += len(platform) - y
    return total_load


cycles = {}
loads = []
periodically_after = None
period_length = None
num_cycles = 1_000_000_000
for i in range(num_cycles):
    cycle()
    h = get_hash()
    if h in cycles:
        periodically_after = cycles[h]
        period_length = i - cycles[h]
        break
    cycles[h] = i
    loads.append(get_load())


normalized_i = ((num_cycles - 1) - periodically_after) % period_length

load = loads[periodically_after + normalized_i]

print(load)
