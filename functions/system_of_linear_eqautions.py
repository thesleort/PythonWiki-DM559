'''
Author: Troels Blicher Petersen (thesleort)

Description:
This file contains multiple ways to solve 
systems of linear equations.
'''
import numpy as np

'''
Example 1
https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html
'''
#a contains the the two equations and b is the dependent variables.
a = [[3, 1], [1, 2]]
b = [9, 8]

#Solve(a, b) only works, when a is square.
x = np.linalg.solve(a, b)
print x

'''
Example 2
https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.lstsq.html
'''
#a is the four equations and b is the dependent variables.
a = [[1, 2, -8, -4, 0], [0, 0, 2, 12, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
b = [5, 4, 0, 0]

#Using lstsq(a, b) solves systems of linear eqautions, when a is not square.
x = np.linalg.lstsq(a, b)
print x
