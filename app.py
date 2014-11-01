from layers.game import Game


class App:
    game = None
    def __init__(self):
        self.game = Game()

    def run(self):
        self.game.start()
