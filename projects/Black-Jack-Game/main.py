import random

class Deck:

    def __init__(self):
        suits = ["hearts", "spades", "clubs", "diamonds"]
        ranks = [
                {"rank": "A", "value": 11},
                {"rank": "2", "value": 2},
                {"rank": "3", "value": 3},
                {"rank": "4", "value": 4},
                {"rank": "5", "value": 5},
                {"rank": "6", "value": 6},
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9},
                {"rank": "10", "value": 10},
                {"rank": "J", "value": 10},
                {"rank": "Q", "value": 10},
                {"rank": "K", "value": 10}
                ]
        self.cards = [] 

        for suit in suits:
            for rank in ranks:
                self.cards.append([suit,rank])

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self,number):
        cards_dealt = []
        for x in range(number):
            card = self.cards.pop()
            cards_dealt.append(card)
        return cards_dealt


deck1 = Deck()
deck2 = Deck()
deck2.shuffle()
print(deck1.cards)
print(deck2.cards)





















# # cards_dealt = deal(2)
# # card = cards_dealt[0]
# # rank = card[1]


# # if rank == "A":
# #     value = 11
# # elif rank == "J" or rank == "K" or rank == "Q":
# #     value = 10
# # else:
# #     value = int(rank)


# rank_dict ={"rank": rank, "value": value}

# print(card)
# print(rank_dict["rank"], rank_dict["value"])



