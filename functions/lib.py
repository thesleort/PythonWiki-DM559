import numpy as np
import scipy as sp
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

def numpydot(a,b):
    matrixa = np.matrix(a)
    matrixb = np.matrix(b)
    return np.dot(matrixa,matrixb);

def numpycross(a,b):
    matrixa = np.matrix(a)
    matrixb = np.matrix(b)
    return np.cross(matrixa,matrixb);


'''
\begin{bmatrix}
  1 & 1 & 1 & = & 6 \\
  2 & 4 & 1 & = & 5 \\
  0 & -1 & 0 & = & 1
\end{bmatrix}
'''
def printmatrixtolatex(a):
    print ("\\begin{bmatrix}")
    first1 = True
    for i in a:
        first2 = True
        if first1 != True:
            print("\\\\ \n", end='')
        else:
            first1 = False
        for j in i:
            if first2 != True:
                print(" & ", end='')
            else:
                first2 = False;
            print (j, end='')

    print()
    print("\\end{bmatrix} ")


#TODO Still working on this, it werks. its ugly, but its works, should probably be done with a while loop
'''
\begin{equation}
  \begin{cases}
    2x_2 -5 = 7\\
    2x_1 + 4x_2 + x_3 = 3 \\
    1/2 x_3 = -5/2 = x_3 = 5
  \end{cases}
\end{equation}
'''
def printlinearsystemtolatex(a):
    print ("\\begin{bmatrix}")
    print ("\\begin{cases}")
    first1 = True
    for i in a:
        first2 = True
        if first1 != True:
            print("\\\\ \n", end='')
        else:
            first1 = False
        *head, tail = i
        for j in head:
            if first2 != True:
                if j < 0:
                    print(" - ", np.absolute(j), end='')
                else:
                    print(" + ",j, end='')
            else:
                first2 = False;
                if j < 0:
                    print("- ",np.absolute(j), end='')
                else:
                    print("  ",j, end='')
        print(" = ",tail,end='')

    print()
    print("\\end{cases}")
    print("\\end{bmatrix} ")

def printlinearsystemtolatexwhileloop(a):
    print ("\\begin{bmatrix}")
    print ("\\begin{cases}")
    i = 0
    while i < len(a):
        if i != 0:
            print("\\\\ \n", end='')
        j = 0
        while j < len(a):
            if j != 0:
                if a[i][j] < 0:
                    print(" - ", np.absolute(a[i][j]), end='')
                else:
                    print(" + ",a[i][j], end='')
            else:
                if a[i][j] < 0:
                    print("- ",np.absolute(a[i][j]), end='')
                else:
                    print("  ",a[i][j], end='')
            j += 1
        print(" = ",a[i][j],end='')
        i +=1


    print()
    print("\\end{cases}")
    print("\\end{bmatrix} ")


def checkifvalidcrossproduct(a,b):
    try:
        numpycross(a, b)
        print("its a valid crossproduct")
        return True
    except:
        print("its invalid crossproduct ")
        return False

def checkifvalidproduct(a,b):
    try:
        numpycross(a, b)
        print("its a valid product")
        return True
    except:
        print("its invalid product ")
        return False

def checkifvaliddotproduct(a,b):
    try:
        numpydot(a, b)
        print("its a valid dotproduct")
        return True
    except:
        print("its invalid dotproduct ")
        return False



def test():
    # a = np.random.randint(1,100,(randint(0, 9),randint(0, 9)));
    # b = np.random.randint(1,100,(randint(0, 9),randint(0, 9)));
    a1 = [[1,1,0],[1,0,1]]
    b1 = [[2,1,1],[3,1,2]]
    a = a1
    b = b1
    print(a)
    print(b)


    # ret =
    #print (ret)
    system = [[-0, -8, 2, 0],
              [-1, 4, -2, 0],
              [-3, 7, 5, 0],]
    # print(system[0][1])

    # printlinearsystemtolatex(system)
    # printlinearsystemtolatexwhileloop(system)
    # print (np.absolute(-1))
    checkifvalidcrossproduct(a,b)
    checkifvalidproduct(a,b)
    checkifvaliddotproduct(a, b)

test()