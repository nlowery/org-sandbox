from layers.game import Game
import unittest

class GameLayerTests(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_theme_init(self):
        self.assertEqual(1,1)
