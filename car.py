import numpy as np

h = 0.1
b = 4.0

time_points = np.arange(0, b + h, h)
acceleration = np.random.uniform(0, 3, len(time_points))

velocity = 0
distance = 0

for i in range(len(time_points) - 1):
    avg_acc = (acceleration[i] + acceleration[i + 1]) / 2
    velocity += avg_acc * h
    distance += velocity * h

print("Значения ускорения в моменты времени:")
for t, a in zip(time_points, acceleration):
    print(f"t = {t:.1f} с: a = {a} м/с²")

print(f"Конечная скорость: {velocity} м/с")
print(f"Пройденное расстояние: {distance} м")
