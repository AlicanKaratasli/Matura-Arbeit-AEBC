import random
x = bin(random.randint(129, 255))[2:]
y = format(random.randint(129, 255), '08b')

print(type(x))
print(x)
print(type(y))
print(y)
