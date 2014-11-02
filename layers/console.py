import settings
import cocos
import pyglet

class ConsoleCommands:


    def __init__(self, game):
        self.game = game
        self.commands = {
            'clear' : self.cmd_clear,
            '_empty': self.cmd_empty,
            'exit': self.cmd_quit,
            'info': self.cmd_info,
            'quit': self.cmd_quit,
            'reset': self.cmd_reset
        }

    def cmd_clear(self, args):
        ConsoleLayer().reset_console()

    def cmd_empty(self, args):
        ConsoleLayer().log('')

    def cmd_info(self, args):
        ConsoleLayer().log('---------------------------------')
        ConsoleLayer().log('Organisms:    %d' % len(self.game.organisms))
        ConsoleLayer().log('Food Sources: %d' % len(self.game.food_layer.org_sprites))
        ConsoleLayer().log('---------------------------------')
        ConsoleLayer().log('')

    def cmd_quit(self, args):
        exit(0)

    def cmd_reset(self, args):
        self.game.reset()

class ConsoleLayer(cocos.layer.Layer):

    text_labels = []
    num_lines = settings.NUMBER_OF_CONSOLE_LINES
    is_event_handler = True

    def __init__(self, game=None):
        super( ConsoleLayer, self ).__init__()

        # init commands and pass on the game object
        self.commands = ConsoleCommands(game)

        for i in range(self.num_lines):
            self.text_labels.append(cocos.text.Label('',font_name='Courier',font_size=10,anchor_x='left', anchor_y='bottom'))
        self.text_labels[0].element.text = '>'

        x_pos = 5
        for tl in self.text_labels:
            tl.position = 10,x_pos
            self.add(tl)
            x_pos += 10

    def reset_console(self):
        for i in range(self.num_lines):
            self.text_labels[i].element.text = ''
        self.text_labels[0].element.text = '>'

    def log(self, txt):
        for i in range(self.num_lines-2,0,-1):
            self.text_labels[i].element.text = self.text_labels[i-1].element.text
        self.text_labels[1].element.text = txt

    def on_key_release (self, key, modifiers):

        if key == pyglet.window.key.BACKSPACE and len(self.text_labels[0].element.text) > 1:
            self.text_labels[0].element.text = self.text_labels[0].element.text[:-1]

        if key == pyglet.window.key.ENTER:
            cmd = self.text_labels[0].element.text[1:]
            self.text_labels[0].element.text = '>'
            self.execute(cmd)

        if key == pyglet.window.key.SPACE:
            self.text_labels[0].element.text += ' '

        if (key >= 97 and key <= 122) or (key >= 48 and key <=58):
            self.text_labels[0].element.text += pyglet.window.key.symbol_string(key).replace('_','')

    def execute(self, cmd):
        s = cmd.split(' ')
        cmd = s[0].lower()
        args = s[1:]

        if cmd == '':
            cmd = '_empty'

        try:
            self.commands.commands[cmd](args)
        except Exception as e:
            self.log('ERROR: %s' % e.message)








