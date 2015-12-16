
class Entity(object):

    def __init__(self):
        self.HP = 100
        self.strength = 5
        self.dex = 5
        self.agility = 5
        self.equipped = []
        self.inventory = []

    def getAttack(self):
        return self.strength * 1.3

    def getGetHP(self):
        return self.HP

    def getStrength(self):
        return self.strength

    def getDex(self):
        return self.dex

    def getAgility(self):
        return self.agility

    def toString(self):
        print "HP: {}, STR: {}, DEX: {}, AGI: {}".format(self.HP, self.strength, self.dex, self. agility)