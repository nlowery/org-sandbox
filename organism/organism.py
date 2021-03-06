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
        self.pos_last_x = self.pos_x
        self.pos_last_y = self.pos_y
        self.energy = settings.STARTING_ENERGY
        self.age = 0
        self.reproduce_time = settings.REPRODUCTION_TIME * (random.randint(75, 125) / 100.0)
        self.distance_from_food = 0
        self.color = color or (random.randint(150,255),random.randint(150,255),random.randint(150,255))

        self.game = game
        self.brain = Brain()


    def move(self,x,y):

        self.pos_last_x = self.pos_x
        self.pos_last_y = self.pos_y

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

        vals[0] = self.game.map.get_tile(x,  y)
        vals[1] = self.game.map.get_tile(x-1,y+1)
        vals[2] = self.game.map.get_tile(x,  y+1)
        vals[3] = self.game.map.get_tile(x+1,y+1)
        vals[4] = self.game.map.get_tile(x+1,y)
        vals[5] = self.game.map.get_tile(x+1,y-1)
        vals[6] = self.game.map.get_tile(x  ,y-1)
        vals[7] = self.game.map.get_tile(x-1,y-1)
        vals[8] = self.game.map.get_tile(x-1,y)

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
                            for fs in self.game.map.food_sources:
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




