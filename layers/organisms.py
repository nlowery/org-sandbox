import cocos
import settings
import random
from cocos.actions import *

class OrganismsLayer(cocos.layer.Layer):

    org_sprites = []

    def __init__(self):
        super( OrganismsLayer, self ).__init__()

    def add_organism(self, organism):
        s = cocos.sprite.Sprite('graphics/organism_red.png')

        dir = 0
        while dir == 0:
            dir = random.randint(-1,1)
        s.do(Repeat(RotateBy(360*dir, duration=random.randint(3,5))))

        s.color = organism.color
        s.position = organism.pos_x, organism.pos_y
        s.id = organism.id

        s.energy_label = cocos.text.Label('0',font_name='Courier',font_size=10,anchor_x='left', anchor_y='bottom', color=(255,0,0,255))
        s.energy_label.position = 15,0


        if settings.DRAW_LABELS:
            s.add(s.energy_label)

        self.org_sprites.append(s)
        self.add(s)

    def update_position(self, org):
        for o in self.org_sprites:
            if o.id == org.id:
                o.position = org.pos_x, org.pos_y

    def update_energy_label(self,org):
        for o in self.org_sprites:
            if o.id == org.id:
                o.energy_label.element.text = str(org.energy)

    def remove_sprite(self,id):
        for org in self.org_sprites:
            if org.id == id:
                self.remove(org)
                self.org_sprites.remove(org)

