import itertools

with open('input.txt') as f:
    universe = [[1 if c == '.' else c for c in line.strip()] for line in f]


def print_universe():
    for row in universe:
        print(''.join(str('M' if c == 1_000_000 else c) for c in row))


def column_has_galaxy(col):
    for row in universe:
        if row[col] == '#':
            return True
    return False


def expand_universe(age=1_000_000):
    for col in range(len(universe[0])):
        if column_has_galaxy(col):
            continue
        for row_index, row in enumerate(universe):
            universe[row_index][col] = age

    for row in universe:
        if '#' not in row:
            for col in range(len(row)):
                row[col] = age


def find_and_replace_galaxies():
    def _():
        for y, row in enumerate(universe):
            for x, space in enumerate(row):
                if space == '#':
                    row[x] = 1
                    yield (y, x)
    return list(_())


def shortest_path(g1, g2):
    y1, x1 = g1
    y2, x2 = g2
    start_y = min(y1, y2)
    start_x = min(x1, x2)
    end_y = max(y1, y2)
    end_x = max(x1, x2)
    path_length = sum(row[start_x] for row in universe[start_y+1:end_y+1])
    path_length += sum(universe[start_y][start_x + 1: end_x + 1])
    return path_length


expand_universe()

galaxies = find_and_replace_galaxies()

sum_of_shortest_paths = 0
for g1, g2 in itertools.combinations(galaxies, 2):
    sum_of_shortest_paths += shortest_path(g1, g2)

print(sum_of_shortest_paths)
