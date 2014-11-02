from brain import Brain
from world.world import Map
import math

import settings
import random

class Organism:

    def __init__(self,id=0, color=None, game=None):

        self.id = id
        self.pos_x = random.randint(0, settings.SCREEN_WIDTH)
        self.pos_y = random.randint(0, settings.SCREEN_HEIGHT)
        self.energy = settings.STARTING_ENERGY
        self.age = 0
        self.reproduce_time = settings.REPRODUCTION_TIME
        self.distance_from_food = 0
        self.color = color or (random.randint(150,255),random.randint(150,255),random.randint(150,255))

        self.game = game
        self.brain = Brain()


    def move(self,x,y):

        self.pos_x += x
        self.pos_y += y

        if self.pos_x < 0:
            self.pos_x = settings.SCREEN_WIDTH

        if self.pos_x > settings.SCREEN_WIDTH:
            self.pos_x = 0

        if self.pos_y < 0:
            self.pos_y = settings.SCREEN_HEIGHT

        if self.pos_y > settings.SCREEN_HEIGHT:
            self.pos_y = 0

    def map_position(self):
        x = (int(self.pos_x)/self.game.map.TILE_SIZE) % self.game.map.MAX_X
        y = (int(self.pos_y)/self.game.map.TILE_SIZE) % self.game.map.MAX_Y
        return x, y

    def scan(self):

        # build a list of all of the tiles around the organism

        vals = [0,0,0,0,0,0,0,0,0]

        x, y = self.map_position()
        m = self.game.map.tiles

        vals[0] = m[x][y]
        vals[1] = m[x-1][min(y+1,Map.size_y)]
        vals[2] = m[x][min(y+1,Map.size_y)]
        vals[3] = m[min(x+1,Map.size_x)][min(y+1,Map.size_y)]
        vals[4] = m[min(x+1,Map.size_x)][y]
        vals[5] = m[min(x+1,Map.size_x)][y-1]
        vals[6] = m[x][y-1]
        vals[7] = m[x-1][min(x+y,Map.size_y)]
        vals[8] = m[x-1][y]

        return vals

    def check_for_food(self):

        # see if we're close enough to a food source to receive energy

        x,y = self.map_position()
        self.distance_from_food = 1000000
        for i in range(self.game.map.MAX_X):
            for j in range(self.game.map.MAX_Y):
                if self.game.map.tiles[i][j] == self.game.map.FOOD_TILE:
                    d = math.hypot(i-(x),j-(y+1))
                    if d < self.distance_from_food:
                        self.distance_from_food = d
                    if d <= 1:
                        if self.energy < settings.MAX_ENERGY:
                            self.energy += 10
                            for fs in Map.food_sources:
                                id = "%d-%d" % (i,j)
                                if fs["id"] == id:
                                    fs["store"] -= 10


    def step(self):
        # process movement, food, age and reproduction
        mx, my = self.brain.process_input(self.scan())

        self.move(mx, my)
        self.check_for_food()
        self.energy -= 1
        self.reproduce_time -= 1
        self.age += 1




