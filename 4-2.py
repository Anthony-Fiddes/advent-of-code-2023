import fileinput
from collections import Counter
from dataclasses import dataclass


@dataclass
class Card:
    winning_nums: set[int]
    card_nums: set[int]

    def matching_nums_count(self) -> int:
        return len(self.winning_nums & self.card_nums)


cards = []
for line in fileinput.input():
    numbers_string = line.split(":")[1]
    number_sets = numbers_string.split("|")
    winning_nums_str = number_sets[0].strip()
    winning_nums = {int(x) for x in winning_nums_str.split()}
    card_nums_str = number_sets[1].strip()
    card_nums = {int(x) for x in card_nums_str.split()}
    card = Card(winning_nums, card_nums)
    cards.append(card)

card_counts = Counter()
for i, card in enumerate(cards):
    # The original card
    card_counts[i] += 1
    curr_card_count = card_counts[i]
    for j in range(i + 1, i + 1 + card.matching_nums_count()):
        # You get one copy of the new card per copy you have of the card
        # generating it
        card_counts[j] += curr_card_count

print(f"Result: {card_counts.total()}")
