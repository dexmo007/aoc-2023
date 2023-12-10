import re
with open('input.txt' ) as f:
  seeds = next(f)
  m = re.match(r'seeds: (\d+(?: \d+)*)', seeds)
  seeds = [int(s) for s in m.group(1).split()]
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
    dest_range_start, src_range_start, range_len = [int(s) for s in line.split()]
    maps[current_map[0]][1].append((dest_range_start, src_range_start, range_len))

def convert_value(value: int, src_category: str, dest_category: str):
  target_category, ranges = maps[src_category]
  for dest_range_start, src_range_start, range_len in ranges:
    if value >= src_range_start and value < src_range_start + range_len:
      converted = value - src_range_start + dest_range_start
      break
  else:
    converted = value
  if target_category == dest_category:
    return converted
  return convert_value(converted, target_category, dest_category)

min_location = min( convert_value(seed, 'seed', 'location') for seed in seeds)

print(min_location)
