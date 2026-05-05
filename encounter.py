

class encounter():
    def __init__(self, monsters):
        self.monsters = monsters

    def __str__(self):
        str = ""
        for monster in self.monsters:
            str += "\n" + monster

        return str
    