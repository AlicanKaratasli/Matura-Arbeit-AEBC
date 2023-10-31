import Values as val

def lower_field(bytes):
    lower_field = {}
    for i in range(9):
        lower_field[f"SUBF{i}"] = bytes[i]
    return lower_field

def field(bytes):
    field = {}
    for i in range(9):
        field[f"FIELD{i}"] = lower_field(bytes[i*9:i*9+9])
    return field

def pack_bytes(input_list):
    new_list = []
    for i in range(0, len(input_list), 9):
        new_list.append(input_list[i:i+9])
    return new_list

def get_content(field):
    content = []
    for lower_field in field:
            for i in range(9):
                content.append(field[lower_field][f"SUBF{i}"])
    return content

def reorder_field(field, positions):
    new_field = []
    for i in range(9):
        new_field.append(field[positions[i]])
    return new_field

def re_reorder_field(field, positions):
    new_list = [None] * 9
    for i in range(9):
        new_list[positions[i]] = field[i]
    return new_list

def substitute(bytes):
    new_bytes = []
    for i in range(len(bytes)):
        try: new_bytes.append(val.substitution_list[f"{bytes[i]}"])
        except: new_bytes.append(bytes[i])
    return new_bytes

def reverse_substitute(bytes):
    new_bytes = []
    for i in range(len(bytes)):
        new_bytes.append(val.reverse_substitution_list[f"{bytes[i]}"])
    return new_bytes

def transpose_field(field, pos_list):
    content = get_content(field)
    new_field = []
    for i in range(81):
        new_field.append(content[pos_list[i]])
    return new_field

def retranspose_field(field, pos_list):
    content = get_content(field)
    new_field = [None] * 81
    for i in range(81):
        new_field[pos_list[i]] = content[i]
    return new_field