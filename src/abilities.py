from src import functions

combat_locations = ("castle", "saxons", "picts", "dark knight", "lancelot", "dragon")

class TradeCards:
    def __init__(self):
        self.phase = "heroic"
        self.affect = "hand cards"
        self.affected = 2
        self.self_affected = True
        self.required_locations = None

    def __call__(self, char, other, card):
        functions.trade_cards(char, other, card)

class SeeBlackCard:
    def __init__(self):
        self.phase = "evil"
        self.affect = "black cards"
        self.affected = 1
        self.self_affected = True
        self.required_locations = None

    def __call__(self, char):
        functions.reveal_black_card(char, 1)

class AddWhiteCard:
    def __init__(self):
        self.phase = "fight"
        self.affect = "outcome"
        self.affected = 0
        self.self_affected = False
        self.required_locations = combat_locations

    def __call__(self, char, card):
        char.add(card)

class MoveFromRoundTable:
    def __init__(self):
        self.phase = "heroic"
        self.affect = None
        self.affected = 1
        self.self_affected = True
        self.required_locations = ("castle",)

    def __call__(self, char, location):
        char.move(location, consume=False)

class UseSpecialCard:
    def __init__(self):
        self.phase = "heroic"
        self.affect "hand cards"
        self.affected = 0
        self.self_affected = False
        self.required_locations = None

    def __call__(self, char, card, target=None):
        char.play(card, target, consume=False)

class GainBraveryPoint:
    def __init__(self):
        self.phase = "fight"
        self.affect = "bravery"
        self.affected = 1
        self.self_affected = True
        self.required_locations = combat_locations

    def __call__(self, char, location):
        char.bravery += 1

class PickThreeCards:
    def __init__(self):
        self.phase = "heroic"
        self.affect = "white cards"
        self.affected = 1
        self.self_affected = True
        self.required_locations = ("castle",)

    def __call__(self, char):
        card = random.choice(variables.white_cards)
        char.cards.append(card)
        variables.white_cards.remove(card)

class PickBlackCard:
    def __init__(self):
        self.phase = "evil"
        self.affect = "black cards"
        self.affected = 1
        self.self_affected = True
        self.required_locations = None

    def __call__(self, char):
        functions.reveal_black_card(char, 2)

class ReviveDeadKnight:
    def __init__(self):
        self.phase = None
        self.affect = "death"
        self.affected = 1
        self.self_affected = False
        self.required_locations = None

    def __call__(self, char, knight):
        knight.bravery = 4
        char.relics.remove("graal")



















