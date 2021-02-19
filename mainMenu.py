import math
import numpy as np
import sympy as sp
from newtonAndSecant import findRoots
from gaussSeidelAndJacobi import calcMatrix
from Simpson import simpsonrule
from Romberg import romberg
from Lagrange import LagrangeInter
from Neville import NevilleInterpolation
from cubicSpline import naturalCubicSpline

def question7():
     polynomial = lambda x: (sp.cos(2 * math.e ** (-2 * x))) / (x ** 2 + 5 * x + 6)
     findRoots(polynomial, -1.1, 0)

     print("\nSimpson:\n")

     f = lambda x: sp.cos((2 * np.e ** (-2 * x))) / ((x ** 2) + 5 * x + 6)
     print("The last answer is:  %.6f" % simpsonrule(f, -0.4, 0.4, 4))

     print("\nRomberg:\n")

     func = lambda x: sp.cos((2 * np.e ** (-2 * x))) / ((x ** 2) + 5 * x + 6)
     rows = 5
     T = romberg(func, -0.4, 0.4, rows)
     solution = T[rows - 1, rows - 1]
     print("The last answer:%.6f" % (solution))


def question16():
     polynomial = lambda x: (x**2*math.e**(-x**2+5*x-3))*(3*x-5)
     findRoots(polynomial, 0, 3)

     print("\nSimpson:\n")

     f = lambda x: ((x ** 2) * (np.e) ** (-x ** 2 + 5 * x - 3)) * (3 * x - 5)
     print("The last answer is:  %.6f" % simpsonrule(f, 0.5, 1, 4))

     print("\nRomberg:\n")

     func = lambda x: ((x ** 2) * (np.e) ** (-x ** 2 + 5 * x - 3)) * (3 * x - 5)
     rows = 4
     T = romberg(func, 0.5, 1, rows)
     solution = T[rows - 1, rows - 1]
     print("The last answer: %.6f" % (solution))

def question22():
     # Question 22

     # original matrix:

     # A = [[2, 1, 0],
     #   [3, -1, 0],
     #   [1, 4, -2]]
     # x = [0, 0, 0]
     # b = [-3, 1, -5]

     # dominant diagonal matrix

     A = [[2, 1, 0],
          [1, -2, 0],
          [0, 1, -2]]
     x = [0, 0, 0]
     b = [-3, 4, 2]

     calcMatrix(A,x,b)

def question27():
     # Question 27

     # original matrix:

     #      A = [[1, 2, -2],
     #           [1, 1, 1],
     #           [2, 2, 1]]
     #      x = [0, 0, 0]
     #      b = [7, 2, 5]

     # dominant diagonal matrix

     A = [[1, 1, 0],
          [1, 2, 0],
          [0, 0, 1]]
     x = [0, 0, 0]
     b = [3, 5, -1]

     calcMatrix(A,x,b)

def question32():
     # Question 32

     print("\nLagrange:\n")

     x_list = [0.35, 0.4, 0.55, 0.65, 0.7, 0.85, 0.9]
     y_list = [-213.5991, -204.4416, -194.9375, -185.0256, -174.6711,-163.8656, -152.6271]

     print("\nFinal: %.6f" % (LagrangeInter(0.75, x_list, y_list)))

     print("\nNeville:\n")

     x_list = [0.35, 0.4, 0.55, 0.65, 0.7, 0.85, 0.9]
     y_list = [-213.5991, -204.4416, -194.9375, -185.0256, -174.6711,-163.8656, -152.6271]
     print("n | m |      x")
     print("---------------------")
     print('\nFinal :', "%.6f" % (NevilleInterpolation(0.75, x_list, y_list, 0, 6)))

def question39():
     x = [0.1, 0.2, 0.3]
     y = [-0.29004996, -0.56079734, -0.81401972]
     value = 0.25
     naturalCubicSpline(x, y, value)

menu = 'Please select an option to display a question:\n'
menu += '1. Question 7\n2. Question 16\n3. Question 22\n4. Question 27\n5. Question 32\n6. Question 39\nChoice: '
selection = input(menu)
if selection == '1': question7()
elif selection == '2': question16()
elif selection == '3': question22()
elif selection == '4': question27()
elif selection == '5': question32()
elif selection == '6': question39()
else: print('Invalid input')