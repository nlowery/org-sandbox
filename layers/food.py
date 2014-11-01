import settings
import random
import cocos
from cocos.actions import Repeat, RotateBy

class FoodLayer(cocos.layer.Layer):

    org_sprites = []

    def __init__(self):
        super( FoodLayer, self ).__init__()

    def add_food(self, x,y):
        s = cocos.sprite.Sprite('graphics/food.png')
        s.position = x * 25,  y * 25
        s.color = (200,200,200)

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

    def remove_food(self, id):
        for os in self.org_sprites:
            if os.id == id:
                self.remove(os)
                self.org_sprites.remove(os)


    def update_labels(self,food_sources):
        for fs in food_sources:
            for os in self.org_sprites:
                if os.id == fs["id"]:
                    os.store_label.element.text = "%d" % fs["store"]
