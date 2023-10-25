def lower_field(bytes):
    lower_field = {}
    for i in range(9):
        lower_field[f"SUBF{i}"] = [bytes[i]]
    return lower_field

def field(bytes):
    field = {}
    for i in range(9):
        field[f"FIELD{i}"] = lower_field(bytes[i])
    return field

def upper_field(name, bytes):
    upper_field = {}
    for i in range(9):
        upper_field[f"{name}{i}"] = field(bytes[0][i])
    return upper_field

def pack_bytes(list, depth):
    new_list = list
    for i in range(depth):
        new_list = [new_list[i:i+9] for i in range(0, len(new_list), 9)]
    return new_list