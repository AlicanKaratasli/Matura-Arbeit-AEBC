def lower_field():
    lower_field = {}
    for i in range(9):
        lower_field[f"SUBF{i}"] = []
    return lower_field

def field():
    field = {}
    for i in range(9):
        field[f"FIELD{i}"] = lower_field()
    return field

def upper_field(name):
    upper_field = {}
    for i in range(9):
        upper_field[f"{name}{i}"] = field()