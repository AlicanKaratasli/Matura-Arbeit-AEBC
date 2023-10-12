import random

used_randoms = []
for i in range(256):
    binary = bin(i)
    rand_bin = bin(random.randint(0,255))
    while rand_bin in used_randoms:
        rand_bin = bin(random.randint(0,255))
    else:
        used_randoms.append(rand_bin)
    binary = binary[2:]
    rand_bin = rand_bin[2:]
    binary = binary.zfill(8)
    rand_bin = rand_bin.zfill(8)
    print(f"{binary} is replaced with {rand_bin}")
