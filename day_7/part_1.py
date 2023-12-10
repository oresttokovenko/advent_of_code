from collections import Counter
from dataclasses import dataclass, field

with open("input.txt", "r") as f:
    input = [i.strip("\n") for i in f.readlines()]

winnings = 0

hand_rankings = {
    "high_card": 1,
    "one_pair": 2,
    "two_pair": 3,
    "three_of_a_kind": 4,
    "full_house": 5,
    "four_of_a_kind": 6,
    "five_of_a_kind": 7,
}

card_rankings = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}


@dataclass
class CamelCard:
    hand: str
    bid: int
    rank: int = None
    type: str = field(init=False)
    hand_labels: Counter = field(init=False)

    def __post_init__(self):
        self.hand_labels = Counter(self.hand)
        self.hand_type()

    def hand_type(self):
        if 5 in self.hand_labels.values():
            self.type = "five_of_a_kind"
        elif 4 in self.hand_labels.values():
            self.type = "four_of_a_kind"
        elif 3 in self.hand_labels.values() and 2 in self.hand_labels.values():
            self.type = "full_house"
        elif 3 in self.hand_labels.values() and 1 in self.hand_labels.values():
            self.type = "three_of_a_kind"
        elif list(self.hand_labels.values()).count(2) == 2:
            self.type = "two_pair"
        elif 2 in self.hand_labels.values() and 1 in self.hand_labels.values():
            self.type = "one_pair"
        else:
            self.type = "high_card"


# instantiating a list of CamelCards, assigning arbitrary ranking for bubble sort
list_of_hands = [
    CamelCard(hand=pair[0], bid=int(pair[1]), rank=idx)
    for idx, i in enumerate(input, start=1)
    for pair in zip(i.split()[::2], i.split()[1::2])
]

n = len(list_of_hands)

for i in range(n):
    for j in range(0, n - i - 1):
        # comparing based on the hand type ranking
        if (
            hand_rankings[list_of_hands[j].type]
            < hand_rankings[list_of_hands[j + 1].type]
        ):
            list_of_hands[j], list_of_hands[j + 1] = (
                list_of_hands[j + 1],
                list_of_hands[j],
            )
            # swapping ranks as well
            list_of_hands[j].rank, list_of_hands[j + 1].rank = (
                list_of_hands[j + 1].rank,
                list_of_hands[j].rank,
            )
        # comparing based on the card rankings if hand type ranking is same
        elif (
            hand_rankings[list_of_hands[j].type]
            == hand_rankings[list_of_hands[j + 1].type]
        ):
            card_a = [
                card_rankings[i] if i in card_rankings else int(i)
                for i in list_of_hands[j].hand
            ]
            card_b = [
                card_rankings[i] if i in card_rankings else int(i)
                for i in list_of_hands[j + 1].hand
            ]
            for ii, jj in zip(card_a, card_b):
                if ii < jj:
                    list_of_hands[j], list_of_hands[j + 1] = (
                        list_of_hands[j + 1],
                        list_of_hands[j],
                    )
                    # swapping ranks as well
                    list_of_hands[j].rank, list_of_hands[j + 1].rank = (
                        list_of_hands[j + 1].rank,
                        list_of_hands[j].rank,
                    )
                    break
                elif ii > jj:
                    break

# assigning ranks from 5 down to 1
for idx, card in enumerate(list_of_hands):
    card.rank = n - idx

for i in list_of_hands:
    product = i.bid * i.rank
    winnings += product

print(winnings)
