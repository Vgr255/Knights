import random

from src import constants
from src import variables

class Quest:
    def grant_rewards(self, knights, char=None):
        if self.win_rewards is not None:
            for type, num in self.win_rewards:
                if type == "cards":
                    if char is not None:
                        char.cards_to_give = num
                    else:
                        while num:
                            knight = random.choice(knights)
                            knight.cards.append(random.choice(constants.white_cards))
                            num -= 1
                if type == "swords":
                    variables.swords["white"] += num
                if type == "bravery":
                    for knight in knights:
                        knight.bravery += num
                if type == "relic":
                    char.relics.append(num)

        if self.lose_rewards is not None:
            for type, num in self.lose_rewards:
                if type == "swords":
                    variables.swords["black"] += num
                if type == "bravery":
                    for knight in knights:
                        knight.bravery -= num
                if type == "catapults":
                    variables.catapults += num

        self.reset()

        for card in constants.evil_cards_quests:
            variables.evil_cards.discard(card)

    def is_lost(self):
        return not self.is_won()

class Castle(Quest):
    def __init__(self):
        self.swords = variables.swords
        self.knights = []
        self.win_rewards = None
        self.lose_rewards = None

    def is_over(self):
        return any(((self.swords["white"] + self.swords["black"]) >= 12,
                    self.swords["black"] >= 7, variable.catapults >= 12))

    def is_won(self):
        return self.swords["white"] > self.swords["black"]

    def is_available(self):
        return True

    def reset(self):
        pass

class SaxonsAndPicts(Quest):
    def __init__(self):
        self.reset()
        self.win_rewards = (("cards", 4), ("bravery", 1), ("swords", 1))
        self.lose_rewards = (("bravery", 1), ("catapults", 2), ("swords", 1))

    def is_over(self):
        return self.enemies >= 4 or (self.card == 5 and not self.need_more) or self.card == 6

    def is_won(self):
        return self.enemies < 4

    def is_available(self):
        return True

    def reset(self):
        self.enemies = 0
        self.card = 0
        self.need_more = False
        for knight in knights:
            knight.move("castle")
        self.knights = []

class Saxons(SaxonsAndPicts):
    pass

class Picts(SaxonsAndPicts):
    pass

class DarkKnight(Quest):
    def __init__(self):
        self.reset()
        self.win_rewards = (("cards", 2), ("bravery", 1), ("swords", 1))
        self.lose_rewards = (("bravery", 1), ("swords", 1))

    def is_over(self):
        return len(self.black_cards) == 5 or len(self.white_cards[0] + self.white_cards[1]) == 5

    def is_won(self):
        return sum(self.white_cards[0] + self.white_cards[1]) > sum(self.black_cards)

    def is_available(self):
        return True

    def reset(self):
        self.black_cards = []
        self.white_cards = [[], []]
        for knight in self.knights:
            knight.move("castle")
        self.knights = []

class HolyGraal(Quest):
    def __init__(self):
        self.white_cards = 0
        self.black_cards = 0
        self.win_rewards = (("relic", "graal"), ("swords", 3), ("bravery", 1), ("cards", 7))
        self.lose_rewards = (("swords", 3), ("bravery", 1))

    def is_over(self):
        return self.white_cards == 7 or self.black_cards == 7

    def is_won(self):
        return self.white_cards == 7

    def is_available(self):
        return not (self.white_cards is self.black_cards is None)

    def reset(self):
        self.white_cards = None
        self.black_cards = None

class Lancelot(Quest):
    def __init__(self):
        self.white_cards = []
        self.black_cards = []
        self.win_rewards = (("relic", "lancelot"), ("swords", 2), ("cards", 4), ("bravery", 1))
        self.lose_rewards = (("swords", 2), ("bravery", 1))

    def is_over(self):
        return len(self.white_cards) == 5 or len(self.black_cards) == 5

    def is_won(self):
        return sum(self.white_cards) > sum(self.black_cards)

    def is_available(self):
        return not (self.white_cards is self.black_cards is None)

    def reset(self):
        self.white_cards = None
        self.black_cards = None

class Dragon(Quest):
    def __init__(self):
        self.white_cards = [[], [], []]
        self.black_cards = []
        self.win_rewards = (("swords", 3), ("cards", 7), ("bravery", 2))
        self.lose_rewards = (("swords", 3), ("bravery", 2))

    def is_over(self):
        return len(self.black_cards) == 6 or len(self.white_cards[0] +
                   self.white_cards[1] + self.white_cards[2]) == 9

    def is_won(self):
        return sum(self.white_cards[0] + self.white_cards[1] + self.white_cards[2]) > sum(self.black_cards)

    def is_available(self):
        return not (self.white_cards is self.black_cards is None)

    def reset(self):
        self.white_cards = None
        self.black_cards = None

class Excalibur(Quest):
    def __init__(self):
        self.position = 7

    def is_over(self):
        return self.position in (1, 13)

    def is_won(self):
        return self.position == 13

    def is_available(self):
        return self.position > 0

    def reset(self):
        self.position = 0
