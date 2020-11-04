# random walks plot
from random import seed 
from random import random 
from matplotlib import pyplot
# generate random walk
seed(3)
random_walk = list()
random_walk.append(-3 if random() < 0.2 else 3)
for i in range(1, 1000):
    movement = -3 if random() < 0.2 else 3
    value = random_walk[i-1] + movement 
    random_walk.append(value) 
pyplot.plot(random_walk)
pyplot.show()