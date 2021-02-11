import math


def simpsonrule(func,start,end,intervals):
    length = (end - start) / intervals
    x = start
    result = (func(start) + func(end))
    print("i     x       f(x)")
    print("___________________")
    for i in range(0, intervals+1):
        print(i,"|","%.3f"%(x+i*length),"|","%.4f"%func(x + i * length))
        result += (int(True) if i % 2 == 0 else int(False)+2)*2 *func(x + i * length)

    print("\n")
    result = (1/3)*length * result
    return result

def f(x):
    return pow(x*2*math.e,pow(-x,2)-5*x-3)*(3*x-5)

print("The last answer is:  %.6f"%simpsonrule(f,0.5,1, 4))