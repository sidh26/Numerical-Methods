# Curve fitting using ordinary least squares regression, lagrange's interpolation, newton's forward interpolation, newton's backward interpolation
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def cust_cov(a, b):
    i = b - np.mean(b)
    j = a - np.mean(a)
    return np.dot(i, j) / (len(i) - 1)


def cust_var(a):
    i = a - np.mean(a)
    return np.dot(i, i) / (len(i) - 1)


def cust_mean(a):
    return sum(a) / len(a)


def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return (fact)


def ufinal(u, n):
    uf = u
    for i in range(1, n):
        uf = uf * (u - i)
    return (uf)


def back_ufinal(u, n):
    uf = u
    for i in range(1, n):
        uf = uf * (u + i)
    return (uf)


# case 0
def ordinary_least_squares(x, y):
    beta = cust_cov(x, y) / cust_var(x)
    alpha = cust_mean(y) - beta * cust_mean(x)
    yhat = [alpha + beta * i for i in x]
    print("alpha : {}".format(alpha))
    print("beta : {}".format(beta))
    print("estimated values")
    plt.scatter(x, y, c="crimson")
    plt.plot(x, yhat, c="black")
    plt.show()
    yhat = [round(i, 2) for i in yhat]
    print(yhat)


# case 1
def lag_interpolation(x, y):
    xi = float(input("Enter the new data point from {} to {}".format(min(x), max(x))))
    term = 0
    for n in range(len(y)):
        num = y[n]
        for s in range(len(x)):
            if (n != s):
                num = num * ((xi - x[s]) / (x[n] - x[s]))
        term = term + num
    print("Value of f(", xi, ") = ", term)


# case 2
def newtons_fwd_interpolation(x, y1):
    n = len(x)
    y = np.zeros((n, n))
    
    # fills newton's forward difference table's first column
    for i in range(0, n):
        y[i][0] = y1[i]
    
    # calculates rest of newton's forward difference table
    for i in range(1, n):
        for j in range(0, n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]
    
    v = 1895
    
    sum = y[0][0]
    u = (v - x[0]) / (x[1] - x[0])
    for i in range(1, n):
        print(y[0][i], ufinal(u, i))
        sum = sum + (ufinal(u, i) * y[0][i]) / factorial(i)


def newtons_bck_interpolation(x, y1):
    n = len(x)
    
    # creates and initializes newton's backward difference table's first column
    y = []
    for i in range(0, n):
        y += [0]
    for i in range(0, n):
        y[i] = [0] * n
    
    # fills newton's backward difference table's first column
    for i in range(0, n):
        y[i][0] = y1[i]
    y = np.array(y)
    
    # calculates rest of newton's backward difference table
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):  # i,n
            
            y[j][i] = y[j][i - 1] - y[j - 1][i - 1]
    
    # prints newtons backward difference table
    for i in range(0, n):
        print(x[i], end=" ")
        for j in range(0, i + 1):
            print(y[i][j], end=" ")
        print()
    print()
    
    v = float(input("Value to interpolate at:"))
    sum = y[n - 1][0]
    
    u = (v - x[n - 1]) / (x[1] - x[0])
    
    for i in range(1, n):
        sum = sum + (back_ufinal(u, i) * y[n - 1][i]) / factorial(i)
    print(sum)
    plt.plot(x, y1, c="black")
    plt.scatter(v, sum, s=102)
    plt.show()


def accept_input():
    t = int(input("Enter 0 for ordinary least squares regression\nEnter 1 for lagrange's interpolation \nEnter 2 for newton's forward interpolation \nEnter 3 for newton's backward interpolation \n"))
    location = ("/Users/amsurve/Downloads/mathio.csv")
    df = pd.read_csv(location)
    x = np.array(df.iloc[:5, 0])
    y = np.array(df.iloc[:5, 1])
    if t == 0:
        print("-" * 175)
        ordinary_least_squares(x, y)
        print("-" * 175)
    
    elif t == 1:
        print("-" * 175)
        lag_interpolation(x, y)
        print("-" * 175)
    
    
    elif t == 2:
        print("-" * 175)
        newtons_fwd_interpolation(x, y)
        print("-" * 175)
    
    
    elif t == 3:
        print("-" * 175)
        newtons_bck_interpolation(x, y)
        print("-" * 175)
    
    else:
        pass


accept_input()
