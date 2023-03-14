import sympy as sy

#Example : Jenny throws a ball directly up in the air. She notices that it changes direction after approximately 3 seconds. What was the initial velocity of the ball?

t = sy.symbols('t')

Q1 = t**5 - 12*t**2 - 9

sy.plot(Q1)

dq1 = sy.diff(Q1,t)

sy.plot(dq1)
print(dq1)

dq2 = sy.diff(dq1,t)

sy.plot(dq2)
print(dq2)