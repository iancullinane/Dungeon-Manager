import unittest
from entities.entity import Entity
from entities.player import Player
from entities.mob import Mob

class TestEntities(unittest.TestCase):

    def setUp(self):
        self.player = Player('Socrates O. Rockefeller')
        self.enemy = Mob("Steve")

    def test_player_created(self):
        '''Test a player can be created'''
        self.assertTrue(isinstance(self.player, Entity))
        self.assertTrue(isinstance(self.player, Player))

    def test_mob_created(self):
        '''Test that a mob can be created'''
        self.assertTrue(isinstance(self.enemy, Entity))
        self.assertTrue(isinstance(self.enemy, Mob))

    #def test_player_attack(self):



if __name__ == '__main__':
    unittest.main()