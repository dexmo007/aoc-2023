with open('input.txt') as f:
    lines = f.readlines()

digit_words = ('one', 'two', 'three', 'four', 'five',
               'six', 'seven', 'eight', 'nine')


def get_digit_by_word(buffer: str):
    for i, w in enumerate(digit_words):
        if buffer.endswith(w):
            return str(i+1)


def parse():
    for line in lines:
        first, last = None, None
        buffer = ''
        for c in line:
            buffer += c
            digit = None
            if c.isdigit():
                digit = c
            else:
                digit = get_digit_by_word(buffer)
            if not digit:
                continue
            if first is None:
                first = digit
            last = digit
        yield int(first + last)


print(sum(parse()))
