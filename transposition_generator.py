import random

with open("Values.py", 'w') as file:
    file.write("transposition_list = ")
    used_randoms = []
    for i in range(256):
        x = random.sample(range(9),9)
        while x in used_randoms:
            x = random.sample(range(9),9)
        used_randoms.append(x)
    file.write(f"{used_randoms}")


