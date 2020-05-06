import copy
import numpy as np


def det(l):
    l1 = copy.deepcopy(l)
    i = 1
    det = 0
    for x in range(len(l1)):
        l2 = []
        for x1 in range(1, len(l1)):
            l3 = []
            for y1 in range(len(l1)):
                if y1 != x:
                    l3.append(l1[x1][y1])
            l2.append(l3)
        t = (l2[0][0] * l2[1][1]) - (l2[0][1] * l2[1][0])
        s = l[0][x] * t
        det += (i * s)
        i *= -1
    return (det)


def cramers(l1, d, l5):
    l2 = copy.deepcopy(l1)
    l2[0][0] = l5[0]
    l2[1][0] = l5[1]
    l2[2][0] = l5[2]
    
    l3 = copy.deepcopy(l1)
    l3[0][1] = l5[0]
    l3[1][1] = l5[1]
    l3[2][1] = l5[2]
    
    l4 = copy.deepcopy(l1)
    l4[0][2] = l5[0]
    l4[1][2] = l5[1]
    l4[2][2] = l5[2]
    
    dx = det(l2)
    dy = det(l3)
    dz = det(l4)
    
    print("Cramers")
    try:
        print("x :", dx / d)
        print("y : ", dy / d)
        print("z : ", dz / d)
    except ZeroDivisionError:
        print("Determinant of initial matrix is 0")
    
    print()


def gausselim(l):
    a = l[2][0]
    for x in range(4):
        l[2][x] = (l[2][x] * l[0][0]) - (l[0][x] * a)
    
    b = l[1][0]
    for x in range(4):
        l[1][x] = (l[0][0] * l[1][x]) - (l[0][x] * b)
    
    c = l[2][1]
    for x in range(4):
        l[2][x] = (l[2][x] * l[1][1]) - (l[1][x] * c)
    
    a = l[0][0]
    for x in range(4):
        l[0][x] = l[0][x] / a
    
    a = l[1][1]
    for x in range(4):
        l[1][x] = l[1][x] / a
    
    a = l[2][2]
    for x in range(4):
        l[2][x] = l[2][x] / a
    
    z = l[2][-1]
    y = l[1][-1] - (l[1][2] * z)
    x = l[0][-1] - (l[0][1] * y) - (l[0][2] * z)
    
    print("Gauss Elimination")
    print("x :", x)
    print("y : ", y)
    print("z : ", z)
    print()


def gaussjordan(l):
    l = np.array(l)
    
    a = l[2][0]
    for x in range(4):
        l[2][x] = (l[2][x] * l[0][0]) - (l[0][x] * a)
    
    b = l[1][0]
    for x in range(4):
        l[1][x] = (l[0][0] * l[1][x]) - (l[0][x] * b)
    
    c = l[2][1]
    for x in range(4):
        l[2][x] = (l[2][x] * l[1][1]) - (l[1][x] * c)
    
    a = l[0][1]
    for x in range(4):
        l[0][x] = (l[0][x] * l[1][1]) - (l[1][x] * a)
    
    a = l[0][2]
    for x in range(4):
        l[0][x] = (l[2][2] * l[0][x]) - (l[2][x] * a)
    
    b = l[1][2]
    for x in range(4):
        l[1][x] = (l[2][2] * l[1][x]) - (l[2][x] * b)
    
    a = l[1][1]
    for x in range(4):
        l[1][x] = l[1][x] / a
    
    a = l[2][2]
    for x in range(4):
        l[2][x] = l[2][x] / a
    
    a = l[0][0]
    for x in range(4):
        l[0][x] = l[0][x] / a
    
    print("Gauss Jordan")
    print("x :", l[0][-1])
    print("y :", l[1][-1])
    print("x :", l[2][-1])
    print()


def x1func(x2, x3, l):
    return (l[0][-1] - (l[0][1] * x2) - (l[0][2] * x3)) / l[0][0]


def x2func(x1, x3, l):
    return (l[1][-1] - (l[1][0] * x1) - (l[1][2] * x3)) / l[1][1]


def x3func(x1, x2, l):
    return (l[2][-1] - (l[2][1] * x2) - (l[2][0] * x1)) / l[2][2]


def gaussseidel(l):
    x1 = x111 = 0
    x2 = x222 = 0
    x3 = x333 = 0
    x11 = x1func(x2, x3, l)
    x1 = x11
    x21 = x2func(x1, x3, l)
    x2 = x21
    x31 = x3func(x1, x2, l)
    count = 0
    while abs(x111 - x11) > 0.00002 and abs(x222 - x21) > 0.00002 and abs(x333 - x31) > 0.00002:
        count += 1
        x2 = x21
        x3 = x31
        x111 = x11
        x222 = x21
        x333 = x31
        x11 = x1func(x2, x3, l)
        x1 = x11
        x21 = x2func(x1, x3, l)
        x2 = x21
        x31 = x3func(x1, x2, l)
    
    print("Gauss Seidel")
    print("x :", x11)
    print("y :", x21)
    print("x :", x31)
    print(count)
    print()


def diagonaldom(l):
    if abs(l[0][0] >= l[0][1] + l[0][2]) and abs(l[1][1] >= l[1][0] + l[1][2]) and abs(l[2][2] >= l[2][0] + l[2][1]):
        return True
    else:
        return False


def gaussjacobi(l):
    x1 = 0
    x2 = 0
    x3 = 0
    x11 = x1func(x2, x3, l)
    x21 = x2func(x1, x3, l)
    x31 = x3func(x1, x2, l)
    while abs(x1 - x11) > 0.02 and abs(x2 - x21) > 0.02 and abs(x3 - x31) > 0.02:
        x1 = x11
        x2 = x21
        x3 = x31
        x11 = x1func(x2, x3, l)
        x21 = x2func(x1, x3, l)
        x31 = x3func(x1, x2, l)
    
    print("Gauss Jacobi")
    print("x :", x11)
    print("y :", x21)
    print("x :", x31)
    print()


for t in range(5):
    print()
l10 = []
l20 = []
l30 = []
print("------------------------Enter Equations--------------------")
print()
print("Equation 1 : Enter 4 numbers in the format ax + by + cz = d")
for r1 in range(4):
    l10.append(int(input()))
print()
print("Equation 2 : Enter 4 numbers in the format ax + by + cz = d")
for r2 in range(4):
    l20.append(int(input()))
print()
print("Equation 3 : Enter 4 numbers in the format ax + by + cz = d")
for r3 in range(4):
    l30.append(int(input()))
print()

l4 = []
l4.append(l10[-1])
l4.append(l20[-1])
l4.append(l30[-1])

l1 = []
l1.append(l10[:3])
l1.append(l20[:3])
l1.append(l30[:3])

l2 = []
l2.append(l10)
l2.append(l20)
l2.append(l30)

print("Equations enetered are:")
print(l2[0][0], end="")
print("x +", end=" ")
print(l2[0][1], end="")
print("y +", end=" ")
print(l2[0][2], end="")
print("z =", end=" ")
print(l2[0][3])
print(l2[1][0], end="")
print("x +", end=" ")
print(l2[1][1], end="")
print("y +", end=" ")
print(l2[1][2], end="")
print("z =", end=" ")
print(l2[1][3])
print(l2[2][0], end="")
print("x +", end=" ")
print(l2[2][1], end="")
print("y +", end=" ")
print(l2[2][2], end="")
print("z =", end=" ")
print(l2[2][3])
print()

count1 = count2 = 0
if l1[0][0] == 0 or l1[1][1] == 0 or l1[2][2] == 0:
    count1 = 1
    print("Gauss Seidel method not computable because some of the diagonal elements are 0")
if diagonaldom(l2) != True:
    count2 = 1
    print("Gauss Seidel and Gauss Jacobi methods are not computable because matrix formed by the equations is not diagonally dominant")
    print()

d = det(l1)
ch = 0
while True:
    print()
    print("---------------------------Main Menu-----------------------")
    print()
    if count2 == 1:
        print("1. for Cramers\n2. for Gauss Elimination\n3. for Gauss Jordan\n4. for all the methods\n0. to exit")
    elif count1 == 1:
        print("1. for Cramers\n2. for Gauss Elimination\n3. for Gauss Jordan\n4. for Gauss Jacobi\n5. for all the methods\n0. to exit")
    else:
        print("1. for Cramers\n2. for Gauss Elimination\n3. for Gauss Jordan\n4. for Gauss Jacobi\n5. for Gauss Seidel\n6. for all the methods\n0. to exit")
    try:
        ch = int(input())
    except ValueError:
        print("Input was not integer\nEnter again")
        continue
    if count1 == 1 and ch == 5:
        ch = 6
    if count2 == 1 and ch == 4:
        ch = 6
    print()
    if ch == 1:
        cramers(l1, d, l4)
    elif ch == 2:
        gausselim(l2)
    elif ch == 3:
        gaussjordan(l2)
    elif ch == 4 and count2 == 0:
        gaussjacobi(l2)
    elif ch == 5 and (count1 == 0 and count2 == 0):
        gaussseidel(l2)
    
    elif ch == 6:
        cramers(l1, d, l4)
        gausselim(l2)
        gaussjordan(l2)
        print()
        if count2 == 0:
            gaussjacobi(l2)
        
        if count1 == 0 and count2 == 0:
            gaussseidel(l2)
    
    elif ch == 0:
        print("--------------Thank you for using the program :D ----------")
        for t in range(10):
            print()
        break
    else:
        print("Wrong input")
        ch = 0
