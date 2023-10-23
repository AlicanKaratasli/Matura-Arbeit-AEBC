import random
import secrets

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

print(schlüssel, binärer_schlüssel, smaller_keys)