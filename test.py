import logging
from deck import Deck

from matplotlib.cbook import ls_mapper
from user import User
def main():
    a = User("srikar",10)
    a.win_round()
    Deck().shuffle

main()