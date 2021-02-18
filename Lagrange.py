import operator
from functools import reduce

from pip._vendor.msgpack.fallback import xrange


def LagrangeInter(x, x_list, y_list):
    def polinom(j):
        P = [(x - x_list[m]) / (x_list[j] - x_list[m]) for m in xrange(k) if m != j]
        print("L(%.d)= "%(j),"%.9f"%(reduce(operator.mul, P)))
        return reduce(operator.mul, P)

    k = len(x_list)
    return sum(polinom(j) * y_list[j] for j in xrange(k))


