import cocos
import settings
import random
import math
from cocos.actions import RotateTo

class OrganismsLayer(cocos.layer.Layer):

    org_sprites = []

    def __init__(self):
        super( OrganismsLayer, self ).__init__()

    def add_organism(self, organism):
        s = cocos.sprite.Sprite('graphics/themes/%s/organism.png' % settings.DEFAULT_THEME)

        dir = 0
        while dir == 0:
            dir = random.randint(-1,1)

        s.color = organism.color
        s.position = organism.pos_x, organism.pos_y
        s.id = organism.id

        s.energy_label = cocos.text.Label('0',font_name='Courier',font_size=10,anchor_x='left', anchor_y='bottom', color=(255,0,0,255))
        s.energy_label.position = 15,0


        if settings.DRAW_LABELS:
            s.add(s.energy_label)

        self.org_sprites.append(s)
        self.add(s)

    def update_org(self, org):
        self.update_position(org)
        self.update_energy_label(org)


    def update_position(self, org):
        vx = (org.pos_last_x) - (org.pos_x)
        vy = (org.pos_last_y*-1) - (org.pos_y*-1)
        r = (math.degrees(math.atan2(vy,vx))) + 90

        for o in self.org_sprites:
            if o.id == org.id:
                o.position = org.pos_x, org.pos_y
                o.do(RotateTo(r, 0.2))

    def update_energy_label(self,org):
        for o in self.org_sprites:
            if o.id == org.id:
                o.energy_label.element.text = str(org.energy)

    def remove_all(self):
        for org in self.org_sprites:
            self.remove(org)
        self.org_sprites = []

    def remove_sprite(self,id):
        for org in self.org_sprites:
            if org.id == id:
                self.remove(org)
                self.org_sprites.remove(org)

