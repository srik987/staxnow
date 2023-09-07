class User:
    def __init__(self, name, money):
        self.name = name
        self.rounds_won = 0
        self.money = money
        self.hand = []

    def get_name(self):
        return self.name
    
    def get_rounds_won(self):
        return self.rounds_won

    def get_money(self):
        return self.money

    def update_name(self, new_name):
        self.name = new_name

    def win_round(self):
        self.rounds_won += 1
        print(self.rounds_won)
    
    def get_role(self):
        return self.role
    