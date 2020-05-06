from math import exp


def simpsons(f, a, b, n):
    h = (b - a) / float(n)
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            s = s + 2 * f(a + i * h)
        else:
            s = s + 4 * f(a + i * h)
    return h * s / 3


def main():
    def g(t):
        return exp(-t ** 4)
    
    a = 0
    b = 2
    n = 1000
    print(simpsons(g, a, b, n))


main()
