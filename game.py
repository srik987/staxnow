class Game:
    def __init__(self, players):
        self.players = players
        self.round = 0
        # pool variable is set equal to current total bet value
        self.pool = 0

    def get_players(self):
        return self.players
    def get_round(self):
        return self.round
    def get_pool(self):
        return self.pool
    
    def add_player(self, new_user):
        self.players.append(new_user)