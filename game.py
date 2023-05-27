from asyncio.windows_events import NULL
from user import User
from deck import Deck
from card import Card

class Game:
    def __init__(self, players):
        self.players = players
        self.round = 0
        # pool variable is set equal to current total bet value
        self.pool = 0
        game_deck = Deck().shuffle
        for num in range(1,2):
            for player in self.players:
                player.hand = game_deck.deal()


    def get_players(self):
        return self.players
    def get_round(self):
        return self.round
    def get_pool(self):
        return self.pool
    def add_player(self, new_user):
        self.players.append(new_user)
    def deal_cards(self):
        NULL