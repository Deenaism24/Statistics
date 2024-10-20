import math
import matplotlib.pyplot as plt


def calculate_trajectory(g, h, alpha, t_end, dt, k, n):
    alpha_rad = math.radians(alpha)
    x = 0
    y = h
    vx = 0
    vy = 0
    t = 0

    x_data = []
    y_data = []
    vx_data = []
    vy_data = []
    t_data = []

    while t < t_end:
        ax = g * math.sin(alpha_rad)
        ay = -g * math.cos(alpha_rad)
        t += dt
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt

        if y <= 0:
            vy = -vy * k
            vx = vx * (1 - n / 100)
            y = 0

        print(f"x={x}, y={y}, t={t}, vx={vx}, vy={vy}")
        x_data.append(x)
        y_data.append(y)
        vx_data.append(vx)
        vy_data.append(vy)
        t_data.append(t)

    return x_data, y_data, vx_data, vy_data, t_data


g = 10
h = 10
alpha = 30
t_end = 10
dt = 0.01
k = 1
n = 5

x_data, y_data, vx_data, vy_data, t_data = calculate_trajectory(g, h, alpha, t_end, dt, k, n)

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.plot(t_data, x_data, label='x(t)')
plt.plot(t_data, y_data, label='y(t)')
plt.xlabel('Время (с)')
plt.ylabel('Координаты (м)')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(t_data, vx_data, label='vx(t)')
plt.plot(t_data, vy_data, label='vy(t)')
plt.xlabel('Время (с)')
plt.ylabel('Скорость (м/с)')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x_data, y_data)
plt.xlabel('x (м)')
plt.ylabel('y (м)')

plt.subplot(2, 2, 4)
plt.plot(vx_data, vy_data)
plt.xlabel('vx (м/с)')
plt.ylabel('vy (м/с)')

plt.tight_layout()
plt.show()