import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

x,y,t = sy.symbols('x y t')

#Displacement equation differentiation = Velocity

f = t**3

sy.plot(f)

df = sy.diff(f, t)

sy.plot(df)
print(df) #Velocity equation = 5*t**4 + 24*t

# Velocity differentiation = Acceleration

df2 = sy.diff(f, t, 2)

sy.plot(df2)
print(df2) #Acceleration equation = 20t**3 + 24

#----------------------------------------------------------------------------