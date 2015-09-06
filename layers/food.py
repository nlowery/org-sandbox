from cocos.actions import Repeat, RotateBy
from utilities.themes import Theme
import settings
import random
import cocos


class FoodLayer(cocos.layer.Layer):

    org_sprites = []
    theme = None

    def __init__(self):
        super( FoodLayer, self ).__init__()
        self.load_theme()

    def load_theme(self):
        self.theme = Theme(settings.DEFAULT_THEME)

    def add_food(self, x,y):


        s = cocos.sprite.Sprite('food.png')
        s.position = (x * 25)+12,  (y * 25)+12
        s.color = (200,200,200)
        s.scale = self.theme.food_scale

        dir = 0
        while dir == 0:
            dir = random.randint(-1,1)

        s.do(Repeat(RotateBy(360*dir, duration=random.randint(15,30))))

        s.id = "%d-%d" % (x,y)

        s.store_label = cocos.text.Label('%d' % settings.STARTING_FOOD_ENERGY,font_name='Courier',font_size=10,anchor_x='left', anchor_y='bottom', color=(54,166,13,255))
        s.store_label.position = (x*25)+15,(y*25)+15

        self.org_sprites.append(s)
        self.add(s)
        if settings.DRAW_LABELS:
            self.add(s.store_label)

    def remove_all(self):
        for os in self.org_sprites:
            self.remove(os)
        self.org_sprites = []

    def remove_food(self, id):
        for os in self.org_sprites:
            if os.id == id:
                self.remove(os)
                self.org_sprites.remove(os)

    def sync_with_map(self, sources):
        # add any missing food sources
        for f in sources:
            found = False
            for os in self.org_sprites:
                if os.id == f["id"]:
                    found = True
            if not found:
                self.add_food(f["x"],f["y"])
        self.update_labels(sources)


    def update_labels(self,food_sources):
        for fs in food_sources:
            for os in self.org_sprites:
                if os.id == fs["id"]:
                    os.store_label.element.text = "%d" % fs["store"]
