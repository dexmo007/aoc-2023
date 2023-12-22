def unfold(arrangement, groups, n=5):
    return '?'.join([arrangement] * n), groups * n


records = []
with open('input.txt') as f:
    for line in f:
        partial_arrangement, groups = line.split(' ')
        groups = tuple(int(g) for g in groups.strip().split(','))
        records.append(unfold(partial_arrangement, groups))


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

# TODO possibly optimize the last group: needs to be where a # is but can connect to it any way possible, there can be 2,3, but they need to connect, if they cant the solution is not possible


def solve(arrangement: str, groups: list[int], start_from: int = 0):
    # print(arrangement, groups)
    if not groups:
        if '#' in arrangement[start_from:]:
            return
        yield arrangement.replace('?', '.')
        # print('solution above')
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
        # if i > start_from:
        #     new_arrangement += arrangement[:i - 1].replace('?', '.') + '.'
        new_arrangement += '#' * head
        if i + head < len(arrangement):
            new_arrangement += '.'
        new_arrangement += arrangement[i + head + 1:]
        yield from solve(new_arrangement, tail, i + head + 1)
        # print(i, possible_group)


# print_records()

index = 4
print(records[index])

solutions = list(solve(*records[index]))
# for s in solutions:
#     print(s)
print(len(solutions))

# result = sum(sum(1 for _ in solve(*record)) for record in records)
# print(result)
