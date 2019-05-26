'''
Made By Owen Whitman
Hopefully this is helpful! Enjoy your coding journey
'''

import math
import random

class NN:
	def __init__(self, numofnet, input = None):
		self.numofnets = numofnet
		if input is None:
			self.network = [[]]
			for numberoflayers in self.numofnets:
				self.network.append([])
		else:
			self.network = [[input]]
			for numberoflayers in self.numofnets:
				self.network.append([])
			self.createnetwork()

	def createnetwork(self):
		for layer in range(len(self.numofnets)):
			for nurons in range(1, self.numofnets[layer] + 1):
				self.network[layer].append([random.uniform(-1,1)])
				while len(self.network[layer][nurons]) != len(self.network[layer][0]):
					self.network[layer][nurons].append(random.uniform(-1,1))
				self.network[layer][nurons].append(random.uniform(-1,1))
			if layer != len(self.numofnets):
				self.network[layer + 1].append(self.calcnetwork(self.network[layer]))

	def calcnetwork(self, layer):
		output = 0
		layeroutput = []
		for neuron in range(1, len(layer)):
			for weight in layer[neuron]:
				if (layer[neuron].index(weight) < len(layer[0])):
					output += (weight * layer[0][layer[neuron].index(weight)]) + layer[neuron][-1]
			layeroutput.append(self.sigmanuts(output))
			output = 0
		return layeroutput

	def runnetwork(self, input):
		self.network[0][0] = input
		for layer in range(len(self.network)-1):
			self.network[layer+1][0] = self.calcnetwork(self.network[layer])

	def sigmanuts(self, num):
		anw = 1 / (math.exp(-num) + 1)
		return anw
	
	def getnetwork(self):
		return self.network
		