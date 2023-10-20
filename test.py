import random
import secrets

#Verlangt die erwünschte Plain Text zu Verschlüsseln
alphabetisch = input("Sie können hier ihr Text schreiben, " \
                      "welchen Sie gerne verschlüsselt haben möchten:")
#Verwandelt alles in Binär und erstellt die Liste e
def binar(alphabetisch):
    a, b = [], []
    for i in alphabetisch:
        a.append(ord(i))
    for i in a:
        b.append((bin(i)[2:]).zfill(8))
    return b
e = binar(alphabetisch)
print (e)
global z
z = 0
for i in e:
    z = z + 1
print(z)
print(len(e))
for i in range(81 - len(e)):
    zufzhl = random.randint(129, 255)
    e.append(bin(zufzhl)[2:])
    z = 81
print(e)



#SUBSTITUTION-BOX
#TRANSPOSITION SHIFTS
#Key generation
def schlüsselgenerator():
    schlüssel_länge_bytes = 16
    key = secrets.token_bytes(schlüssel_länge_bytes)
    return key
def bytes_zu_binary(byte_str):
    return "".join(f"{byte:08b}" for byte in byte_str)
def keykleinermachen(key_str):
    smaller_keys = [key_str[i:i+8] for i in range(0, len(key_str), 8)]
    return smaller_keys
schlüssel = schlüsselgenerator()
binärer_schlüssel = bytes_zu_binary(schlüssel)
smaller_keys = keykleinermachen(binärer_schlüssel)
for i, key in enumerate(smaller_keys, 1):
    globals()[f"key{i}"] = key
print(binärer_schlüssel)
print(key1)
print(key2)
print(key3)
print(key4)
print(key5)
print(key6)
print(key7)
print(key8)
print(key9)


#DISPLACEMENT

#KEY INFUSION
#Transposition shifts

#Key infusion
