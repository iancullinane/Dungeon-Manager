
class Entity(object):

    def __init__(self, stats = None):
        self.stats = {}
        '''A base set of stats when stats are not provided'''
        if(stats == None):
            self.stats['HP'] = 10
            self.stats['STR'] = 5
            self.stats['AGI'] = 5
            self.stats['DEX'] = 5
        else:
            for k, v in stats.iteritems():
                self.stats[k] = v

        self.equipped = []
        self.inventory = []


    def heal(self, points):
        self.stats['HP'] += points

    def hurt(self, points):
        self.stats['HP'] -= points

    def initStats(self):
        self.stats['HP'] = 100
        self.stats['STR'] = 5
        self.stats['AGI'] = 5
        self.stats['DEX'] = 5

    def getAttack(self):
        return self.stats['STR'] * 1.3

    def getGetHP(self):
        return self.stats['HP']

    def getStrength(self):
        return self.stats['STR']

    def getDex(self):
        return self.stats['DEX']

    def getAgility(self):
        return self.stats['AGI']
