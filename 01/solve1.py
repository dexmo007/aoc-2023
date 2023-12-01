with open('input.txt') as f:
    lines = f.readlines()


def parse():
    for line in lines:
        first, last = None, None
        for c in line:
            if not c.isdigit():
                continue
            if first is None:
                first = c
            last = c
        yield int(first + last)


print(sum(parse()))
