'''
TODO
1.connect sigma to numbers 
2.make weights and biases random 
3.create floats
4.clean up code
5. dab on dem haters yeet yah
'''

import math
import random

inputs = [[1, 2], [0, 1]]
ans = [[[inputs[0]]]]
completed = []
num_ofnet = [2,2,1]
for every in num_ofnet:
	ans[0].append([])
right = [[1,2],[3,4]]
fitness = []
output = []
options = {}

def sigmanuts(num):
	anw = 1 / (math.exp(-num) + 1)
	return anw

def stat(every):
	num = 0
	alladd = []
	answ = []
	for a in range(1, len(every)):
		for b in every[a]:
			if (every[a].index(b) < len(every[0])):
				num += (b * every[0][every[a].index(b)]) + every[a][-1]
		alladd.append(num)
		num = 0
	for ever in alladd:
		answ.append(ever)  # sigmanuts(ever))
	while len(answ) != len(alladd):
		answ.pop(0)
	return answ

def create_network(numeachlayer):
	for item, count in list(enumerate(numeachlayer)):

		for everyr in range(1, numeachlayer[item] + 1):
			ans[0][item].append([random.randint(-5, 5)])  # random.uniform(-1,1)])
			while len(ans[0][item][everyr]) != len(ans[0][item][0]):
				ans[0][item][everyr].append(random.randint(-5, 5))  # random.uniform(-5,5))
			ans[0][item][everyr].append(random.randint(-5, 5))  # random.uniform(-1,1))
		if item != len(numeachlayer):
			ans[0][item][0] = stat(ans[0][item])
			ans[0][item + 1].append(ans[0][item][0])

def runnet(x):
	index = 0
	every = 0
	runtimes = 0
	ans.append([[inputs[x]]])
	for yet in ans[0]:
		index = ans[0].index(yet)
		if index != len(ans[0])-1:
			for every in ans[0][index]:
				if every != ans[0][index][0]:
					ans[x][index].append(every)
			ans[x][index][0] = stat(ans[x][index])
			ans[x].append([ans[x][index][0]])

def main():
	create_network(num_ofnet)
	for every in range(1,len(inputs)):
		runnet(every)
		location = "trial-" + str(len(options))
		options["trial-" + str(len(options))] = {}
		for evr in range(len(ans)):
			options[location]["test-" + str(evr)] = {}
			options[location]["test-" + str(evr)]["network"] = ans[evr]
			options[location]["test-" + str(evr)]["output"] = ans[evr][-1][0]
			options[location]["test-" + str(evr)]["right"] = right[evr]


#main()	
#print(options)

class NN:

	def __init__(self, input, numofnet):
		self.network = [[input]]
		self.input = input
		self.numofnets = num_ofnet
		for numberoflayers in self.numofnets:
			self.network.append([])
		self.createnetwork()
	
	def createnetwork(self):
		for item in range(self.numofnets):
			for everyr in range(1, self.numofnets[item] + 1):
				self.network[item].append([random.randint(-5, 5)])  # random.uniform(-1,1)])
				while len(self.network[item][everyr]) != len(self.network[item][0]):
					self.network[item][everyr].append(random.randint(-5, 5))  # random.uniform(-5,5))
				self.network[item][everyr].append(random.randint(-5, 5))  # random.uniform(-1,1))
			if item != len(self.numofnets):
				self.network[item][0] = stat(self.network[item])
				self.network[item + 1].append(self.network[item][0])




	def getnetwork(self):
		return self.network

nural1 = NN([1,2],[2,2])
print(nural1.getnetwork())