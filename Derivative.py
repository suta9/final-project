import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

x,y,t = sy.symbols('x y t')

#Displacement equation differentiation = Velocity

f = x**3

sy.plot(f)

df = sy.diff(f, x)

sy.plot(df)
print(df) #Velocity equation differentiation = Acceleration

# Velocity differentiation = Acceleration

df2 = sy.diff(f, x, 2)

sy.plot(df2)
print(df2) #Acceleration
#----------------------------------------------------------
# Integration

