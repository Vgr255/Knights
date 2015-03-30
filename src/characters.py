import random

from src import abilities
from src import functions
from src import constants

class Character:
    def __init__(self):
        self.name = functions.separate_name(self.__class__.__name__)
        self.bravery = 4
        self.side = "good"
        pl = functions.list_players()
        all_cards = list(constants.white_cards)
        for i in len(pl):
            all_cards.remove("Merlin")
        self.cards = [None] * 5
        for i in range(len(self.cards)):
            self.cards[i] = random.choice(all_cards)
        self.special = self.get_special()

class KingArthur(Character):
    def get_special(self):
        return abilities.TradeCards()

class SirePerceval(Character):
    def get_special(self):
        return abilities.SeeBlackCard()

class SireTristan(Character):
    def get_special(self):
        return abilities.MoveFromRoundTable()






























