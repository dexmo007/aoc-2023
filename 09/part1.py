import itertools

datasets = []

with open('input.txt') as f:
    for line in f:
        datasets.append([int(v) for v in line.split()])


def extrapolate(dataset: list[int]):
    deltas = [dataset]
    while True:
        delta = [b - a for a, b in itertools.pairwise(deltas[-1])]
        deltas.append(delta)
        if all(d == 0 for d in delta) or len(delta) == 1:
            break
    deltas[-1].append(0)
    for i, d in enumerate(reversed(deltas[:-1])):
        d.append(d[-1] + deltas[-i-1][-1])

    return deltas[0][-1]


result = sum(extrapolate(d) for d in datasets)
print(result)
