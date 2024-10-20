from math import pi


def trapezoidal_method(a, b, n, f):
    h = (b - a) / n
    s = f(a) / 2 + f(b) / 2
    x = a
    for _ in range(n - 1):
        x += h
        s += f(x)
    return s * h


a = -1
b = 1
n = 5
print(f"Приближенная площадь: {trapezoidal_method(a, b, n, abs)}")


def f(x):
    return x**2


def volume_of_revolution(a, b, n, f):
    integral = trapezoidal_method(a, b, n, lambda x: f(x)**2)
    print(integral)
    volume = pi * integral
    return volume


a = 0
b = 2
n = 1000
print(f"Объем тела вращения: {volume_of_revolution(a, b, n, f)}")