import operator
from functools import reduce

from pip._vendor.msgpack.fallback import xrange


def LagrangeInter(x, x_list, y_list):
    def polinom(j):
        P = [(x - x_list[m]) / (x_list[j] - x_list[m]) for m in xrange(k) if m != j]
        print("L(%.d)= "%(j),"%.9f"%(reduce(operator.mul, P)))
        return reduce(operator.mul, P)

    k = len(x_list)-1
    return sum(polinom(j) * y_list[j] for j in xrange(k))


x_list = [0.35,0.4, 0.55, 0.65, 0.7, 0.85,0.9]
y_list = [-213.5991,-204.4416, -194.9375, -185.0256, -163.8656,-152.6271]

print("\nFinal: %.6f"%(LagrangeInter(0.75, x_list, y_list)))