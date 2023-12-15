from collections import Counter
import functools

ORDER = list(reversed(['A', 'K', 'Q', 'T', '9',
             '8', '7', '6', '5', '4', '3', '2', 'J']))

with open('input.txt') as f:
    hands = []
    for line in f:
        hand, bid = line.strip().split()
        hand = list(hand)
        bid = int(bid)
        hands.append((hand, bid))

FIVE_OF_KIND = 500
FOUR_OF_KIND = 400
FULL_HOUSE = 350
THREE_OF_KIND = 300
TWO_PAIR = 200
ONE_PAIR = 100
HIGH_CARD = 0


def score(hand: list[str]):
    occurences = [c for _, c in Counter(
        card for card in hand if card != 'J').most_common()]
    jokers = hand.count('J')
    card_values = [ORDER.index(card) for card in hand]

    def calc_type():
        if jokers == 5:
            return FIVE_OF_KIND
        first, *rest = occurences
        if first + jokers == 5:
            return FIVE_OF_KIND
        if first + jokers == 4:
            return FOUR_OF_KIND
        second, *rest = rest
        if first + jokers == 3:
            if second == 2:
                return FULL_HOUSE
            return THREE_OF_KIND
        if first + jokers == 2:
            if second == 2:
                return TWO_PAIR
            return ONE_PAIR
        return HIGH_CARD
    return calc_type(), card_values


def compare(left, right):
    *_, (left_type, left_values) = left
    *_, (right_type, right_values) = right
    if left_type != right_type:
        return left_type - right_type
    for l, r in zip(left_values, right_values):
        if l != r:
            return l - r
    return 0


scored_hands = [(hand, bid, score(hand)) for hand, bid in hands]


ordered_hands = sorted(scored_hands, key=functools.cmp_to_key(compare))

total_winning = sum((i+1)*bid for i, (_, bid, _)
                    in enumerate(ordered_hands))

print(total_winning)
