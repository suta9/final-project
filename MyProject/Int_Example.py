import sympy as sy

x = sy.symbols('x')

Q2 = x + 19

sy.plot(Q2)

in_q = sy.integrate(Q2, x)

sy.plot(in_q)

print(in_q)

in_q2 = sy.integrate(in_q, x)

sy.plot(in_q2)

print(in_q2)