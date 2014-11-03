from cocos.actions import Repeat, RotateBy
import cocos
import settings

class BackgroundLayer(cocos.layer.Layer):

    def __init__(self):
        super( BackgroundLayer, self ).__init__()
        s = cocos.sprite.Sprite('graphics/themes/%s/background.jpg' % settings.DEFAULT_THEME)
        s.position = settings.SCREEN_WIDTH/2,settings.SCREEN_HEIGHT/2
        s.color = (100,100,100)
        s.do(Repeat(RotateBy(360, duration=480)))
        self.add(s)

