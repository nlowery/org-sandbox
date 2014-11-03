from cocos.actions import Repeat, RotateBy, Liquid
from utilities.themes import Theme
import cocos
import settings

class BackgroundLayer(cocos.layer.Layer):

    theme = None

    def __init__(self):
        super( BackgroundLayer, self ).__init__()

        self.theme = Theme(settings.DEFAULT_THEME)

        s = cocos.sprite.Sprite('graphics/themes/%s/background.jpg' % settings.DEFAULT_THEME)
        s.position = settings.SCREEN_WIDTH/2,settings.SCREEN_HEIGHT/2
        s.color = (100,100,200)
        s.opacity = 200

        s.do(Repeat(RotateBy(360, duration=480)))

        if self.theme.background_animated:
            s.do( Repeat(Liquid( grid=(10,10), duration=15 )))

        self.add(s)

