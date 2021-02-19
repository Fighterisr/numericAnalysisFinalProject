import numpy as np


def naturalCubicSpline(x, y, value):
    xIndex = 0
    n = len(x)
    # creating h, lambda, mu, d and M
    h = [0] * (n-1)
    lamb = [0] * n
    mu = [0] * n
    d = [0] * n
    M = [0] * n
    # initialize n*n matrix
    matrix = [ [ 0 for i in range(n) ] for j in range(n) ]
    for i in range(n-1): # calculate h
        h[i] = x[i+1] - x[i]
    for i in range(1, n-1): # calculate lambda mu and d
        lamb[i] = h[i]/(h[i-1]+h[i])
        mu[i] = 1-lamb[i]
        d[i] = 6/(h[i-1]+h[i])*((y[i+1]-y[i])/h[i]-(y[i]-y[i-1])/h[i-1])
    # fill the matrix
    for i in range(n):
        for j in range(n):
            if i == j: matrix[i][j] = 2
            elif i - j == 1: matrix[i][j] = mu[i]
            elif j-i == 1: matrix[i][j] = lamb[j-1]
    # determine xIndex
    for i in range(n):
        if value >= x[i]: xIndex = i

    print("Matrix:")
    print(np.array(matrix))
    print("D array:")
    print(d)
    M = np.linalg.solve(matrix,d)
    print("Estimated value:")
    def S(X):
        result =(((x[xIndex+1]-X)**3)*M[xIndex]+((X-x[xIndex])**3)*M[xIndex+1])/(6*h[xIndex])
        result += ((x[xIndex+1]-X)*y[xIndex]+(X-x[xIndex]*y[xIndex+1]))/h[xIndex]

        result += -((x[xIndex+1]-X)*M[xIndex]+(X-x[xIndex])*M[xIndex+1])*h[xIndex]/6
        print(result)
    S(value)


