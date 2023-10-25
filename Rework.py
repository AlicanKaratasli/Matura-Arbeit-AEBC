import random
import secrets
import math
import Functions as func

input_text = "Hallo" # input("Geben Sie hier den Text ein um diesen zu verschlüsseln: ")

binary_clear_text = []
for c in input_text:
    binary_clear_text.append(bin(ord(c))[2:])

# Testfall
print(binary_clear_text)

field_length = len(binary_clear_text)

if field_length < 10:
    field_length = 82

field_size = math.ceil(math.log(field_length, 9))
field_length = 9 ** field_size

# Testfall
print(field_size)
print(field_length)

field_content = binary_clear_text

for i in range(len(binary_clear_text), field_length):
    field_content.append(format(random.randint(129, 255), '08b'))

packed_content = func.pack_bytes(field_content, field_size)

field = func.upper_field("UPPER_FIELD", packed_content)

# Testfall
print(field)