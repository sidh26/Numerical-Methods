from math import exp


def Trapezoidal(f, a, b, n):
    h = (b - a) / float(n)
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n, 1):
        s = s + f(a + i * h)
    return h * s


def main():
    def g(t):
        return exp(-t ** 4)
    
    a = 0
    b = 2
    n = 1000
    prevresult = Trapezoidal(g, a, b, 1)
    
    for i in range(2, n):
        result = Trapezoidal(g, a, b, i)
        if abs(prevresult - result) < 0.001:
            break
        prevresult = result
    print(result)


main()
