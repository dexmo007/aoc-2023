import itertools

with open('input.txt') as f:
    universe = [list(line.strip()) for line in f]


def print_universe():
    for row in universe:
        print(''.join(row))


def column_has_galaxy(col):
    for row in universe:
        if row[col] == '#':
            return True
    return False


def expand_universe():
    expanded = [[] for _ in universe]
    for col in range(len(universe[0])):
        expand_col = not column_has_galaxy(col)
        for row_index, row in enumerate(universe):
            expanded[row_index].append(universe[row_index][col])
            if expand_col:
                expanded[row_index].append('.')

    for row in expanded:
        if '#' not in row:
            yield row
        yield row


def find_galaxies():
    for y, row in enumerate(universe):
        for x, space in enumerate(row):
            if space == '#':
                yield (y, x)


def shortest_path(g1, g2):
    y1, x1 = g1
    y2, x2 = g2
    return abs(y1 - y2) + abs(x1 - x2)


universe = list(expand_universe())

galaxies = find_galaxies()

sum_of_shortest_paths = 0
for g1, g2 in itertools.combinations(galaxies, 2):
    sum_of_shortest_paths += shortest_path(g1, g2)

print(sum_of_shortest_paths)
