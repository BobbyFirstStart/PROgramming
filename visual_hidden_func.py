import pickle
import numpy as np
import matplotlib.pyplot as plt

file_path = "data_to_decrypt.bin"
file = open(file_path, "rb")
loaded_data = pickle.load(file)
file.close()

X = loaded_data['x_train']
Y = loaded_data['y_train']


degree = 3

# МНК для полиномиальной регрессии
coefficients = np.polyfit(X, Y, degree)

# Создаем полиномиальную модель на основе коэффициентов
polynomial_model = np.poly1d(coefficients)

# значения для графика
x_values = np.linspace(min(X), max(X), 100)
y_values = polynomial_model(x_values)

# Вывод
plt.scatter(X, Y, label='Данные')
plt.plot(x_values, y_values, label='Полиномиальная регрессия', color='red')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
