"""
Created on Mon Oct 18 10:04:42 2021

@author: dtran556
"""
i = 2.0
emf = 20

def linear():
        x = -100
        while x < 100:
                if i*x + 5 == 13:
                        print("The solution is")
                        print("   x =",x)
                        break
                x += 1

def double():
        x = 0.0
        while x < 100.0:
                y = 0.0
                while y < 100.0:
                        if i*x+y == emf :
                                print("(I, R, \u0394V) =",(i,x,y))
                        y += 1
                x+=1
        print()  
        
emf = 12
i = 0.5
print("i =",i)
double()
i = 1.0
print("i =",i)
double()
i = 1.5
print("i =",i)
double()
i = 2.0
print("i =",i)
double()