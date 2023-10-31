import random
import secrets
import numpy as np
import Functions as func
import Values as val

print(f"Willkommen zum AEBC Encryption Tool. Bitte wählen Sie die gewünschte Funktion aus:\n[E]ncrypt oder [D]ecrypt")
encrypt = None
while True:
    if encrypt == 'E' or encrypt == 'e':
        input_text = input("Geben Sie hier den Text ein um diesen zu verschlüsseln: ")

        binary_clear_text = []
        for c in input_text:
            binary_clear_text.append((bin(ord(c))[2:]).zfill(8))

        field_length = len(binary_clear_text)
        oversized = False

        if field_length < 729: field_length = 729
        else : 
            oversized = True
            oversize_count = (field_length // 729) + 1
            field_length = oversize_count * 729

        field_content = binary_clear_text

        for i in range(len(binary_clear_text), field_length):
            field_content.append(format(random.randint(129, 255), '08b'))

        #Key Generation Test
        Key = secrets.randbits(8)
        print("\nIhr Schlüssel ist: ", Key)

        if not oversized:
            field_list = {}
            packed_content = func.pack_bytes(field_content)
            field_list["COMPLETE_FIELD0"] = func.field(packed_content)
        else:
            packed_content = [func.pack_bytes(field_content[i:i+729]) for i in range(0, field_length, 729)]
            field_list = {}
            for i in range(oversize_count):
                field_list[f"COMPLETE_FIELD{i}"] = func.field(packed_content[i])
        for _ in range(9):
            for field in field_list:
                #S-Box
                flat_list = np.array(func.get_content(field_list[field]))
                flat_list = flat_list.ravel().tolist()
                substituted_list = func.substitute(flat_list)
                field_list[field] = func.field(func.pack_bytes(substituted_list))

                #Displacement
                for i in range(9):
                    for j in range(9):
                        field_list[field][f"FIELD{i}"][f"SUBF{j}"] = func.reorder_field(field_list[field][f"FIELD{i}"][f"SUBF{j}"], val.displacement_list[Key])

                #Transposition
                transposed_field = func.transpose_field(field_list[field], val.transposition_list[Key])
                field_list[field] = func.field(transposed_field)

                #Key Infusion
                infusion_field = np.array(func.get_content(field_list[field]))
                infusion_field = infusion_field.ravel().tolist()

                elements = []
                for element in infusion_field:
                    elements.append(int(element, 2) ^ Key)
                for i in range(len(elements)):
                    elements[i] = (bin(int(elements[i]))[2:]).zfill(8)

                field_list[field] = func.field(func.pack_bytes(elements))
        output = np.array(func.get_content(field_list[field]))
        output = output.ravel().tolist()
        while True:
            print_or_file = input("\nMöchten sie den verschlüsselten Text in die Datei \"encrypted.txt\" abspeichern? [Y]/[N]\n")
            if print_or_file == 'N' or print_or_file == 'n':
                print("\nIhr verschlüsselter Text:")
                print(", ".join(map(str, output)))
                break
            elif print_or_file == 'Y' or print_or_file == 'y':
                with open("encrypted.txt", 'w') as file:
                    file.write(", ".join(map(str, output)))
                    print("Datei wurde erfolgreich beschrieben.")
                break
            else:
                print("Eingabe nicht erkannt")
                continue
                    
        break
    elif encrypt == 'D' or encrypt == 'd':
        Key = input("Bitte geben sie den Schlüssel ein: ")
        try: 
            Key = int(Key)
        except:
            print("Schlüssel muss eine Zahl zwischen 0 und 255 sein.")
            continue
        field_content = []
        while True:
            read_file = input("\nMöchten sie den verschlüsselten Text von der Datei \"encrypted.txt\" auslesen? [Y]/[N]\n")
            if read_file == 'N' or read_file == 'n':
                field_content = input("Bitte geben sie den zu entschlüsselden Text ein:")
                field_content = field_content.split(", ")
                break
            elif read_file == 'Y' or read_file == 'y':
                with open("encrypted.txt", 'r') as file:
                    field_content = file.readline()
                    field_content = field_content.split(", ")
                    print("Datei wurde erfolgreich ausgelesen.")
                break
            else:
                print("Eingabe nicht erkannt")
                continue
        print(field_content)

        field_length = len(field_content)
        oversized = False

        if field_length < 730: field_length = 729
        else : 
            oversized = True
            oversize_count = (field_length // 729) + 1
            field_length = oversize_count * 729
        
        if not oversized:
            field_list = {}
            packed_content = func.pack_bytes(field_content)
            field_list["COMPLETE_FIELD0"] = func.field(packed_content)
        else:
            packed_content = [func.pack_bytes(field_content[i:i+729]) for i in range(0, field_length, 729)]
            field_list = {}
            for i in range(oversize_count):
                field_list[f"COMPLETE_FIELD{i}"] = func.field(packed_content[i])

        ###
        for _ in range(9):
            for field in field_list:
                #Key Infusion should work by itself
                infusion_field = np.array(func.get_content(field_list[field]))
                infusion_field = infusion_field.ravel().tolist()

                elements = []
                for element in infusion_field:
                    elements.append(int(element, 2) ^ Key)
                for i in range(len(elements)):
                    elements[i] = (bin(int(elements[i]))[2:]).zfill(8)

                field_list[field] = func.field(func.pack_bytes(elements))
                
                #Transposition
                transposed_field = func.retranspose_field(field_list[field], val.transposition_list[Key])
                field_list[field] = func.field(transposed_field)

                #Displacement
                for i in range(9):
                    for j in range(9):
                        field_list[field][f"FIELD{i}"][f"SUBF{j}"] = func.re_reorder_field(field_list[field][f"FIELD{i}"][f"SUBF{j}"], val.displacement_list[Key])

                #S-Box should work
                flat_list = np.array(func.get_content(field_list[field]))
                flat_list = flat_list.ravel().tolist()
                substituted_list = func.reverse_substitute(flat_list)
                field_list[field] = func.field(func.pack_bytes(substituted_list))

        output = np.array(func.get_content(field_list[field]))
        output = output.ravel().tolist()
        print(output)
        ###

        break
    encrypt = input()
    if encrypt == None:
        continue
    elif encrypt != None and encrypt != 'E' and encrypt != 'e' and encrypt != 'D' and encrypt != 'd':
        print("Eingabe nicht erkannt")
    

