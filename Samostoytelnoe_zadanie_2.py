#задание 1, первый способ.Допишите функцию, которая принимает 2 числа, сравнивает между собой и возвращает наименьшее.
a = input()
b = input()
if a < b:
    print(a)
else:
    print(b)

#задание 1 второй способ
a = input()
b = input()
c = min([a, b])
print(c)

#задание 2. Допишите функцию, которая принимает 3 числа, сравнивает между собой и возвращает наименьшее.
a = input()
b = input()
c = input()
d = min([a, b, c])
print(d)

#задание 3. Допишите функцию, которая принимает 3 числа, сравнивает между собой и возвращает количество совпадающих чисел. Соответственно, программа может возвращать одно из трех чисел: 3 - если совпадают все, 2 - если совпадают 2 числа, 0 - если все числа различны.
a = input()
b = input()
c = input()
if a == b and b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
