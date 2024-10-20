from math import sin, pi


def a_func(x):
    return x * sin(x) - 1


def b_func(x):
    return x**3 - 3


def bisection_method(a, b, d, f):
    while (b - a) / 2 > d:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return (a + b) / 2


a = 0
b = 2 * pi
d = 0.02
print(f"Приближенный корень: {bisection_method(a, b, d, a_func)}")

a = 1
b = 2
d = 0.00001
print(f"Приближенный корень: {bisection_method(a, b, d, b_func)}")
