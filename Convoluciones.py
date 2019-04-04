# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 2019

@author: Nahuel
"""
import scipy as sp

# Convolucion Lineal de scipy => sp.convolve(x,h)
def CheckLengthSignal(f,g):
    if (len(g) == len(f)):
        return True
    else:
        return False 

def ConvolucionCircular(f, g):
    if (CheckLengthSignal(f,g)):
        y = sp.zeros(len(f));
        for k in range(len(f)):
            for p in range(len(f)):
                y[k] = y[k] + (f[p] * g[k-p])
    else: 
        fog = len(f) + len(g) - 1 # condicion de aprox. conv lineal a circular
        cantZerosf = fog - len(f)
        cantZerosg = fog - len(g)
        f = sp.append(f,sp.zeros(cantZerosf)) # agrego los ceros que faltan
        g = sp.append(g,sp.zeros(cantZerosg))
        y = sp.zeros(fog);
        for k in range(fog):
            for p in range(fog):
                y[k] = y[k] + (f[p] * g[k-p])
    return y

""" Test 1
f = [2,5,0,4]
g = [4,1,3]     
# Resultado: y = [8 22 11 31 4 12]
""" 
""" # Test 2
f = [2,5,0,4]
g = [4,1,3,0]
# Resultado: y = [12 34 11 31]
"""
"""# Test 3
f = [0,2,2,2,1]
g = [2,2,2]
# Resultado: y = [0 4 8 12 10 6 2]
"""
