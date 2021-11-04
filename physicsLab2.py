import matplotlib.pyplot as plt
import numpy as np

data=np.genfromtxt('ohmslaw_data.txt')
# seperate data into x values
x=data[:,0]
# seperate data into y values
y=data[:,1]
#take n to be length of the array
n=len(x)
def sum_func(array):
 array_sum=0
 for i in array:
         array_sum+=i

 return array_sum

def R(x,y,n):
    numerator = n * sum_func(x * y) - sum_func(x) * sum_func(y)
    denominator = n * sum_func(x ** 2) - sum_func(x)**2
    
    return   (numerator/denominator)

def V(I):
    return I*R(x,y,n)


    #generates values for current in terms of A
I=np.linspace(0,380,n)

    #starts figure then label axes and give title to plot
plt.figure()
plt.xlabel("Current (A)")
plt.ylabel("Voltage(V)")
plt.title("Current-Voltage Plot")

    #plots scatter plot of data provided
plt.scatter(x,y)

    #plots linear function V(I) defined above
plt.plot(I,V,(I), color='k')

    #inserts equation V=IR into plot
plt.text(7,10,r'$V_=$_I%0.3f'%R(x,y,n), fontsize=15)

plt.show()