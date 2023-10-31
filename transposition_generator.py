import random

#with open("Values.py", 'w') as file:
#    file.write("transposition_list = ")
#    used_randoms = []
#    for i in range(256):
#        x = random.sample(range(9),9)
#        while x in used_randoms:
#            x = random.sample(range(9),9)
#        used_randoms.append(x)
#    file.write(f"{used_randoms}")


#with open("Values.py", 'a') as file:
#    file.write("\nsubstitution_list = ")
#    sub_list = {}
#    used_randoms = []
#    for i in range(256):
#        x = random.randint(0,255)
#        while x in used_randoms or x == i:
#            x = random.randint(0,255)
#        used_randoms.append(x)
#        sub_list[(bin(i)[2:]).zfill(8)] = (bin(x)[2:]).zfill(8)
#    file.write(f"{sub_list}")

import Values as val

#with open("Values.py", 'a') as file:
#    file.write("\nreverse_substitution_list = ")
#    sub_list = val.substitution_list
#    reversed_dict = {value: key for key, value in sub_list.items()}
#    file.write(f"{reversed_dict}")

with open("test.py", 'a') as file:
    file.write("\ntransposition_list = ")
    used_randoms = []
    for i in range(256):
        x = random.sample(range(81),81)
        while x in used_randoms:
            x = random.sample(range(81),81)
        used_randoms.append(x)
    file.write(f"{used_randoms}")