'''
Made By Owen Whitman
Hopefully this is helpful! Enjoy your coding journey
'''

import math
import random
import numbpy

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
	
	def getoutput(self):
		return self.network[-1][0]
	
	def getnetwork(self):
		return self.network
	
	def randomisenuron(self,degree,nuronnum):
		for nuron in range(1,len(self.network[nuronnum])):
			for connection in range(len(self.network[nuronnum][nuron])):
				if(self.network[nuronnum][nuron][connection]+degree >= 1 and self.network[nuronnum][nuron][connection]+degree <= -1):						
					print("your difference is to high pick a number less than one")
					return
				elif(self.network[nuronnum][nuron][connection]+degree >= 1):
					self.network[nuronnum][nuron][connection] = random.uniform(self.network[nuronnum][nuron][connection]-degree,1)
				elif(self.network[nuronnum][nuron][connection]+degree <= -1):
					self.network[nuronnum][nuron][connection] = random.uniform(-1,self.network[nuronnum][nuron][connection]+degree)					
				else:
					self.network[nuronnum][nuron][connection] = random.uniform(self.network[nuronnum][nuron][connection]-degree, self.network[layer][nuron][connection]+degree)
	
	def randomiseall(self,degree):
		for layer in range(len(self.network)):
			for nuron in range(1,len(self.network[layer])):
				for connection in range(len(self.network[layer][nuron])):
					if(self.network[layer][nuron][connection]+degree >= 1 and self.network[layer][nuron][connection]+degree <= -1):
						print("your difference is to high pick a number less than one")
						return
					elif(self.network[layer][nuron][connection]+degree >= 1):
						self.network[layer][nuron][connection] = random.uniform(self.network[layer][nuron][connection]-degree,1)
					elif(self.network[layer][nuron][connection]+degree <= -1):
						self.network[layer][nuron][connection] = random.uniform(-1,self.network[layer][nuron][connection]+degree)
					else:
						self.network[layer][nuron][connection] = random.uniform(self.network[layer][nuron][connection]-degree, self.network[layer][nuron][connection]+degree)
	
	def replacenuron(self,newconnections,nuronnum):
		self.network[nuronnum] = newconnections
	
	def testnetwork(self, inputs, outputs):
		fin = {"totalcost":0.0}
		if(len(inputs) != len(outputs)):
			print("the len of inputs is not equal to output")
			return
		if(len(outputs[0]) != self.numofnets[-1]):
			print("you did not format the output correctly it should either be one number or a list of all the weights with the intened positins")
			return
		for trial in range(0,len(inputs)):
			finloc = "trial " + str(trial)
			for intenedoutput in range(len(outputs[trial])):
				if(outputs[trial][intenedoutput] > 1.0 or outputs[trial][intenedoutput] < -1):
					outputs[trial][intenedoutput] = self.sigmanuts(outputs[trial][intenedoutput])
			fin[finloc] = {"allcosts":{"costofoutput":{}},"costoftrial":0.0}
			self.runnetwork(inputs[trial])
			for num_of_outputs in range(0,len(self.getoutput())):
				fin[finloc]["allcosts"]["costofoutput"]["costofnuron " + str(num_of_outputs+1)] = self.getoutput()[num_of_outputs]-outputs[trial][num_of_outputs]
				fin[finloc]["costoftrial"] += self.getoutput()[num_of_outputs]-outputs[trial][num_of_outputs]
			fin[finloc]["costoftrial"] /= len(self.getoutput())
			fin["totalcost"] += fin[finloc]["costoftrial"]
		fin["totalcost"]/=len(inputs)
		return fin

				
b = NN([2,2],[1,3])
print(b.getnetwork())

print(b.testnetwork([[1,2]],[[3,4]]))
'''a=b
a.randomiseall(0.1)
print(a.getnetwork())'''
