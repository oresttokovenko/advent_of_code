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
    "five_of_a_kind": 7
}

card_rankings = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    'J': 1
}

@dataclass
class CamelCard:
    hand: str
    original_hand: str
    bid: int
    rank: int = None
    type: str = field(init=False)
    original_hand_labels: Counter = field(init=False)
    hand_labels: Counter = field(init=False)

    def __post_init__(self):
        """
        1. initializing a Counter for the original hand to keep track of card frequencies,
           including jokers. This is stored in original_hand_labels

        2. calling the joker_replace method to replace any jokers in the hand with 
           the most frequent card found in the original hand. This step is intended to 
           strengthen the hand by replacing jokers with the most advantageous card

        3. reinitializing the hand_labels Counter for the modified hand (post joker replacement) 
           for accurate frequency tracking of the current hand composition

        4. initializing the hand type based on the current hand composition by calling 
           the hand_type method. This sets the type attribute, categorizing the hand 
           according to the rules of the game
        """
        self.original_hand_labels = Counter(self.original_hand)
        self.joker_replace()
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

    def joker_replace(self):
        # fetching the element with the highest count, second highest count if J is highest
        if self.original_hand_labels.most_common(1)[0][0] != "J":
            highest_card = self.original_hand_labels.most_common(1)[0][0]
        else: 
            try:
                highest_card = self.original_hand_labels.most_common(2)[1][0]
            # addressing edge case where each card is a J
            except IndexError:
                highest_card = "J"
        self.hand = self.original_hand.replace("J", highest_card)

# instantiating a list of CamelCards, assigning arbitrary ranking for bubble sort
list_of_hands = [
    CamelCard(original_hand=pair[0], hand=pair[0], bid=int(pair[1]), rank=idx)
    for idx, i in enumerate(input, start=1)
    for pair in zip(i.split()[::2], i.split()[1::2])
]

# print(list_of_hands[1])

n = len(list_of_hands)

for i in range(n):
    for j in range(0, n-i-1):
        # comparing based on the hand type ranking
        if hand_rankings[list_of_hands[j].type] < hand_rankings[list_of_hands[j+1].type]:
            list_of_hands[j], list_of_hands[j+1] = list_of_hands[j+1], list_of_hands[j]
            # swapping ranks as well
            list_of_hands[j].rank, list_of_hands[j+1].rank = list_of_hands[j+1].rank, list_of_hands[j].rank
        # comparing based on the card rankings if hand type ranking is same
        elif hand_rankings[list_of_hands[j].type] == hand_rankings[list_of_hands[j+1].type]:
            card_a = [card_rankings[i] if i in card_rankings else int(i) for i in list_of_hands[j].original_hand]
            card_b = [card_rankings[i] if i in card_rankings else int(i) for i in list_of_hands[j+1].original_hand]
            for ii, jj in zip(card_a, card_b):
                if ii < jj:
                    list_of_hands[j], list_of_hands[j+1] = list_of_hands[j+1], list_of_hands[j]
                    # swapping ranks as well
                    list_of_hands[j].rank, list_of_hands[j+1].rank = list_of_hands[j+1].rank, list_of_hands[j].rank
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
