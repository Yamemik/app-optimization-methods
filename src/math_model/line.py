from pulp import *

# Создание модели
model = LpProblem("Minimize_Transport_Costs", LpMinimize)

# Переменные
x_A1 = LpVariable("x_A1", lowBound=0)
x_A2 = LpVariable("x_A2", lowBound=0)
x_A3 = LpVariable("x_A3", lowBound=0)
x_B1 = LpVariable("x_B1", lowBound=0)
x_B2 = LpVariable("x_B2", lowBound=0)
x_B3 = LpVariable("x_B3", lowBound=0)

# Целевая функция
model += 5 * x_A1 + 7 * x_A2 + 4 * x_A3 + 6 * x_B1 + 5 * x_B2 + 8 * x_B3

# Ограничения спроса
model += x_A1 + x_B1 == 50
model += x_A2 + x_B2 == 30
model += x_A3 + x_B3 == 20

# Ограничения запаса
model += x_A1 + x_A2 + x_A3 <= 100
model += x_B1 + x_B2 + x_B3 <= 80

# Решение задачи
model.solve()

# Вывод результатов
for variable in model.variables():
    print(f"{variable.name}: {variable.varValue}")

print(f"Минимальные затраты: {value(model.objective)}")
