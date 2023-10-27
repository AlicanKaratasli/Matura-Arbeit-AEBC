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

field_length = 18000
oversized = False

if field_length < 729: field_length = 729
else : 
    oversized = True
    oversize_count = (field_length // 729) + 1
    field_length = oversize_count * 729
        
        
# Testfall
print(field_length)

field_content = binary_clear_text

for i in range(len(binary_clear_text), field_length):
    field_content.append(format(random.randint(129, 255), '08b'))

if not oversized:
    packed_content = func.pack_bytes(field_content)
    field = func.upper_field(packed_content)



# Testfall
print(field_content)
print(len(field_content))


# Testfall
#print(field)