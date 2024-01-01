
patterns = [[]]

with open('sample.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            patterns.append([])
            continue
        patterns[-1].append(line)

# print(patterns)


def transpose(array):
    transposed = [[] for _ in range(len(array[0]))]
    for row in array:
        for i, c in enumerate(row):
            transposed[i].append(c)
    return transposed


def is_reflection(pattern, i):
    if i >= len(pattern) - 1:
        return False
    d_max = min(i, len(pattern) - i - 2) + 1
    for d in range(d_max):
        if pattern[i - d] != pattern[i + 1 + d]:
            return False
    return True


def find_reflection(pattern):
    for i, _ in enumerate(pattern):
        # print(i, is_reflection(pattern, i))
        if is_reflection(pattern, i):
            return i
    return None


result = 0
for pattern in patterns:
    r = find_reflection(pattern)
    if r is not None:
        result += 100 * (r+1)
        continue
    r = find_reflection(transpose(pattern))
    if r is not None:
        result += r+1

print(result)
