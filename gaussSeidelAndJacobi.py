import prettytable as pt

def isDominant(A):
    size = len(A)
    for i in range(size):
        diagonal = abs(A[i][i])
        rowSum = sum([abs(number) for number in A[i]]) - diagonal
        if rowSum > diagonal:
            return False
    return True

def jacobi(A,x,b):
    x = x.copy()
    if isDominant(A) == False:
        print("The matrix is not diagonally dominant")
        return
    else:
        print("The matrix is diagonally dominant")
    size = len(A)
    iteration = 0
    epsilon = 0.0001
    table = pt.PrettyTable()
    table.field_names = ['Iteration', 'X', 'Y', 'Z']
    while True:
        oldX = x.copy()
        table.add_row([iteration + 1, x[0], x[1], x[2]])
        for i in range(size):
            sumX = 0
            for j in range(size):
                if i != j:
                    sumX += A[i][j]*oldX[j]
            x[i] = (b[i] - sumX)/A[i][i]
        condition = abs(x[0] - oldX[0])
        if condition < epsilon:
            break
        iteration += 1
    print(table)
    table.clear()
    table.field_names = ['X', 'Y', 'Z']
    table.add_row(x)
    print("\nThe solutions are:")
    print(table)

def gaussSeidel(A,x,b):
    x = x.copy()
    if isDominant(A) == False:
        print("The matrix is not diagonally dominant")
        return
    else:
        print("The matrix is diagonally dominant")
    size = len(A)
    iteration = 0
    epsilon = 0.0001
    table = pt.PrettyTable()
    table.field_names = ['Iteration', 'X', 'Y', 'Z']
    while True:
        oldX = x.copy()
        table.add_row([iteration + 1, x[0], x[1], x[2]])
        for i in range(size):
            sumX = 0
            for j in range(size):
                if i != j:
                    sumX += A[i][j]*x[j]
            x[i] = (b[i] - sumX)/A[i][i]
        condition = abs(x[0]-oldX[0])
        if condition < epsilon:
            break
        iteration += 1
    print(table)
    table.clear()
    table.field_names = ['X', 'Y', 'Z']
    table.add_row(x)
    print("\nThe solutions are:")
    print(table)

def calcMatrix(A,x,b):
    print('Jacobi method:')
    jacobi(A,x,b)

    print('\n______________________________________________________________________________\n')

    print('\ngauss-Seidel method:')
    gaussSeidel(A,x,b)
