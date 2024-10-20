def calculate_bounces(g, k, v0, h, n):
    bounces = []

    t = 0
    x = 0
    y = h
    vx = v0
    vy = 0

    dt = 0.001  # шаг времени

    i = 0
    while len(bounces) < n:
        vy += -g * dt
        x += vx * dt
        y += vy * dt

        t += dt

        if y <= 0:
            vy = -vy * k
            y = h
            x = 0
            v = vx * k
            bounces.append(i)
            i += 1

        if x >= 1:
            x = 0
            i += 1

    return bounces


g = 10
k = 1
v0 = 15
h = 0.1
n = 10
bounces = calculate_bounces(g, k, v0, h, n)
print("Номера ступенек, о которые ударится мяч:", bounces)