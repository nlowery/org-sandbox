from pybrain.tools.shortcuts import buildNetwork
import settings
import random


class Brain:

    # generate a random set of neural layers, neurons and connections
    def __init__(self):
        self.move_network = buildNetwork(9, 3, 2, bias=True)


    def process_input(self, input):

        a = self.move_network.activate(input)

        return int(a[0]), int(a[1])


