import pickle, requests
from controllers.game import Game
from interface.Printer import Printer
#from entities.player import Player
from entities.mob import Mob
#from controllers.Game import Game
from controllers.service_controller import Services
from interface.view import View


# Set up utility objects
printer = Printer()
services = Services()
view = View()

view.clear_screen()
game = Game(services)

# Set up entity objects
while not game.player.is_dead():
    #view.clear_screen()
    for mob in game.mobs:
        print mob.name
    user_input = raw_input(view.get_prompt())
