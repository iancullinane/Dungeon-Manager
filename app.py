#from flask import Flask
#
#app = Flask(__name__)
#
#@app.route("/")
#def hello():
#    return "This be a flask app!"
#
#if __name__ == "__main__":
#    app.run(host='0.0.0.0', threaded=True, debug=True)

from interface.Printer import Printer
from entities.Player import Player
from entities.Mob import Mob
from controllers.Game import Game



# Set up utility objects
game = Game()
printer = Printer()

# Set up entity objects
player = Player()
enemy = Mob()

player.toString()
enemy.toString()


