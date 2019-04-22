'''
connect sigma to numbers 
make weights and biases random 

'''

import math
import random

inputs = [[1, 2], [0, 1]]
ans = [[[inputs[0]]]]
completed = []
num_ofnet = [2]
for every in num_ofnet:
    ans[0].append([])
right = [[1,2],[3,4]]
fitness = []
output = []


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

def calc_cost(x,a,t):
  if t == "t":
    calc = 0
    calc = (math.sqrt((x-a) ** 2)/2)
    return calc
  else:
    calc = 0
    for every in x:
      index = x.index(every)
      calc += (math.sqrt((every-a[index]) ** 2)/2)
    return calc

def sloping(x):
  print(x)
  
  for e in range(0,len(ans[-1]),2):
    for v in range(len(ans[-1][e][-1][0])):
      try:
        print(v,e[-3][0][v])
      except:
        num = 0
        #print(x[index][v],inputs[index][v])
        num = (x[e][v]-x[e+1][v])/(inputs[e][v]-inputs[e+1][v])
        print(num, "slope")
  print(ans[-1])
'''
def learn():
  cost = 0
  deltaC = []
  deltaCs = []
  deltaCb = []
  changednums = []
  learningrate = 0.1
  for er in output:
    index = output.index(er)
    cost += calc_cost(er,right[index],"b")
  for e in range(len(ans)):
    deltaC.append([])
    deltaCs.append([])
    deltaCb.append([])
    for ever in ans[e][-2]:
      if ever != ans[e][-2][0]:
        index = ans[e][-2].index(ever)
        deltaC.append([])
        print(ever)
        deltaC[index-1].append(calc_cost(ever[-1],right[e][index-1],"t"))
      else:
        for b in ever:
          deltaCs[index-1].append(calc_cost(b,right[e][index-1],"t"))
          deltaCb[index-1].append(calc_cost([0,right[e][index-1],"f"))
  print(deltaCb, "aing")
  print(deltaCs,"dabs")
  ans.append(list(ans))
  for c in range(len(deltaC)-1,0,-1):
    if(deltaC[c] == []):
      deltaC.pop(c)
  for uno in range(len(deltaC)):
    changednums.append([])
    for dos in range(len(deltaC[uno])):
      changednums[uno].append(ans[uno][-1][0][dos]-learningrate*deltaC[uno][dos])'''


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

    '''for everu in range(1, len(inputs)):
        runnet(everu)
    for ev in range(len(ans)):
        output.append(ans[ev][-1][0])

    for every in ans:
      print(every)
      print(" ")
    learn()'''
    # fitness.append(calc_cost(ans[-1][0],0, 0.1))


main()
print(ans)