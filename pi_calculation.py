import random


def monte_carlo_pi(num):
    inside = 0
    for _ in range(num):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            inside += 1
    pi_approx = 4 * inside / num
    return pi_approx


num = 1000000  # Количество случайных точек
print(f"Вычисление числа π с помощью метода Монте-Карло: {monte_carlo_pi(num)}")