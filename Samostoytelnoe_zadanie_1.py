a = True
b = False
result1 = a and b
print(result1)
result2 = (a and b) or b
print(result2)
result3 = (a and b) or not (a and b)
print(result3)
result4 = a and b or not (a or b) or b
print(result4)
result5 = b and b or not a and (a or b or a) or not (a or b)
print(result5)

print(1 << 2)
print(1 & 0 | 1 >> 1)
print(1 & 0 | 1 >> 0)
print(0b101 & 0b111 ^ 0b111 | 0b010) # числа в двоичной системе: 0b101=5, 0b111=6, 0b010=2