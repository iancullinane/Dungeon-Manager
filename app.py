import pickle, requests
from interface.Printer import Printer
from entities.player import Player
from entities.Mob import Mob
from controllers.Game import Game
#from controllers.MobController import MobController
from controllers.service_controller import Services

print "Welcome to pit fighter\n"

# Set up utility objects
game = Game()
printer = Printer()
services = Services()

player = Player('Tim the Enchanter')
enemy = services.getRandomMob()


# Set up entity objects

while not player.isDead():
    print "Your turn\n"
    next_input = raw_input("$=>")
    if next_input == 'attack':
        player.attack(enemy)


#mobs.printRandomMob()
