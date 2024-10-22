"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r

def sphere_volume(n, d):
    f = lambda x : x**2
    lst = [[f(r.uniform(-1, 1)) for e in range(d)] for i in range(n)]
    inside = list(filter(less_or_eq, lst))
    return (len(inside)/n)*2**d

def less_or_eq(num):
    if sum(num) <= 1:
        return True
    else:
        return False

def hypersphere_exact(n,d):
    return (m.pi)**(d/2)/(m.gamma(((d/2)+1)))
     
def main():
    n = 100000
    d = 11
    print(sphere_volume(n,d))
    print(hypersphere_exact(n, d))


if __name__ == '__main__':
	main()
