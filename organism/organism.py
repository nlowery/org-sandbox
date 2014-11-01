from brain import Brain
from world.world import Map
import math

import settings
import random

class Organism:

    def __init__(self,id=0, color=None):

        self.id = id
        self.pos_x = random.randint(0, settings.SCREEN_WIDTH)
        self.pos_y = random.randint(0, settings.SCREEN_HEIGHT)
        self.energy = settings.STARTING_ENERGY
        self.age = 0
        self.reproduce_time = settings.REPRODUCTION_TIME
        self.distance_from_food = 0
        self.color = color or (random.randint(150,255),random.randint(150,255),random.randint(150,255))

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
        x = (self.pos_x/Map.TILE_SIZE) % Map.MAX_X
        y = (self.pos_y/Map.TILE_SIZE) % Map.MAX_Y
        return x, y

    def scan(self):

        # build a list of all of the tiles around the organism

        vals = [0,0,0,0,0,0,0,0,0]

        x, y = self.map_position()
        m = Map.tiles

        vals[0] = m[x][y]

        try:
            vals[1] = m[x-1][y+1]
        except:
            pass

        try:
            vals[2] = m[x][y+1]
        except:
            pass

        try:
            vals[3] = m[x+1][y+1]
        except:
            pass

        try:
            vals[4] = m[x+1][y]
        except:
            pass

        try:
            vals[5] = m[x+1][y-1]
        except:
            pass

        try:
            vals[6] = m[x][y-1]
        except:
            pass

        try:
            vals[7] = m[x-1][y+1]
        except:
            pass

        try:
            vals[8] = m[x-1][y]
        except:
            pass

        return vals

    def check_for_food(self):

        # see if we're close enough to a food source to receive energy

        x,y = self.map_position()
        self.distance_from_food = 1000000
        for i in range(0, Map.MAX_X):
            for j in range(0, Map.MAX_Y):
                if Map.tiles[i][j] == Map.FOOD_TILE:
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




