import numpy as np
import matplotlib.pyplot as plt

E = 6
C = 1
R = 1
t0 = 0
q0 = 0
tf = 10
n = 101

def delta(t1,t2,n):
    return (t2 - t1) / (n - 1)

t = np.linspace(t0,tf,n)
q = np.zeros([n])

q[0] = q0

for i in range (1,n):
    q[i] = delta(tf, t0, n) * ((1 / R * C) * q[i - 1] - E / R) + q[i - 1]

for i in range(n):
    print(t[i],q[i])

qActual = np.zeros([n])

for i in range (0,n):
    qActual[i] = C * E * (1 - np.exp(-t[i] / (R * C)))

for i in range(n):
    print(t[i],qActual[i])
    
plt.plot(t, q)
plt.plot(t, qActual)

plt.xlabel("Input_Values_(x)")
plt.ylabel("Total_Charge_(C)")
plt.title("Approximation_of_Charge_in_RC_Circuit")
plt.show()


