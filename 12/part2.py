import heapq

def unfold(arrangement, groups, n=1):
    return '?'.join([arrangement] * n), groups * n

def read_input(file: str, unfold_n: int = 5):
    records = []
    with open(file) as f:
        for line in f:
            partial_arrangement, groups = line.split(' ')
            groups = tuple(int(g) for g in groups.strip().split(','))
            records.append(unfold(partial_arrangement, groups, unfold_n))
    return records


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

solve_count = 0

def solve(arrangement: str, groups: list[int], start_from: int = 0):
    global solve_count
    solve_count += 1
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

def _hash(item):
    start_from, groups, base_count = item
    return hash((start_from, *groups, base_count))

def heappop(pq: tuple[list, dict]):
    heap, d = pq
    item = heapq.heappop(heap)
    count = d.pop(_hash(item))
    return item, count

def heappush(pq, item, count=1):
    heap, d = pq
    item_hash = _hash(item)
    if item_hash in d:
        d[item_hash] += 1
        return
    heapq.heappush(heap, item)
    d[item_hash] = count

solve_opt_count = 0
def solve_opt(arrangement: str, groups: list[int]):
    global solve_opt_count

    solutions = 0
    pq = [], {}
    heappush(pq, ( 0, groups, 1))

    while pq[0]:
        solve_opt_count += 1
        (start_from, groups, base_count), count = heappop(pq)
        count = base_count * count
        head, *tail = groups
        next_fixed = arrangement[start_from:].find('#')
        if next_fixed == -1:
            possible_range = arrangement[start_from:]
        else:
            possible_range = arrangement[start_from:start_from + next_fixed + head] # todo evtl count last group
        for i, possible_group in nth_wise(possible_range, head):
            i = start_from + i
            if '.' in possible_group:
                continue
            if i > 0 and (arrangement[i - 1] == '#' ): # or '#' in arrangement[start_from:i]
                continue
            if i + head < len(arrangement) and arrangement[i + head] == '#':
                continue
            if len(arrangement) - i - head < sum(tail) + len(tail) :
                continue
            if not tail:
                if '#' in arrangement[i + head + 1:]:
                    continue
                solutions += count
                continue
            heappush(pq, (  i + head + 1, tail, count))
        #if solve_opt_count >= 8:
        #    break
    #for s in pq[0]:
    #    print(s)
    return solutions

# print_records()
import time

records = read_input('input.txt', unfold_n=5)

index = 0
print(records[index])

#start = time.time()
#solutions = list(solve(*records[index]))
#duration = time.time() - start
#print('old', duration)
#print('solve_count', solve_count)
# for s in solutions:
#     print(s)
#print(len(solutions))

# start = time.time()
# solutions = solve_opt(*records[index])
# duration = time.time() - start
# print('opt', duration)
# print('solve_opt_count', solve_opt_count)
# print(solutions)

# result = sum(sum(1 for _ in solve(*record)) for record in records)
# print(result)
