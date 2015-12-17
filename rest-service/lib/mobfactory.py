import json, random
from entities.mob import Mob

class MobFactory(object):

    def __init__(self):
        self.mobs = []
        self.initMobs()

    def initMobs(self):
        with open('lib/mobs.json', 'r') as mob_list:
            tempJson = json.load(mob_list)
            for mob in tempJson['mobs']:
                temp = Mob(mob['name'], mob['stats'])
                self.mobs.append(temp)

    def get_random_mob(self):
        x = random.randint(0, len(self.mobs))
        print x
        if x == len(self.mobs):
            x -= 1
        return self.mobs[x]
