cards = []

with open('input.txt') as f:
    for line in f:
        _, s = line.split(':')
        ws, hs = s.split('|')
        winning = [int(w) for w in ws.split()]
        hand = [int(w) for w in hs.split()]
        cards.append((winning, hand))


total_scratchcards = 0
carryover = [1 for _ in range(max((len(winning) for winning, _ in cards)))]

for winning, hand in cards:
    n_current = carryover.pop(0)
    total_scratchcards += n_current
    carryover.append(1)
    c = 0
    for n in hand:
        if n not in winning:
            continue
        carryover[c] += n_current
        c += 1

print(total_scratchcards)
