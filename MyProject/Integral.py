import sympy as sy


x,y = sy.symbols('x y')

def accel_int(y):

    #Integral of displacement is velocity

    in_f = y

    sy.plot(in_f)

    in_fx = sy.integrate(in_f,x)
    print(in_fx)
    sy.plot(in_fx) #Velocity

    in_fx2 = sy.integrate(in_fx,x)
    print(in_fx2)
    sy.plot(in_fx2)#Acceleration

accel_int()