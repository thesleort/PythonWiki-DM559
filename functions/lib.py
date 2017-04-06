# Module: lib.py
import numpy as np
import scipy as sp
from scipy.linalg import lu

from random import randint

'''
def sumVec(a, b): return [a[i] + b[i] for i in range(len(b))]


def subVec(a, b): return [a[i] - b[i] for i in range(len(b))]


def mulVec(a, b): return [a[i] * b[i] for i in range(len(b))]


def divVec(a, b): return [a[i] / b[i] for i in range(len(b))]
'''


def numpySum(a, b):
    matrixa = np.matrix(a)
    matrixb = np.matrix(b)
    return matrixa + matrixb


def numpysub(a, b):
    matrixa = np.matrix(a)
    matrixb = np.matrix(b)
    return matrixa - matrixb


def numpymul(a, b):
    matrixa = np.matrix(a)
    matrixb = np.matrix(b)
    return matrixa * matrixb


def numpydiv(a, b):
    matrixa = np.matrix(a)
    matrixb = np.matrix(b)
    return matrixa / matrixb


def numpydot(a, b):
    matrixa = np.matrix(a)
    matrixb = np.matrix(b)
    return np.dot(matrixa, matrixb);


def numpycross(a, b):
    matrixa = np.matrix(a)
    matrixb = np.matrix(b)
    return np.cross(matrixa, matrixb);


def numpydet(a):
    return np.linalg.det(a)


def solvegaussian(a):
    array = np.array(a)
    pl, u = sp.linalg.lu(array, permute_l=True)
    return u


def generatearray(x, y):
    return np.random.randint(1, 100, (x, y))


'''
    returns a list where the first value states if its a valid product or not, and the 2nd value is the matrix is its valid.
'''
def checkifvalidcrossproduct(a, b):
    try:
        ret = numpycross(a, b)
        # print("its a valid cross product")
        return [True, ret]
    except:
        # print("its invalid cross product ")
        return [False]


def checkifvaliddotproduct(a, b):
    try:
        ret = numpydot(a, b)
        # print("its a valid dot product")
        return [True, ret]
    except:
        # print("its invalid dot product ")
        return [False]


def checkifvalidmatrixmatrixproduct(a, b):
    return checkifvaliddotproduct(a, b)
