import unittest
from entities.entity import Entity
from entities.player import Player
from entities.mob import Mob
from controllers.service_controller import Services

class TestControllers(unittest.TestCase):

    def setUp():
        services = Services()

