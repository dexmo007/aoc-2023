import os

current_day = max(int(d) for d in next(os.walk('.'))[1] if d != '.git')

next_day = f'{current_day+1:02d}'

os.mkdir(next_day)

with open(f'{next_day}/sample.txt', 'w'):
    pass
with open(f'{next_day}/input.txt', 'w'):
    pass
with open(f'{next_day}/part1.py', 'w') as f:
    f.write("""
with open('sample.txt') as f:
    for line in f:
        pass
""")
