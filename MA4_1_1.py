
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""


import random as r
import matplotlib.pyplot as plt 

def approximate_pi(n):
    x = [r.uniform(-1, 1) for i in range(n)]
    y = [r.uniform(-1, 1) for i in range(n)]
    inside_x = []
    inside_y = []
    outside_x = []
    outside_y = []
    for i in range(0, len(x)):
        if x[i]**2 + y[i]**2 <= 1:
            inside_x.append(x[i])
            inside_y.append(y[i])
        else:
            outside_x.append(x[i])
            outside_y.append(y[i])   
    plt.scatter(outside_x, outside_y, color = 'blue')
    plt.scatter(inside_x, inside_y, color = 'red')
    plt.show()
    return 4*len(inside_x)/n
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        print(approximate_pi(n))

if __name__ == '__main__':
	main()
