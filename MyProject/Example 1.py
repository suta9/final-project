import sympy as sy

def diff_ex():
    t = sy.symbols('t')

    Q1 = t**5 - 12*t**2 - 9

    sy.plot(Q1)

    dq1 = sy.diff(Q1,t)

    sy.plot(dq1)
    print(dq1)

    dq2 = sy.diff(dq1,t)

    sy.plot(dq2)
    print(dq2)

diff_ex()