import matplotlib.pyplot as plt


def spring_oscillation(m, k, g, x0, v0, dt, t_end):
    x = x0
    xp = x
    v = v0
    t = 0
    x_data = []
    v_data = []
    t_data = []

    while xp <= x:
        a = g - k * x * m
        t += dt
        v += a * dt
        xp = x
        x += v * dt

        print(f"x={x}, t={t}, v={v}")
        t_data.append(t)
        x_data.append(x)
        v_data.append(v)

    return t_data, x_data, v_data


m = 1
g = 10
k = 6
x0 = -1
v0 = 0
dt = 0.01
t_end = 10

t_data, x_data, v_data = spring_oscillation(m, k, g, x0, v0, dt, t_end)

plt.figure()
plt.plot(t_data, x_data, label='Displacement (m)')
plt.plot(t_data, v_data, label='Velocity (m/s)')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.legend()
plt.show()
