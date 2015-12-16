from entities.entity import Entity

class Mob(Entity):

    def __init__(self, name, stats = None):
        super(Mob, self).__init__(stats)
        self.name = name

    def to_string(self):
        print self.name
        print '================='
        for k, v in self.stats.iteritems():
            print '{} => {}'.format(k, v)
