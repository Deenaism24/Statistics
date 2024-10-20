import numpy as np
import matplotlib.pyplot as plt

a = 1.0
v = 0.1
T = 10.0
dt = 0.1
bugs_positions = np.array([
    [0, 0],
    [0, a],
    [a, a],
    [a, 0]
])
trajectories = [[] for _ in range(4)]


def update_positions(positions):
    new_positions = np.copy(positions)
    for i in range(4):
        next_bug = (i + 1) % 4

        direction = positions[next_bug] - positions[i]
        distance = np.linalg.norm(direction)
        if distance > 0:
            unit_direction = direction / distance
            new_positions[i] += unit_direction * v * dt

    return new_positions


for t in np.arange(0, T, dt):
    for i in range(4):
        trajectories[i].append(bugs_positions[i].copy())
    bugs_positions = update_positions(bugs_positions)

plt.figure(figsize=(8, 8))
for i in range(4):
    trajectory = np.array(trajectories[i])
    plt.plot(trajectory[:, 0], trajectory[:, 1], label=f'Жук {i + 1}')

plt.title('Траектории движения жуков')
plt.show()