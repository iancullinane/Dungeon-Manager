from entities.entity import Entity

class Player(Entity):

    def __init__(self, name, stats = None):
        if(stats == None):
            super(Player, self).__init__(stats)
        else:
            super(Player, self).__init__()
        self.name = name

    def attack(self, mob):
        mob.stats['HP'] -= self.getAttack()
        print '{} did {} points of damage\n'.format(self.name, self.getAttack())
        print 'The {} has {} HP remaining\n'.format(mob.name, str(mob.stats['HP']))
        mob.is_dead()

    def toString(self):
        print self.name
        print '================='
        for k, v in self.stats.iteritems():
            print '{} => {}'.format(k, v)
        print '\n'

    def isDead(self):
        if(self.stats['HP'] <= 0):
            return True