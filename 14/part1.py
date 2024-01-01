
platform = []

with open('input.txt') as f:
    for line in f:
        platform.append(list(line.strip()))


def print_platform():
    for row in platform:
        print(''.join(row))


# print_platform()


def roll_north(y, x):
    if y == 0 or platform[y - 1][x] != '.':
        return
    platform[y - 1][x] = 'O'
    platform[y][x] = '.'
    roll_north(y - 1, x)


for y in range(1, len(platform)):
    for x in range(len(platform[y])):
        current = platform[y][x]
        if current != 'O':
            continue
        roll_north(y, x)

# print()
# print_platform()

total_load = 0

for y, row in enumerate(platform):
    for c in row:
        if c != 'O':
            continue
        total_load += len(platform) - y

print(total_load)
