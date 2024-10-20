import matplotlib.pyplot as plt


def falling(g, k, h0, h_stop, v0, dt):
    h = h0
    v = v0
    t = 0
    time_data = []
    height_data = []
    velocity_data = []

    while h > h_stop:
        a = g - k(h) * v**2
        t += dt
        h -= v * dt
        v += a * dt

        print(f"time={t}, height={h}, velocity={v}")
        time_data.append(t)
        height_data.append(h)
        velocity_data.append(v)

    plt.figure()
    plt.plot(time_data, height_data, label='Height (m)')
    plt.plot(time_data, velocity_data, label='Velocity (m/s)')
    plt.xlabel('Time (s)')
    plt.ylabel('Value')
    plt.legend()
    plt.show()


g = 10


def k(h):
    if h > 1000:
        return 0.004
    return 0.003


h0 = 1300
h_stop = 600
v0 = 0  # 3000
dt = 1

falling(g, k, h0, h_stop, v0, dt)
