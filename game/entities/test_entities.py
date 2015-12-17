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

    def test_player_attack(self):
        '''Test that a player attack removes health of the enemy'''
        self.assertEqual(self.enemy.stats['HP'], 10)
        self.player.attack(self.enemy)
        self.assertNotEqual(self.enemy.stats['HP'], 10)

    def test_player_heal(self):
        self.player.stats['HP'] = 2
        self.player.heal(8)
        self.assertEqual(self.player.stats['HP'], 10)

    def test_life(self):
        self.assertTrue(self.player.is_alive())
        self.assertFalse(self.player.is_dead())
        self.player.stats['HP'] = 0
        self.assertTrue(self.player.is_dead())
        self.assertFalse(self.player.is_alive())



if __name__ == '__main__':
    unittest.main()