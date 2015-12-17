import unittest
from controllers.game import Game
from entities.entity import Entity
from entities.player import Player
from entities.mob import Mob
from controllers.service_controller import Services

class TestControllers(unittest.TestCase):

    def setUp(self):
        self.services = Services()
        self.game = Game(self.services)

    def test_get_random_mob(self):
        self.assertEqual(self.services.get_random_mob(), str)


