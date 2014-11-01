import settings
import cocos

class ConsoleLayer(cocos.layer.Layer):

    text_labels = []
    num_lines = settings.NUMBER_OF_CONSOLE_LINES

    def __init__(self):
        super( ConsoleLayer, self ).__init__()

        for i in range(0, self.num_lines):
            self.text_labels.append(cocos.text.Label('',font_name='Courier',font_size=10,anchor_x='left', anchor_y='bottom'))

        x_pos = 5
        for tl in self.text_labels:
            tl.position = 10,x_pos
            self.add(tl)
            x_pos += 10

    def log(self, txt):
        for i in range(self.num_lines-1,0,-1):
            self.text_labels[i].element.text = self.text_labels[i-1].element.text
        self.text_labels[0].element.text = txt