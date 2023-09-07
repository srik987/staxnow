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
        self.current_dealer = 0
        
    def start_game(self):
        self.game_deck = Deck().shuffle()
        self.deal_cards()
        if len(self.players) < 2:
            return "too few players to play"
        elif len(self.players) == 2:
            self.players[self.current_dealer].role = "dealer"
            if self.current_dealer == 1:
                self.players[self.current_dealer - 1] = "big blind"
            else: self.players[self.current_dealer + 1].role = "big blind"
        else:
            self.players[self.current_dealer].role = "dealer"
            #if self.current_dealer
            self.players[self.current_dealer + 1].role = "small blind"
            self.players[self.current_dealer + 2].role = "big blind"
            self.current_dealer += 1
    def get_players(self):
        return self.players
    def get_round(self):
        return self.round
    def get_pool(self):
        return self.pool
    def add_player(self, new_user):
        self.players.append(new_user)
    def deal_cards(self):
        for num in range(1,2):
            for player in self.players:
                player.hand = self.game_deck.deal()
