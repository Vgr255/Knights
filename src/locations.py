from src import functions
from src import quests

class Location:
    def __init__(self):
        self.name = functions.separate_name(self.__class__.__name__)
        self.quest = getattr(quests, self.name)()

    def is_available(self):
        return self.quest.is_available()

class Castle(Location):
    ...

class Saxons(Location):
    ...

class Picts(Location):
    ...

class DarkKnight(Location):
    ...

class HolyGraal(Location):
    ...

class Lancelot(Location):
    ...

class Dragon(Location):
    ...

class Excalibur(Location):
    ...
