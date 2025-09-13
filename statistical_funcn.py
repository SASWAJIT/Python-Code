import numpy as np
import statistics as stat
baked_food=[200,150,150,130,200,220,170,188]

a=np.array(baked_food)
# print(np.mean(a)) #sum of all numbers/number of values
# print(np.median(a)) #central value after sorting
# print(stat.mode(a)) #the number occurs most time in the array(if two number ara occuring same no. of times the the numbers occurs first will be th mode)
# print(np.std(a)) # std= (sumation(mean-baked[i)/no. of values)square root
# print(np.var(a)) #variance = (std)^2


#co efficient of co relation

# -1 represents inversely propertional relation ship
#  1 represents  propertional relation ship
#  0 represents no relation ship

tobaco_consumption=[30,50,10,30,50,40]
deaths=[100,120,70,100,120,112]
print(np.corrcoef([tobaco_consumption,deaths]))

