from random import *

import numpy as np
from sympy import *


# Defining Function
def f(x):
    return (cos(pow(2 * e, -2 * x))) / (x ** 2 + 5 * x + 6)


# Defining derivative of function
def g(x):
    return f(x).diff(x).evalf()


# newtonRaphson
def newtonRaphson(xn,N):
    step = 0
    flag = 1
    condition = True
    while condition:
        x1 = xn - np.float(f(x).evalf(subs={x: xn})) / np.float(g(x).evalf(subs={x: xn}))
        print(f'The {step} iteration xn is {xn:.6} and f(xn) is {np.float(f(x).evalf(subs={x: xn})):.6}')
        xn = x1
        step = step + 1
        if step > N:
            flag = 0
            break

        condition = abs(f(xn)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % xn)
    else:
        print('\nNot Convergent.')




# Input Section
x = symbols('x')
e = 0.001
N = 10
xn = -1.0
newtonRaphson(xn,N)

