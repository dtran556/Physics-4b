    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    Created on Wed Sep 22 17:25:49 2021
    
    @author: dtran556
    """

    
import matplotlib.pyplot as plt
def line(x):
        m = 0.725
        b = 4
        return m * x + b
with open('/Users/dtran556/Desktop/data.txt', 'r') as f:
        lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
    
    

n = np.linspace(0,60,50)
plt.plor(n,line(n))
plt.scatter(x ,y)
plt.show()
