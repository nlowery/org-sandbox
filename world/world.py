import settings
import random

class Map:

    EMPTY_TILE = 0
    FOOD_TILE = -10
    TILE_SIZE = 25
    MAX_X = settings.SCREEN_WIDTH/TILE_SIZE
    MAX_Y = settings.SCREEN_HEIGHT/TILE_SIZE
    tiles = []
    food_sources = []
    size_x = 0
    size_y = 0


    def __init__(self):
        self.size_x = settings.SCREEN_WIDTH/self.TILE_SIZE
        self.size_y = settings.SCREEN_HEIGHT/self.TILE_SIZE

        for i in range(0,self.size_x):
            cols = []
            for j in range(self.size_y):
                cols.append(self.EMPTY_TILE)
            self.tiles.append(cols)

        for i in range(0, settings.NUMBER_OF_FOOD_SOURCES):
            self.new_food()

    def new_food(self,set_x=None,set_y=None):
        if set_x == None:
            set_x = random.randint(0, self.size_x-1)
        if set_y == None:
            set_y = random.randint(0, self.size_y-1)
        self.tiles[set_x][set_y] = self.FOOD_TILE
        source = {"id": "%d-%d" % (set_x,set_y), "store": settings.STARTING_FOOD_ENERGY, "x": set_x, "y": set_y}
        self.food_sources.append(source)

