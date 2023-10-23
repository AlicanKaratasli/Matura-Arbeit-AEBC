def field():
    field = {}
    for i in range(9):
        field[f"SUBF{i}"] = []
    return field

def superfield():
    superfield = {}
    for i in range(9):
        superfield[f"field{i}"] = [f"{field()}{i}"]
    return superfield