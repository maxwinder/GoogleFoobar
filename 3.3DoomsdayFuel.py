# Built on Python 2.7.13
# Google Foobar Doomsday Fuel

from functools import reduce
from fractions import Fraction, gcd

def MM(a,b):
    c = []
    for i in range(0,len(a)):
        temp=[]
        for j in range(0,len(b[0])):
            s = 0
            for k in range(0,len(a[0])):
                s += a[i][k]*b[k][j]
            temp.append(s)
        c.append(temp)
    return c

def solution(m):

    # locating the stable ores (absorbing states)
    where = [sum(i) == 0 for i in m]

    # from frequency matrix to transition probability matrix
    for i,j in enumerate(m):
        if sum(j):
            m[i] = [float(k) / sum(j) for k in j]
        else:
            m[i][i] = 1

    # finding solution matrix by running many calculations A*A*A*..*A*A --> solution
    for i in range(10):
        m = MM(m,m)

    # probabilities from ore in state0 to stable state ores
    res = [j for i,j in enumerate(m[0]) if where[i]]
    res = [Fraction(i).limit_denominator(10000) for i in res]
    
    base = reduce(lambda x,y: x*y, [i.denominator for i in res])
    denominator = reduce(gcd, [i.numerator * base / i.denominator for i in res])
    answer = [i.numerator * base / (i.denominator * denominator) for i in res]
    answer.append(base / denominator)
    return answer

'''
solution([[0, 1, 0, 0, 0, 1],
               [4, 0, 0, 3, 2, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]])

'''
