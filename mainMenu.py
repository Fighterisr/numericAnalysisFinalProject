import math
import sympy as sp
from newtonAndSecant import findRoots
from gaussSeidelAndJacobi import calcMatrix

def question7():
     polynomial = lambda x: (sp.cos(2 * math.e ** (-2 * x))) / (x ** 2 + 5 * x + 6)
     findRoots(polynomial, -1.1, 0)

def question16():
     polynomial = lambda x: (x**2*math.e**(-x**2+5*x-3))*(3*x-5)
     findRoots(polynomial, 0, 3)

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


menu = 'Please select an option to display a question:\n'
menu += '1. Question 7\n2. Question 16\n3. Question 22\n4. Question 27\n5. Question 32\n6. Question 39\nChoice: '
selection = input(menu)
if selection == '1': question7()
elif selection == '2': question16()
elif selection == '3': question22()
elif selection == '4': question27()
elif selection == '5': pass
elif selection == '6': pass
else: print('Invalid input')