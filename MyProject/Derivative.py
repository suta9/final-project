import sympy as sy

x,y = sy.symbols('x y')

def accel_diff(y):
    #Displacement equation differentiation = Velocity

    f = y

    sy.plot(f)

    df = sy.diff(f, x)

    sy.plot(df)
    print(df) #Velocity equation differentiation = Acceleration

    # Velocity differentiation = Acceleration

    df2 = sy.diff(df, x)

    sy.plot(df2)
    print(df2) #Acceleration
    #----------------------------------------------------------

accel_diff()

