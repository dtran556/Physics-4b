from scipy import random
import numpy as np
import matplotlib.pyplot as plt

i = 4
B = 6
R = 5
a1 = -R
b1 = R
a2 = 0
b2 = np.pi
N = 1000

def f(x):
    return 1
def g(x):
    return np.sin(x)

array1 = np.zeros(N)
array2 = np.zeros(N)

for i in range(N):
    array1[i] = random.uniform(a1, b1)
    array2[i] = random.uniform(a2, b2)

integral_straight = 0.0
integral_semicirc = 0.0

for i in array1:
    integral_straight += f(i)

for i in array2:
    integral_semicirc += g(i)

straight = ((b1-a1)/float(N))*integral_straight
semicirc = ((b2-a2)/float(N))*integral_semicirc

f_net = -i*B*straight+i*B*R*semicirc

print('The_net_force is %0.06f'%f_net, 'N.')
