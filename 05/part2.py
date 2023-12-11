import re
import math

with open('input.txt') as f:
    seeds = next(f)
    m = re.match(r'seeds:((?: \d+ \d+)+)', seeds)
    seeds = (int(s) for s in m.group(1).split())
    seeds = list(zip(seeds, seeds))

    current_map = None
    maps = {}
    for line in f:
        line = line.strip()
        if not line:
            current_map = None
            continue
        if not current_map:
            m = re.match(r'([a-z]+)-to-([a-z]+) map:', line)
            src, dest = m.groups()
            current_map = (src, dest)
            maps[src] = (dest, [])
            continue
        dest_range_start, src_range_start, range_len = [
            int(s) for s in line.split()]
        maps[current_map[0]][1].append(
            (src_range_start, src_range_start + range_len - 1, dest_range_start - src_range_start))

# fill 0 to first range, last range to inf and holes within the ranges for each conversion
for src, (dest, ranges) in maps.items():
    min_start = min(start for start, _, _ in ranges)
    max_end = max(end for _, end, _ in ranges)
    prev = None
    holes_to_fill = []
    for start, end, delta in sorted(ranges, key=lambda r: r[0]):
        if prev is None:
            prev = start, end, delta
            continue
        if prev[1] < start - 1:
            print('Found hole', src, dest, prev[1], start)
            holes_to_fill.append((prev[1] + 1, start - 1, 0))
        prev = start, end, delta
    ranges.extend(holes_to_fill)
    if min_start > 0:
        ranges.append((0, min_start - 1, 0))
    ranges.append((max_end + 1, math.inf, 0))


def coalesce(r1, r2):
    start1, end1, delta1 = r1
    start2, end2, delta2 = r2
    if start1 + delta1 > end2 or end1 + delta1 < start2:
        return None
    return (max(start1 + delta1, start2) - delta1, min(end1 + delta1, end2) - delta1, delta1 + delta2)


def coalesce_all(rs1, rs2):
    for r1 in rs1:
        for r2 in rs2:
            nr = coalesce(r1, r2)
            if nr is not None:
                yield nr


# coalesce all conversions into a single mapping
origin = 'seed'
next_category, coalesced_ranges = maps[origin]


while True:
    next_next_category, rs2 = maps[next_category]

    coalesced_ranges = list(coalesce_all(coalesced_ranges, rs2))
    if next_next_category == 'location':
        break
    next_category = next_next_category


def convert_value_fast(value: int):
    for start, end, delta in coalesced_ranges:
        if value >= start and value <= end:
            return value + delta
    raise ValueError(f'must have a match for {value}')


seed_ranges = [(seed_start, seed_start + span - 1)
               for seed_start, span in seeds]

# get all possible location value ranges from input seeds


def process():
    for seed_start, seed_end in seed_ranges:
        for start, end, delta in coalesced_ranges:
            if seed_start > end or seed_end < start:
                continue
            yield (max(seed_start, start), min(seed_end, end), delta)


print('===== RESULTS ======')

results = list(process())

for start, end, delta in sorted(results, key=lambda x: x[0]):
    print(f'{start:,} {end:,} {delta:,}')

# minimun start value plus delta is lowest possible location number
print('====== LOWEST LOCATION NUMBER ========')
lowest_location = min(start + delta for start, _, delta in results)
print(lowest_location)
