import pickle, requests

class Services(object):

    def __init__(self):
        self._api_url = 'http://192.168.33.200:5000/'

    def getRandomMob(self):
        mob = requests.get(self._api_url + 'mobs/random')
        return pickle.loads(mob.text)