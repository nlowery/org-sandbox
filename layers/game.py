from layers.console import ConsoleLayer
from layers.organisms import OrganismsLayer
from layers.food import FoodLayer
from layers.background import BackgroundLayer
from organism.organism import Organism
from layers.console import ConsoleLayer
from world.world import Map
import settings
import cocos
import time
import random

class Game(cocos.layer.Layer):

    main_scene = None
    console    = None
    org_layer  = None
    food_layer = None
    back_layer = None
    map        = None
    organisms  = []

    def __init__(self):

        cocos.director.director.init(width=settings.SCREEN_WIDTH,height=settings.SCREEN_HEIGHT,fullscreen=settings.FULL_SCREEN)

        super( Game, self ).__init__()

        self.map = Map()
        self.back_layer = BackgroundLayer()
        self.add(self.back_layer)
        self.org_layer = OrganismsLayer()
        self.add(self.org_layer, z=1)
        self.food_layer = FoodLayer()
        self.add(self.food_layer, z=0)
        self.console = ConsoleLayer(self)
        self.add(self.console, z=100)
        self.main_scene = cocos.scene.Scene(self)

        self.schedule(self.setup)

    def reset(self):
        self.unschedule(self.update)
        self.org_layer.remove_all()
        self.food_layer.remove_all()
        self.organisms = []
        self.schedule(self.setup)


    def setup(self, dt):

        # create and add a new organism
        self.organisms.append(Organism(id=int(time.time()*1000),game=self))
        self.org_layer.add_organism(self.organisms[-1])

        self.map.setup_food()

        # if we've created enough organisms, move on from setup
        if len(self.organisms) >= settings.NUMBER_OF_ORGANISMS:
            self.unschedule(self.setup)
            self.schedule(self.update)

    def update(self, dt):
        for i in range(settings.STEPS_PER_FRAME):

            # tell each organism to do its thing
            for org in self.organisms:
                org.step()
                self.org_layer.update_org(org)

            # cull dead organisms and reproduce if it's time
            for org in self.organisms:
                if org.energy <= 0 or org.age >=settings.AGE_OF_DEATH:
                    self.org_layer.remove_sprite(org.id)
                    self.organisms.remove(org)

                if org.reproduce_time <= 0 :
                    org.reproduce_time = settings.REPRODUCTION_TIME
                    if len(self.organisms) < settings.MAX_ORGANISMS or settings.MAX_ORGANISMS < 0:
                        new_org = Organism(id=time.time()*1000,color=org.color,game=self)
                        new_org.brain = org.brain
                        new_org.pos_x = org.pos_x + random.randint(-20,20)
                        new_org.pos_y = org.pos_y + random.randint(-20,20)
                        self.organisms.append(new_org)
                        self.org_layer.add_organism(new_org)



            #check for expired food sources
            self.food_layer.sync_with_map(self.map.food_sources)
            for f in self.map.food_sources:
                if f["store"] <= 0:
                    self.food_layer.remove_food(f["id"])
                    self.map.tiles[f["x"]][f["y"]] = self.map.EMPTY_TILE
                    self.map.food_sources.remove(f)
                    self.map.new_food()

            # reload a new set of organisms if they all die
            if len(self.organisms) <= 0:
                self.reset()


    def start(self):
        cocos.director.director.run(self.main_scene)

