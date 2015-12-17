import pickle
from flask import Flask, jsonify, request
from lib.mobfactory import MobFactory
import json

app = Flask(__name__)
mob_factory = MobFactory()

@app.route("/")
def hello():
    return "Pit Fighter Services API v0.0.1"


@app.route("/mobs/random")
def getRandomMob():
    return pickle.dumps(mob_factory.get_random_mob())


@app.route("/combat", methods=['POST'])
def combat_round():
    if request.method == 'POST':
        print request.data
        #data = request
        return "Combat return"



if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, debug=True)
