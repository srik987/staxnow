class Card:
    rank = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    suit = ('S', 'C', 'D', 'H')
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit