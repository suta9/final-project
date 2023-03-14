import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

x,y,t = sy.symbols('x y t')

#Integral of displacement is velocity

in_f = 2*x

sy.plot(in_f)

in_fx = sy.integrate(in_f,x)
print(in_fx)
sy.plot(in_fx) #Velocity

in_fx2 = sy.integrate(in_fx,x)
print(in_fx2)
sy.plot(in_fx2)#Acceleration