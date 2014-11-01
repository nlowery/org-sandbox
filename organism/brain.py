import settings
import random

class Neuron:

    def __init__(self):
        self.org_value = random.randint(0,1)
        self.value = self.org_value
        self.connections = []
        for i in range(0,settings.CONNECTIONS_PER_NEURON):
            self.connections.append(random.randint(0,settings.NEURONS_PER_LAYER-1))


class NeuralLayer:

    def __init__(self):
        self.neurons = []
        for i in range (0, settings.NEURONS_PER_LAYER):
            self.neurons.append(Neuron())


class Brain:

    # generate a random set of neural layers, neurons and connections
    def __init__(self):
        self.neural_layers = []
        self.memory = {}
        for i in range(0,settings.NEURAL_LAYERS_PER_BRAIN):
            self.neural_layers.append(NeuralLayer())

    def reset_neurons(self):
        for i in range(0, settings.NEURAL_LAYERS_PER_BRAIN):
            for j in range(0, settings.NEURONS_PER_LAYER):
               self.neural_layers[i].neurons[j].value = self.neural_layers[i].neurons[j].org_value

    def check_memory(self, input):
        return None
        #key = ''.join(str(x) for x in input)
        #return self.memory.get(key,None)

    def set_memory(self,input,value):
        key = ''.join(str(x) for x in input)
        self.memory[key] = value
        return value

    def process_input(self, input):

        # do some crazy shit with the input based on our
        # neural connections and return which directions
        # to move on the x and y axis

        # check to see if we've ever processed this input
        mem = self.check_memory(input)

        if mem is None:
             # reset neurons to their initial values
            self.reset_neurons()

            # loop through the input list enough times to assign
            # a value to each neuron on the first layer
            n = 0
            while n < settings.NEURONS_PER_LAYER:
                for i in input:
                    self.neural_layers[0].neurons[n % settings.NEURONS_PER_LAYER].value = i
                    n += 1

            # step through each layer, each neuron, and its connections
            # adding values along those connections to the next layer
            for i in range(0, settings.NEURAL_LAYERS_PER_BRAIN-1):
                for j in range(0, settings.NEURONS_PER_LAYER):
                    for k in range(0, settings.CONNECTIONS_PER_NEURON):
                        c = self.neural_layers[i].neurons[j].connections[k]
                        self.neural_layers[i+1].neurons[c].value += self.neural_layers[i].neurons[j].value

            # remember this input/output so we don't have to process it again later
            mem = self.set_memory(input, self.neural_layers[-1])

        # take the FIRST HALF of values on the output layer and sum up a random selection of them
        xtv = 0
        for i in range(0, settings.NEURONS_PER_LAYER/2):
            xtv += mem.neurons[random.randint(0, settings.NEURONS_PER_LAYER/2)].value

        # if that value is even, move negative on the x axis
        # if it's odd, move positive
        if xtv % 2 == 0:
            mx = -1
        else:
            mx = 1

        # take the LAST HALF of the values on the output layer and sum up a random selection of them
        xtv = 0
        for i in range(settings.NEURONS_PER_LAYER/2, settings.NEURONS_PER_LAYER):
            xtv += mem.neurons[random.randint(settings.NEURONS_PER_LAYER/2, settings.NEURONS_PER_LAYER-1)].value

        # if that value is even, move negative on the y axis
        # if it's odd, move positive
        if xtv % 2 == 0:
            my = -1
        else:
            my = 1

        return mx, my


