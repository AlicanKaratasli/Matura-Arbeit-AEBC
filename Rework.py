import random
import secrets
import math

input_text = input("Geben Sie hier den Text ein um diesen zu verschlüsseln: ")

binary_clear_text = []
for c in input_text:
    binary_clear_text.append(bin(ord(c))[2:])

# Testfall
print(binary_clear_text)

field_length = len(binary_clear_text)
if field_length < 10:
    field_length = 10

field_length = 9 ** math.ceil(math.log(field_length, 9))

print(field_length)

