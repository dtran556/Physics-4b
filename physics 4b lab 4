import numpy as np

def linear():
    x = -100
    while x < 100:
        if (2*x + 5) == 13:
            print('x = ', x)
            break
        x += 1


def double():
    x = 0.0
    while x < 100:
        y = 0.0
        while y < 100:
            if (2*x + 3*y) == 20:
                print('(x, y) =', (x, y))
            y += 1
        x += 1

              
def resistance():
    current = 0.5
    emf = 12
    
    while current <= 2:
        resist = 0.0
        print()
        print("Current = ", current, " A:")
        while current * resist <= emf:
            voltage = emf - current * resist
            
            print('(R, Δv) =', (resist, voltage))
            
            resist += 1
        current += 0.5
        
        
def exponential():
    v = 0.0
    while v < 4:
        if np.round((0.5 * np.exp(0.95 * v))) == 20:
            print('v = ', v)
            break
        v += 0.001
        
#linear()
#print()
#double()
#resistance()
exponential()
