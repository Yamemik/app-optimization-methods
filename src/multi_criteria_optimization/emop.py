import numpy as np
import matplotlib.pyplot as plt


def target_function(x, y):
    return x**2 + y**2, (x-2)**2 + (y-2)**2


# Создаем сетку точек для анализа
x = np.linspace(0, 4, 20)
y = np.linspace(0, 4, 20)
X, Y = np.meshgrid(x, y)

# Вычисляем значения критериев для каждой точки
Z1, Z2 = target_function(X, Y)

# Строим график с использованием цветной маркировки точек на границе Парето
plt.contourf(X, Y, Z1, cmap='Blues', levels=50, alpha=0.7)
plt.contourf(X, Y, Z2, cmap='Greens', levels=50, alpha=0.7)

# Находим точки на границе Парето и помечаем их красным цветом
efficient_frontier = []
for i in range(len(x)):
    for j in range(len(y)):
        Z1_val, Z2_val = target_function(x[i], y[j])
        is_efficient = True
        for k in range(len(x)):
            for l in range(len(y)):
                if target_function(x[k], y[l])[0] < Z1_val and target_function(x[k], y[l])[1] < Z2_val:
                    is_efficient = False
                    break
            if not is_efficient:
                break
        if is_efficient:
            efficient_frontier.append([x[i], y[j]])
efficient_frontier = np.array(efficient_frontier)
plt.scatter(efficient_frontier[:, 0], efficient_frontier[:, 1], color='gray', label='Граница Парето')

# Добавляем подписи и легенду
plt.xlabel('Критерий 1')
plt.ylabel('Критерий 2')
plt.title('График множества Парето с помощью EMOP')
plt.legend()

# Показываем график
plt.show()

if __name__ == "__main__":
    plt.show()