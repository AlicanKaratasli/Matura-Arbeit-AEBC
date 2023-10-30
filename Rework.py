import random
import secrets
import math
import Functions as func
import Values as val

input_text = "Hallo" # input("Geben Sie hier den Text ein um diesen zu verschlüsseln: ")

binary_clear_text = []
for c in input_text:
    binary_clear_text.append(bin(ord(c))[2:])

field_length = 1300 #len(binary_clear_text)
oversized = False

if field_length < 729: field_length = 729
else : 
    oversized = True
    oversize_count = (field_length // 729) + 1
    field_length = oversize_count * 729

field_content = binary_clear_text

for i in range(len(binary_clear_text), field_length):
    field_content.append(format(random.randint(129, 255), '08b'))

if not oversized:
    packed_content = func.pack_bytes(field_content)
    field_list = func.upper_field(packed_content)
else:
    packed_content = [func.pack_bytes(field_content[i:i+729]) for i in range(0, field_length, 729)]
    field_list = {}
    for i in range(oversize_count):
        field_list[f"COMPLETE_FIELD{i}"] = func.upper_field(packed_content[i])
