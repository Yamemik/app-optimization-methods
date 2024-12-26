import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определим три целевые функции
def f1(x, y, z):
    return 2*x + y - 3*z

def f2(x, y, z):
    return x + 3*y - 2*z

def f3(x, y, z):
    return -x + 2*y + 4*z

# Сгенерируем точки в диапазоне
x_values = np.linspace(0, 40, 50)
y_values = np.linspace(0, 40, 50)
z_values = np.linspace(0, 40, 50)

# Создаем массив для хранения всех точек
points = []

for x in x_values:
    for y in y_values:
        for z in z_values:
            if x + 3*y + 2*z >= 1 and 2*x - y + z <= 16 and x + 2*y <= 24:
                f1_value = f1(x, y, z)
                f2_value = f2(x, y, z)
                f3_value = f3(x, y, z)
                if f1_value>= 0 and f2_value >= 0 and f3_value >= 0:
                    points.append([f1_value, f2_value, f3_value])

points = np.array(points)

# Функция для нахождения парето-оптимальных точек
def pareto_optimal(points):
    pareto_points = []
    for i, p in enumerate(points):
        if not any(np.all(p2 <= p) and not np.all(p2 == p) for j, p2 in enumerate(points) if i != j):
            pareto_points.append(p)
    return np.array(pareto_points)

# Найдем парето-оптимальные точки
pareto_points = pareto_optimal(points)

# Визуализируем результаты
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Визуализируем все точки
ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='lightgray', label='Все точки', alpha=1)

# Визуализируем парето-оптимальные точки
ax.scatter(pareto_points[:, 0], pareto_points[:, 1], pareto_points[:, 2], color='red', label='Парето-оптимальные точки')

ax.set_xlabel('f1(x, y, z)')
ax.set_ylabel('f2(x, y, z)')
ax.set_zlabel('f3(x, y, z)')
ax.set_title('Метод Парето-оптимальности')
ax.legend()
plt.show()

print(points)
print()
print(pareto_points)