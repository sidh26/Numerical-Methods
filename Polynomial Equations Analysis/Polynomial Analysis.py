# Given any polynomial function f(x), plot f(x), f'(x), present all stats about f(x).
# Roots, increasing, decreasing regions, pt. of inflection, maxima, minima.

import matplotlib.pyplot as plt
import numpy as np

degree = int(input("Enter maximum number of degree for function "), )
d = []  # Stores coef of the polynomial function
for i in range(0, degree + 1):
    num = float(input("Enter coefficient for " + str(i) + "th degree ", ))
    d.append(num)

print(d)


# represent a function given list of coef
def rep(a):
    for i in range(0, len(a)):
        if a[i] == 0:
            continue
        if a[i] == 1:
            if i == 0:
                print(str(a[0]) + " +", end=" ")
            elif i == 1:
                print("x +", end=" ")
            elif i == len(a) - 1:
                print(("x^" + str(i)), end=" ")
            else:
                print(("x^" + str(i) + " +"), end=" ")
        
        else:
            if i == 0:
                print((str(a[0]) + " +"), end=" ")
            elif i == 1:
                print((str(a[1]) + "*x +"), end=" ")
            elif i == len(a) - 1:
                print((str(a[i]) + "*x^" + str(i)), end=" ")
            else:
                print((str(a[i]) + "*x^" + str(i) + " +"), end=" ")


rep(d)


# calculate value of a function at a point x
def f(x, a):
    s = 0
    for i in range(0, len(a)):
        s += a[i] * x ** i
    return s


f(1, d)
# plot the function
x = np.linspace(-15, 15, 100)  # 100 linearly spaced numbers
y = f(x, d)

# compose plot
plt.plot(x, y)
plt.show()  # show the plot


# plot f'(x)by calculating values of derivative using central approximation
def C(value, n):
    return (f(value + 1 / n, d) - f(value - 1 / n, d)) * n / 2


def der(num):
    n = 1
    u1 = C(num, n)
    n += 1
    u2 = C(num, n)
    while abs(u1 - u2) > 0.00000000001:
        n += 1
        u1 = u2
        u2 = C(num, n)
    return u2


ydash = []
for num in x:
    ydash.append(der(num))

# compose plot
plt.plot(x, ydash)
plt.show()  # show the plot


# calculate root of function
# newton-raphson method
def newton_raphson(x):
    h = f(x, d) / der(x)
    while abs(h) >= 0.000001:
        h = f(x, d) / der(x)
        x = x - h
    
    return x


# bisection method
def bisection(a, b, co):
    c = (a + b) / 2.0
    while (b - a) / 2.0 > 0.0000001:
        if f(c, co) == 0:
            return c
        elif f(a, co) * f(c, co) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2.0
    
    return c


print(bisection(0, -2, d))

# all roots using np.roots
print(np.roots(d[::-1]))  # Roots of f(x)


# Calculate coef of derivative of the function represented by d
def derivative(d):
    l = []
    for i in range(1, len(d)):
        l.append(d[i] * i)
    return l


# Finding first and second derivative
firstDerivative = derivative(d)
print(firstDerivative)

secondDerivative = derivative(firstDerivative)
print(secondDerivative)

# Finding roots of first derivative
minMax = np.roots(firstDerivative[::-1])
print(minMax)

# Checking for Maxima and Minima
for i in range(0, len(minMax)):
    if f(minMax[i], secondDerivative) < 0:
        print("This is a local maxima " + str(minMax[i]))
    elif f(minMax[i], secondDerivative) > 0:
        print("This is a local minima " + str(minMax[i]))
    else:
        print("This is a neither a local maxima nor a local minima " + str(minMax[i]))

# Checking increasing or decreasing
incDec = sorted(minMax)

if len(incDec) == 1:
    if f(incDec[0] - 0.0001, firstDerivative) < 0:
        print("The function is decreasing from -infinity to " + str(incDec[0]))
    elif f(incDec[0] - 0.0001, firstDerivative) > 0:
        print("The function is increasing from -infinity to " + str(incDec[0]))
    if f(incDec[0] + 0.0001, firstDerivative) < 0:
        print("The function is decreasing from " + str(incDec[0]) + " to +infinity")
    elif f(incDec[0] + 0.0001, firstDerivative) > 0:
        print("The function is increasing from " + str(incDec[0]) + " to +infinity")

if len(incDec) > 1:
    if f(incDec[0] - 0.0001, firstDerivative) < 0:
        print("The function is decreasing from -infinity to " + str(incDec[0]))
    elif f(incDec[0] - 0.0001, firstDerivative) > 0:
        print("The function is increasing from -infinity to " + str(incDec[0]))
    if f(incDec[len(incDec) - 1] + 0.0001, firstDerivative) < 0:
        print("The function is decreasing from " + str(incDec[len(incDec) - 1]) + " to +infinity")
    elif f(incDec[len(incDec) - 1] + 0.0001, firstDerivative) > 0:
        print("The function is increasing from " + str(incDec[len(incDec) - 1]) + " to +infinity")

for i in range(0, len(incDec) - 1):
    if f(incDec[i] + 0.0001, firstDerivative) < 0:
        print("The function is decreasing from " + str(incDec[i]) + " to " + str(incDec[i + 1]))
    elif f(incDec[i] + 0.0001, firstDerivative) > 0:
        print("The function is increasing from " + str(incDec[i]) + " to " + str(incDec[i + 1]))

# Finding roots of second derivative
inflection = np.roots(secondDerivative[::-1])
print(inflection)

# Checking point of inflection
count = 0
for i in range(0, len(inflection)):
    
    if f(inflection[i] - 0.001, secondDerivative) * f(inflection[i] + 0.001, secondDerivative) < 0:
        print(str(inflection[i]) + " is a point of inflection ")
        count = count + 1

if count == 0:
    print("There is no point of inflection ")
