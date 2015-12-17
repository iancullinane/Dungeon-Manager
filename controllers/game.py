from entities.player import Player
from entities.mob import Mob
from controllers.service_controller import Services

class Game(object):

    def __init__(self, services):
        self.mobs = []
        self.services = services
        self.init_game()

    def init_game(self):
        print "Enter your name:"
        name = raw_input()
        self.player = Player(name)
        monster_count = 5
        for i in range(0, monster_count):
            self.mobs.append(self.services.get_random_mob())


    def toString(self):
        if(self.gameOver):
            return 'The game continues'