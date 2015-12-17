import pickle
from entities.player import Player
from entities.mob import Mob
from controllers.service_controller import Services


class Game(object):

    def __init__(self, services):
        self.services = services
        self.mobs = []
        self.init_game()

    def init_game(self):
        #print "Enter your name:"
        #name = raw_input()
        self.player = Player("Tim the Enchanter")
        monster_count = 5
        for i in range(0, monster_count):
            new_mob = pickle.loads(self.services.get_random_mob())
            self.mobs.append(new_mob)

    def toString(self):
        if(self.gameOver):
            return 'The game continues'