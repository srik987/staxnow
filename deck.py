from card import Card
import random
class Deck:
    def __init__(self):
        self.deck = []
        for suit in Card.suit:
            for rank in Card.rank:
                self.deck.append(Card(rank,suit))

    def shuffles(self):
        random.shuffle(self.deck)
        print(self.deck)


    def deal(self, user):
        user.hand = user.hand.append(self.deck.pop)
        