'''
Made By Owen Whitman
Hopefully this is helpful! Enjoy your coding journey
'''

import math
import random

class NN:

	def __init__(self, numofnet, input):
		self.meaning = []
		self.numofnets = numofnet
		self.network = []
		for numberoflayers in range(len(self.numofnets)):
			self.network.append([])
		self.network.append([])
		self.createnetwork(input)

	def createnetwork(self,input):
		self.network[0].append(input)
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
		for layer in range(len(self.numofnets)):
			self.network[layer + 1][0]=self.calcnetwork(self.network[layer])
		return self.network
	
	def sigmanuts(self, num):
		anw = 1 / (math.exp(-num) - 1)
		return anw
	
	def getoutput(self):           
		if(self.meaning == []):
			return self.network[-1][0]
		
		ret = {"choice":self.meaning[self.network[-1][0].index(max(self.network[-1][0]))], "opions":{}}
		for output in range(len(self.network[-1][0])):
			ret["opions"][self.meaning[output]] = self.network[-1][0][output]
		return ret
	
	def randomisenuron(self,degree,nuronnum):
		for nuron in range(1,len(self.network[nuronnum])):
			for connection in range(len(self.network[nuronnum][nuron])):
				self.network[nuronnum][nuron][connection] = random.uniform(self.network[nuronnum][nuron][connection]-degree, self.network[nuronnum][nuron][connection]+degree)
	
	def randomiseall(self,degree):
		for layer in range(len(self.network)):
			for nuron in range(1,len(self.network[layer])):
				for connection in range(len(self.network[layer][nuron])):
					self.network[layer][nuron][connection] = random.uniform(self.network[layer][nuron][connection]-degree, self.network[layer][nuron][connection]+degree)
	
	def replacenuron(self,newconnections,nuronnum):
		self.network[nuronnum] = newconnections
	
	def calccost(self,perdictions):
		if(len(perdictions) != len(self.network[-1][0])):
			print("the len of inputs is not equal to output")
			return
		cost = []
		for layers in range(len(self.numofnets)):
			cost.append([])
			for neurons in range(self.numofnets[layers]):
				cost[layers].append(0.0)
		cost.reverse()
		for first in range(self.numofnets[-1]):
			cost[0][first]+=(self.network[-1][0][first]-perdictions[first])**2
		for layer in range(len(self.numofnets)-1,0,-1):
				for connection in range(1,len(self.network[layer])):
					avg = 0
					for neuorn in range(len(self.network[layer][connection])-1):
						avg+=self.network[layer][connection][neuorn]
					for neuornb in range(len(self.network[layer][connection])-1):
						cost[len(self.numofnets)-layer][neuornb] += (self.network[layer][connection][neuornb]/avg)*cost[len(self.numofnets)-1-layer][connection-1]	
		return cost
	

	def testnetwork(self, inputs, outputs):
		fin = {"totalcost":0.0}
		for trial in range(0,len(inputs)):
			finloc = "trial " + str(trial)
			fin[finloc] = {"allcosts":{"costofoutput":{}},"costoftrial":0.0}
			self.runnetwork(inputs[trial])
			calccost = self.calccost(outputs[trial])
			for every in range(len(calccost),-1):
				if(every!=0):
					fin[finloc]["allcosts"]["costs of layer "+ str(len(calccost[every])-every)]={"avgcost":0.0}
				for output in calccost[every]:
					if(every==0):
						fin[finloc]["costoftrial"] += output
						fin[finloc]["allcosts"]["costofoutput"]["neuron "+str(calccost[every].index(output))] = output
					else:
						fin[finloc]["allcosts"]["costs of layer "+ str(len(calccost[every])-every)]["neuron "+ str(calccost[every].index(output))] = output
						fin[finloc]["allcosts"]["costs of layer "+ str(len(calccost[every])-every)]["avgcost"] += output
				if(every!=0):
					fin[finloc]["allcosts"]["costs of layer "+ str(len(calccost[every])-every)]["avgcost"] /=  len(calccost[every])
			fin['totalcost']+= fin[finloc]["costoftrial"]
		fin[finloc]["costoftrial"] /= len(inputs)
		return fin

				
b = NN([1,3,2],[2])
print(b.network)
print(" ")
print(b.runnetwork([3]))
print(b.calccost([0.5,1]))
#print(b.getoutput())
print(" ")
print(b.testnetwork([[1]],[[1,2]]))
'''a=b
a.randomiseall(0.1)
print(a.getnetwork())'''
