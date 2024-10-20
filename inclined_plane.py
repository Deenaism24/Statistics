from math import radians, sin, cos
import matplotlib.pyplot as plt


def calculate_trajectory(g, h, alpha, t_end, dt, k, n, r):
    alpha_rad = radians(alpha)
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
    s_data = []
    s = 0

    while t < t_end:
        ax = g * sin(alpha_rad) - r * vx
        ay = -g * cos(alpha_rad) - r * vy
        t += dt
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt

        s += (vx**2 + vy**2)**0.5 * dt

        if y <= 0:
            vy = -vy * k
            vx = vx * (1 - n / 100)
            y = 0

        print(f"x={x}, y={y}, t={t}, vx={vx}, vy={vy}, s={s}")
        x_data.append(x)
        y_data.append(y)
        vx_data.append(vx)
        vy_data.append(vy)
        t_data.append(t)
        s_data.append(s)

    return x_data, y_data, vx_data, vy_data, t_data, s_data


g = 10
h = 10
alpha = 30
t_end = 10
dt = 0.01
k = 1
n = 5
r = 0.5

x_data, y_data, vx_data, vy_data, t_data, s_data = calculate_trajectory(g, h, alpha, t_end, dt, k, n, r)

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
plt.plot(t_data, s_data, label='s(t)')
plt.xlabel('Время (с)')
plt.ylabel('Длина пути (м)')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x_data, y_data)
plt.xlabel('x (м)')
plt.ylabel('y (м)')


plt.tight_layout()
plt.show()