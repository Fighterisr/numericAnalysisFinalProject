import math
import numpy as np


def Trapezoid(func, start, end, intervals):

    length = (end - start)/intervals
    x = start
    result = (func(start)+func(end))/2
    for i in range(1,intervals):
        result += func(x + i*length)

    result = length *result
    return result


def romberg(func, a, b, p):

    T = np.zeros((p, p))
    for k in range(0, p):
        T[k, 0] = Trapezoid(func, a, b, 2**k)

        for j in range(0, k):
            T[k, j+1] = (4**(j+1) * T[k, j] - T[k-1, j]) / (4**(j+1) - 1)

        print(T[k,0:k+1])

    print("\n")
    return T



def func(x):
    return pow(x*2*math.e,pow(-x,2)-5*x-3)*(3*x-5)

rows = 4
T = romberg(func, 0.5 , 1, rows)
solution = T[rows-1, rows-1]
print("The last answer: %.6f"%(solution))