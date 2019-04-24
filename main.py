'''
TODO
1.connect sigma to numbers 
2.make weights and biases random 
3.create floats
4.clean up code

'''

import math
import random

inputs = [[1, 2], [0, 1]]
ans = [[[inputs[0]]]]
completed = []
num_ofnet = [2,2]
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

def costs():
    basecost = []
    for a in options: 
        basecost.append([])
        for b in options[a]:
            for ever in range(len(options[a][b]["output"])):
                try:
                    basecost[-1][ever] += float((options[a][b]["output"][ever] - options[a][b]["right"][ever]))
                    basecost[-1][ever] /= 2
                except:
                    basecost[-1].append(float(options[a][b]["output"][ever] - options[a][b]["right"][ever]))
    
    print(ans[0])
    print(" ")
    for ewads in range(len(ans[0])-2,-1,-1):
        basecost.append([])
    for every in range(len(ans[0])-2,-1,-1):
        for e in range(1,len(ans[0][every])):
            num = 0
            denom = 0
            for c in range(len(ans[0][every])-1):
                denom += ans[0][every][e][c] - ans[0][every][e][-1]
            for b in range(len(ans[0][every])-1):
                print(b)
                if every == len(ans[0])-2:
                    basecost.get()
                    '''print(ans[0][every][e][b],denom,basecost[0][e-1], "all", float(ans[0][every][e][b]-ans[0][every][e][-1])/float(denom))
                    basecost[0][b].append(float(ans[0][every][e][b]-ans[0][every][e][-1])/float(denom)) * basecost[0][e-1])
                else:
                    get = basecost[0][b].append(float(ans[0][every][e][b]-ans[0][every][e][-1])/float(denom)) * basecost[][e-1])
                    #num += (float(ans[0][every][e][b]-ans[0][every][e][-1])/float(denom)) * basecost[-1][e-1]'''
            #print("ez", len(ans[0])-1-every, num)
            #basecost[len(ans[0])-1-every].append(num)

    print(basecost)


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
    costs()

   
main()
print(options)