import pickle, requests
from controllers.game import Game
from interface.Printer import Printer
#from entities.player import Player
from entities.mob import Mob
#from controllers.Game import Game
from controllers.service_controller import Services
from interface.view import View


# Set up utility objects
services = Services()
view = View()

view.clear_screen()
game = Game(services)

# Set up entity objects
while game.player.is_alive():
    view.print_box_array(game.mobs)
    #view.clear_screen()
    #for mob in game.mobs:
    #    print mob.name
    user_input = raw_input(view.get_prompt())
    if user_input == 'attack':
        game.player.attack(game.mobs[0])
    elif user_input == 'clear':
        view.clear_screen()
