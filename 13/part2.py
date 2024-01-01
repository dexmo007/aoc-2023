
patterns = [[]]

with open('input.txt') as f:
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


def get_diff_count(s1, s2):
    diff_count = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diff_count += 1
    return diff_count


def is_reflection(pattern, i, n_smudges):
    if i >= len(pattern) - 1:
        return False
    d_max = min(i, len(pattern) - i - 2) + 1
    mismatch_count = 0
    for d in range(d_max):
        mismatch_count += get_diff_count(pattern[i - d], pattern[i + 1 + d])
        if mismatch_count > n_smudges:
            return False
    return mismatch_count == n_smudges


def find_reflection(pattern, n_smudges=1):
    for i, _ in enumerate(pattern):
        # print(i, is_reflection(pattern, i))
        if is_reflection(pattern, i, n_smudges):
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
