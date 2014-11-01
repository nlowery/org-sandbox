import cocos
import settings

class BackgroundLayer(cocos.layer.Layer):

    def __init__(self):
        super( BackgroundLayer, self ).__init__()
        s = cocos.sprite.Sprite('graphics/background.jpg')
        s.position = settings.SCREEN_WIDTH/2,settings.SCREEN_HEIGHT/2
        s.color = (100,100,100)
        self.add(s)

