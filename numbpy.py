'''
Made By Owen Whitman
Hopefully this is helpful! Enjoy your coding journey
'''

import math
import random
import numpy as np

class NN:

	def __init__(self, numofnet, input = None, outputmeaning = None,sizeofwieghts=None,sizeofbiases=None,flattenfunction=None):
		self.sizeofwieghts = [-1,1]
		self.sizeofbiases = [-5,5]
		self.meaning = []
		self.numofnets = numofnet
		self.flattenfunction = 1
		if sizeofwieghts is not None:
			self.flattenfunction = flattenfunction
		if sizeofwieghts is not None:
			self.sizeofwieghts= [-sizeofwieghts,sizeofwieghts]
		
		if sizeofbiases is not None:
			self.sizeofbiases= [-sizeofbiases,sizeofbiases]

		if outputmeaning is not None:
			self.meaning = outputmeaning
		if input is None:
			self.network = [[]]
			for numberoflayers in self.numofnets:
				self.network.append([])
				if(isinstance(self.numofnets[numberoflayers],list)):
					for seperatelayers in range(len(self.numofnets[numberoflayers])):
						self.network[numberoflayers].append([])
		else:
			self.network = []
			for numberoflayers in range(len(self.numofnets)):
				self.network.append([])
				if(isinstance(self.numofnets[numberoflayers],list)):
					for seperatelayers in range(len(self.numofnets[numberoflayers])):
						self.network[numberoflayers].append([])
			self.network.append([[]])
			self.network = np.array(self.network)
			print(self.network)
			#self.createnetwork(input)

	def createnetwork(self,input):
		if(isinstance(self.numofnets[0],list)):
			place = 0
			for every in range(len(self.numofnets[0])):
				if(every == len(self.numofnets[0])-1):
					self.network[0][every].append(input[place:self.numofnets[0][every][0]+place])
				else:
					self.network[0][every].append(input[place:self.numofnets[0][every][0]+place])
				place += every +1
		else:
			self.network[0].append(input)
		for layer in range(len(self.numofnets)):
			if(isinstance(self.numofnets[layer],list)):
				for layers in range(len(self.numofnets[layer])):
					for nurons in range(1, self.numofnets[layer][layers][0] + 1):  
						self.network[layer][layers].append([random.uniform(self.sizeofwieghts[0],self.sizeofwieghts[1])])
						while len(self.network[layer][layers][nurons]) != len(self.network[layer][layers][0]):
							self.network[layer][layers][nurons].append(random.uniform(self.sizeofwieghts[0],self.sizeofwieghts[1]))
						self.network[layer][layers][nurons].append(random.uniform(self.sizeofbiases[0],self.sizeofbiases[1]))
					try:
						if(self.numofnets[layer][layers].index('f')):
							self.network[-1][0].extend(self.calcnetwork(self.network[layer][layers]))

					except ValueError:
						if(isinstance(self.numofnets[layer+1],list)):
							calc = self.calcnetwork(self.network[layer][layers])
							a = True
							while a:
								layersleft = layer +1

								try:
									if(isinstance(self.numofnets[layersleft],list)):
										for connector in range(len(self.numofnets[layersleft])):
											if(self.numofnets[layersleft][connector][-1]==self.numofnets[layer][layers][-1]):
												try:
													self.network[layersleft][connector][0].extend(calc)
												except:
													self.network[layersleft][connector].append(calc)
												a = False
									else:
										try:
											self.network[layersleft][0].extend(self.calcnetwork(self.network[layer][layers]))
										except:
											self.network[layersleft].append(self.calcnetwork(self.network[layer][layers]))
										a= False
								except:
									a=False
								layersleft += 1
						else:
							try:
								self.network[layer + 1][0].extend(self.calcnetwork(self.network[layer][layers]))
							except:
								self.network[layer + 1].append(self.calcnetwork(self.network[layer][layers]))
			else:
				for nurons in range(1, self.numofnets[layer] + 1):
					self.network[layer].append([random.uniform(self.sizeofwieghts[0],self.sizeofwieghts[1])])
					while len(self.network[layer][nurons]) != len(self.network[layer][0]):
						self.network[layer][nurons].append(random.uniform(self.sizeofwieghts[0],self.sizeofwieghts[1]))
					self.network[layer][nurons].append(random.uniform(self.sizeofbiases[0],self.sizeofbiases[1]))
				if(layer+1 != len(self.numofnets)):
					if(not isinstance(self.numofnets[layer+1],list)):
						self.network[layer + 1].append(self.calcnetwork(self.network[layer]))
					else:
						for pieces in range(len(self.network[layer+1])):
							self.network[layer + 1][pieces].append(self.calcnetwork(self.network[layer]))
				else:
					self.network[layer + 1][0].extend(self.calcnetwork(self.network[layer]))

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
	
	def setoutputmeaning(self, outputmeaning):
		self.meaning = outputmeaning

	def runnetwork(self, input):
		for layer in range(len(self.numofnets)):
			if(not isinstance(self.numofnets[layer],list)):
				self.network[layer][0]=[]
			else:
				for connection in range(len(self.numofnets[layer])):
					self.network[layer][connection][0] = []
			self.network[-1][0]=[]
		if(isinstance(self.numofnets[0],list)):
			place = 0
			for every in range(len(self.numofnets[0])):
				if(every == len(self.numofnets[0])-1):
					self.network[0][every][0]=input[place:self.numofnets[0][every][0]+place]
				else:
					self.network[0][every][0]=input[place:self.numofnets[0][every][0]+place]
				place += every +1
		else:
			self.network[0][0]= input
		print(self.network)
		for layer in range(len(self.numofnets)):
			if(isinstance(self.numofnets[layer],list)):

				for layers in range(len(self.numofnets[layer])):
					try:
						if(self.numofnets[layer][layers].index('f')):
							self.network[-1][0].extend(self.calcnetwork(self.network[layer][layers]))

					except ValueError:
						if(isinstance(self.numofnets[layer+1],list)):
							calc = self.calcnetwork(self.network[layer][layers])
							a = True
							while a:
								layersleft = layer +1
								if(isinstance(self.numofnets[layersleft],list)):
									for connector in range(len(self.numofnets[layersleft])):
										if(self.numofnets[layersleft][connector][-1]==self.numofnets[layer][layers][-1]):
											self.network[layersleft][connector][0].extend(calc)		
											a = False
								else:
									self.network[layersleft][0].extend(self.calcnetwork(self.network[layer][layers]))
									a= False
								layersleft += 1
						else:
							self.network[layer + 1][0].extend(self.calcnetwork(self.network[layer][layers]))


			else:
				if(layer+1 != len(self.numofnets)):
					if(not isinstance(self.numofnets[layer+1],list)):
						self.network[layer + 1][0].extend(self.calcnetwork(self.network[layer]))
					else:
						for pieces in range(len(self.network[layer+1])):

							self.network[layer + 1][pieces][0].extend(self.calcnetwork(self.network[layer]))
				else:
					self.network[layer+1][0].extend(self.calcnetwork(self.network[layer]))
		return self.network
	
	def sigmanuts(self, num):
		anw = 1 / (math.exp(-num) - 1)
		return anw
	
	def setflattenfunction(self,changeto):
		self.flattenfunction = changeto

	def changesizeofwieghts(self,sizeofwieghts):
		self.sizeofwieghts= [-sizeofwieghts, sizeofwieghts]

	def changesizeofbiases(self,sizeofbiases):
		self.sizeofbiases= [-sizeofbiases,sizeofbiases]

	def getoutput(self):           
		if(self.meaning == []):
			return self.network[-1][0]
		
		ret = {"choice":self.meaning[self.network[-1][0].index(max(self.network[-1][0]))], "opions":{}}
		for output in range(len(self.network[-1][0])):
			ret["opions"][self.meaning[output]] = self.network[-1][0][output]
		return ret
	
	def getnetwork(self): 
		return self.network
	
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
		cost = [[]]
		perdictions = self.turntochanged(perdictions)

		for layers in range(len(self.numofnets)):
			cost.append([])
			if(isinstance(self.numofnets[layers],list)):
				for peice in range(len(self.numofnets[layers])):
					cost[layers].append([])

				for peice in range(len(self.numofnets[layers])):
			
					for neurons in range(self.numofnets[layers][peice][0]):
						cost[layers][peice].append(0.0)
			else:
				for neurons in range(self.numofnets[layers]):
					cost[layers].append(0.0)
		cost.reverse()
		print(cost)
		for first in range(self.numofnets[-1]):
			cost[0].append(0.0)
			cost[0][first]+=(self.network[-1][0][first]-perdictions[first])*(self.network[-1][0][first]-perdictions[first])
		for layer in range(len(self.numofnets)-1,1,-1):
			if(isinstance(self.numofnets[layer],list)):
				for layers in range(len(self.numofnets[layer])):
					for connection in range(1,len(self.network[layer][layers])):
						avg = 0
						for neuorn in range(len(self.network[layer][layers][connection])-1):
							avg+=self.network[layer][layers][connection][neuorn]
						for neuornb in range(len(self.network[layer][layers][connection])-1):
							if(isinstance(self.numofnets[len(self.numofnets)-layer],list)):
								pass
							else:
								cost[len(self.numofnets)-layer][layers][neuornb] += (self.network[layer][layers][connection][neuornb]/avg)*cost[len(self.numofnets)-1-layer][connection-1]	
			else:	
				for connection in range(1,len(self.network[layer])):
					pass
				avg = 0
				for neuorn in range(len(self.network[layer][connection])-1):
					avg+=self.network[layer][connection][neuorn]
				for neuornb in range(len(self.network[layer][connection])-1):
					cost[len(self.numofnets)-layer][neuornb] += (self.network[layer][connection][neuornb]/avg)*cost[len(self.numofnets)-1-layer][connection-1]	
		print(" ")
		print(cost)
		return cost
	
	def turntochanged(self,perdiction):
		if(len(self.network[-1])==1):
			#print("your output is one so it cant be changed to a position")
			return perdiction
		for trial in range(len(perdiction)):
			try:
				index = self.meaning.index(perdiction[trial])
				perdiction=[]
				for output in range(len(self.network[-1][0])):
					if(output==index):
						perdiction.append(1)
					else:
						perdiction.append(0)
			except:
				pass
		return perdiction

	def testnetwork(self, inputs, outputs):
		fin = {"totalcost":0.0}
		for output in range(len(outputs)):
			outputs[output] = self.turntochanged(outputs[output])
		for trial in range(0,len(inputs)):
			finloc = "trial " + str(trial)
			for intenedoutput in range(len(outputs[trial])):
				if(outputs[trial][intenedoutput] > 1.0 or outputs[trial][intenedoutput] < 0.0):
					outputs[trial][intenedoutput] = self.sigmanuts(outputs[trial][intenedoutput])
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

				
b = NN([[[1,'b'],[2,'a']],[[1,'b'],[2,'f','a']],2],[2,3,4])
#print(b.getnetwork())
print(" ")
#print(b.runnetwork([3,5,4]))
#print(b.calccost([0.5,1]))
#print(b.getoutput())
print(" ")
#print(b.testnetwork([[1]],[[1,2,3,4,5]]))
'''a=b
a.randomiseall(0.1)
print(a.getnetwork())'''
