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

def upper_field(bytes):
    upper_field = {}
    for i in range(9):
        upper_field[f"UPPER_FIELD{i}"] = field(bytes[0][i])
    return upper_field

def pack_bytes(list):
    new_list = list
    for i in range(3):
        new_list = [new_list[i:i+9] for i in range(0, len(new_list), 9)]
    return new_list

def reorder_field(field, positions):
    new_field = []
    for i in range(len(positions)):
        new_field[i] = field[positions[i]]
    return new_field

def get_content(upper_field):
    content = []
    for field in upper_field:
        for lower_field in upper_field[field]:
            for i in range(9):
                content.append(upper_field[field][lower_field][f"SUBF{i}"])
    return content