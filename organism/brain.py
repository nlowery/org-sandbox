from pybrain.tools.shortcuts import buildNetwork


class Brain:

    def __init__(self):
        self.move_network = buildNetwork(9, 3, 2, bias=True)


    def process_input(self, input):

        a = self.move_network.activate(input)

        return a[0], a[1]
