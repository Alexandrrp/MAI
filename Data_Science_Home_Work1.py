# Задача №1
# Считайте (через input) 2 числа:
# n - размер Numpy вектора;
# x - координата элемента вектора, который должен быть равен 1. Остальные должны быть равны 0.
# Создайте вектор размера n, в котором все элементы равны 0, кроме элемента с номером x - он равен 1.

import numpy as np

n, x = map(int, input("Введите размер матрицы через пробел ").split())
vec = np.zeros(n)
vec[x] = 1

print(vec)

# Задача №2
# Считайте 3 числа: n, m, s. Создайте Numpy вектор, состоящий из чисел от n до m с шагом s.

import numpy as np

n, m, s = map(int, input("Введите три числа через пробел ").split())

vec = np.arange(n, m, s)

print(vec)

# Задача №3
# Создайте матрицу 3х3 со значениями от 0 до 8. Значения нужно сгенерировать.

import numpy as np

matrix3 = np.random.randint(low=0, high=100, size=(3,3))
print(matrix3)

# Задача №4
# Создайте матрицу 4х4 со случайными значениями.
# Найдите максимальное значение первой строки, минимальное - второй, среднее - третьей, сумму - четвертой.

import numpy as np

array = np.random.rand(4, 4).round(2)
print(array)
print(f'max {np.max(array[0, :]).round(2)}')
print(f'min {np.min(array[1, :]).round(2)}')
print(f'mean {np.mean(array[2, :]).round(2)}')
print(f'sum {np.sum(array[3, :]).round(2)}')

# Задача №5
# Создайте диагональную матрицу 5х5, все ненулевые элементы равны 5.

import numpy as np

print(np.eye(5, 5))

# Задача №6
# Создайте Numpy массив случайных чисел размерности 6х6х6 и найдите максимальное значение среди всех элементов.

import numpy as np

matrix6 = np.random.rand(6,6,6)
print(matrix6)
print("Максимальное число: " + str(np.max(matrix6).round(4)))

# Задача №7
# Напишите функцию, которая принимает на вход 2 Numpy матрицы, проверяет, можно ли их перемножить, и если можно - то перемножает и возвращает транспонированную результирующую матрицу.

import numpy as np

def cond_and_mult_and_trans(A, B):
    if A.shape[1] == B.shape[0]:
        return print(np.transpose(A @ B))

    return print("Невозможно перемножать")
A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])

cond_and_mult_and_trans(A, B)

A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 2], [3, 4]])

cond_and_mult_and_trans(A, B)

# Задача №8
# Эту задачу можете как запрограммировать, так и решить на листочке.
#
# Но проще, конечно, запрограммировать.

import numpy as np

def func(x, y):
    return x*x + 2.0 * y*y + np.exp(x + y)

def f_x(func, x, y, eps=0.001):
    return (func(x+eps, y) - func(x, y)) / eps

def f_y(func, x, y, eps=0.001):
    return (func(x, y+eps) - func(x, y)) / eps
EPS = 0.001
INIT = np.array([1.0, -1.75])
LEARN_RATE = 0.05
ITER = 10000

X_prev = INIT
delta = 1
for i in range(ITER):
    if delta > EPS:
        fxx = f_x(func, X_prev[0], X_prev[1], eps=0.001)
        fyy = f_y(func, X_prev[0], X_prev[1], eps=0.001)
        grad = np.array([fxx, fyy])

        X_next = X_prev - LEARN_RATE * grad

        delta = np.sqrt(np.sum(grad*grad))

        X_prev = X_next

    else:
        break
print(f"Значение функции {func(X_next[0], X_next[1]).round(5)}")
print(f"x_min {X_next[0].round(5)}")
print(f"y_min {X_next[1].round(5)}")
print(f"Производная в x_min {f_x(func, X_next[0], X_next[1], eps=0.001).round(5)}")
print(f"Производная в y_min {f_y(func, X_next[0], X_next[1], eps=0.001).round(5)}")
print(f"Градиент {np.sqrt((grad**2).sum()).round(5)}")