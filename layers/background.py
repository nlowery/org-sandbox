from cocos.actions import Repeat, RotateBy, Liquid
from utilities.themes import Theme
import cocos
import settings
import pyglet

class BackgroundLayer(cocos.layer.Layer):

    theme = None
    background = None

    def __init__(self):
        super(BackgroundLayer, self ).__init__()

        self.load_theme()

    def load_theme(self):
        self.theme = Theme(settings.DEFAULT_THEME)
        self.load()

    def load(self):

        if self.background:
            self.remove(self.background)

        self.background = cocos.sprite.Sprite('background.jpg')
        self.background.position = settings.SCREEN_WIDTH/2,settings.SCREEN_HEIGHT/2
        self.background.color = (100,100,200)
        self.background.opacity = 200

        self.background.do(Repeat(RotateBy(360, duration=480)))

        if self.theme.background_animated:
            self.background.do( Repeat(Liquid( grid=(10,10), duration=15 )))

        self.add(self.background)

