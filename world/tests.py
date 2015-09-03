from world import Map
import unittest
import settings

class WorldTests(unittest.TestCase):

    def setUp(self):
        self.map = Map()
        self.map.setup_food()

    def test_map_init(self):
        self.assertEqual(self.map.FOOD_TILE, -10)
        self.assertEqual(self.map.EMPTY_TILE, 0)
        self.assertEqual(self.map.TILE_SIZE, 25)
        self.assertEqual(self.map.MAX_X, settings.SCREEN_WIDTH/self.map.TILE_SIZE)
        self.assertEqual(self.map.MAX_Y, settings.SCREEN_HEIGHT/self.map.TILE_SIZE)
        self.assertEqual(len(self.map.food_sources), settings.NUMBER_OF_FOOD_SOURCES)

    def test_map_add_food(self):
        num_food_sources = len(self.map.food_sources)
        self.map.new_food()
        self.assertEqual(len(self.map.food_sources), num_food_sources+1)

    def test_map_get_tile(self):
        self.assertEqual(self.map.get_tile(0,0), self.map.tiles[0][0])
