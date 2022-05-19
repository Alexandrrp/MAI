# вывести третий символ этой строки.
row = "Lambdadambda"
print(row[2])

# Вывести предпоследний символ этой строки.
row = "Lambdadambda"
a = len(row)
print(row[11-1])

# Вывести первые пять символов этой строки.
row = "Lambdadambda"
i = 1
while i <= 5:
    print(row[i-1], end='')
    i = i + 1

# Вывести строку, кроме последних двух символов.
row = "Lambdadambda"
i = 1
while i <= len(row)-2:
    print(row[i-1], end='')
    i += 1

# Вывести все символы с четными индексами (считайте, что 0 - четный индекс).
row = "Lambdadambda"
i = 1
print(row[0],end='')
while i <= len(row)-1:
    if (i % 2) == 0:
        print(row[i], end='')
    i += 1

# Вывести все символы с нечетными индексами.
row = "Lambdadambda"
i = 1
while i <= len(row)-1:
    if (i % 2) == 1:
        print(row[i], end='')
    i += 1

# Вывести все символы в обратном порядке.
i = 1
row = "Lambdadambda"
while i <= len(row)-1:
    print(row[len(row)-1-i], end='')
    i += 1

# Вывести все символы строки через один в обратном порядке, начиная с последнего.
i = 0
row = 'Lambdadambda'
summa = ''
itog = ''
while i <= len(row)-1:
    if (i % 2) == 0:
        summa += row[i]
    i = i + 1
i = 0
while i <= len(summa)-1:
    itog += summa[len(summa)-1-(i)]
    i += 1
print(itog)

# Вывести длину данной строки.
row = "Lambdadambda"
print(len(row))