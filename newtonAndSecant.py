import prettytable as pt
import sympy as sp

def toDerivative(polynomial):
    x = sp.symbols('x')
    derivative = sp.diff(polynomial(x), x)
    return sp.lambdify(x, derivative, 'math')

def newtonRaphson(polynomial,left,right,epsilon):
    derivative = toDerivative(polynomial)
    xr = (left+right)/2
    iteration = 0
    xrOld = 0
    table = pt.PrettyTable()
    header = ['Iteration','xr', 'f(xr)', "f'(xr)"]
    table.field_names = header
    table.float_format = '0.6'
    while abs(xr-xrOld) > epsilon:
        table.add_row([iteration+1, xr, float(polynomial(xr)), derivative(xr)])
        xrOld = xr
        xr = xr - (float(polynomial(xr))/derivative(xr))
        iteration +=1
    print(table)
    print('Root: {:.6f}'.format(xr))
    print('Number of iterations:',iteration)

def secantMethod(polynomial, left, right, epsilon):
    iteration = 0
    xr, xr1 = left, right
    table = pt.PrettyTable()
    header = ['Iteration', 'xr', 'xr+1', "f(xr)"]
    table.field_names = header
    table.float_format = '0.6'
    while abs(xr-xr1) > epsilon:
        table.add_row([iteration + 1, xr, xr1, float(polynomial(xr))])
        xrTemp = xr1
        xr1 = (xr*float(polynomial(xr1))-xr1*float(polynomial(xr)))/(float(polynomial(xr1))-float(polynomial(xr)))
        xr = xrTemp
        iteration += 1
    print(table)
    print('Root: {:.6f}'.format(xr1))
    print('Number of iterations:', iteration)

def findRoots(polynomial, left, right):
    epsilon = 0.000001
    step = 0.1


    leftOld = left
    print('Finding roots using the Newton-Raphson method:')
    while left < right:
        if polynomial(left)*polynomial(left + step)<=0:
            newtonRaphson(polynomial, left, left + step, epsilon)
        left += step
    left = leftOld

    print('\n______________________________________________________________________________\n')


    print('\nFinding roots using the Secant method:')
    while left < right:
        if polynomial(left)*polynomial(left + step)<=0:
            secantMethod(polynomial, left, left + step, epsilon)
        left += step

