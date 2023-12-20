records = []
with open('input.txt') as f:
    for line in f:
        partial_arrangement, groups = line.split(' ')
        groups = tuple(int(g) for g in groups.strip().split(','))
        records.append((partial_arrangement, groups))


def print_records():
    for arrangement, groups in records:
        print(arrangement, ','.join(map(str, groups)))


def nth_wise(it, n):
    it = iter(it)
    n_tuple = [None]
    try:
        for _ in range(n - 1):
            n_tuple.append(next(it))
    except StopIteration:
        return
    for i, e in enumerate(it):
        n_tuple.pop(0)
        n_tuple.append(e)
        yield (i, n_tuple)


def solve(arrangement: str, groups: list[int], start_from: int = 0):
    if not groups:
        if '#' in arrangement[start_from:]:
            return
        yield arrangement.replace('?', '.')
        return
    head, *tail = groups
    for i, possible_group in nth_wise(arrangement[start_from:], head):
        i = start_from + i
        if '.' in possible_group:
            continue
        if i > 0 and (arrangement[i - 1] == '#' or '#' in arrangement[start_from:i]):
            continue
        if i + head < len(arrangement) and arrangement[i + head] == '#':
            continue
        new_arrangement = arrangement[:i].replace('?', '.')
        new_arrangement += '#' * head
        if i + head < len(arrangement):
            new_arrangement += '.'
        new_arrangement += arrangement[i + head + 1:]
        yield from solve(new_arrangement, tail, i + head + 1)


result = sum(sum(1 for _ in solve(*record)) for record in records)
print(result)
