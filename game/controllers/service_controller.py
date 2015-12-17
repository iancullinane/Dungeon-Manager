import pickle, requests
from entities.mob import Mob

class Services(object):

    def __init__(self):
        self._api_url = 'http://192.168.33.200:5000/'

    def get_random_mob(self):
        mob = requests.get(self._api_url + 'mobs/random')
        return mob.content

    def start_combat(self, player):
        req = requests.post(self._api_url + 'combat/start', data = player)
        return req.content