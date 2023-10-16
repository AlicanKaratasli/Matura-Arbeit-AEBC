import random
import secrets

#Verlangt die erwünschte Plain Text zu Verschlüsseln
alphabetisch = input ("Sie können hier ihr Text schreiben, "
                      "welchen Sie gerne verschlüsselt haben möchten:")
#Verwandelt alles in Binär und erstellt die Liste e
def binar (alphabetisch):
    a , b = [], []
    for i in alphabetisch:
        a.append(ord(i))
    for i in a:
        b.append((bin(i)[2:]).zfill(8))
    return b
e = binar (alphabetisch)
print (e)
global z
z = 0
for i in e:
    z = z + 1

for i in range(81 - len(e)):
    zufzhl = random.randint(129, 255)
    e.append(bin(zufzhl)[2:])
    z = 81
print(e)
