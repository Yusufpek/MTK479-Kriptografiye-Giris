from des_contstant import IP, S_BOXES, PC1, PC2, E, P


def int_to_bit(value, bit_length=8):
    result = ""
    while value > 1:
        result = str(value % 2) + result
        value = value // 2

    result = str(value) + result

    while len(result) < bit_length:
        result = "0" + result
    return result


def bit_to_int(bit_string):
    result = 0
    length = len(bit_string)
    for i in range(length):
        bit = bit_string[length - 1 - i]
        result += int(bit) * (2**i)
    return result


def xor(str_a, str_b):
    result = ""
    for i in range(len(str_a)):
        if str_a[i] == str_b[i]:
            result += "0"
        else:
            result += "1"
    return result


def get_plain_text(plain_text):
    while len(plain_text) < 8:
        plain_text += "0"

    plain_text = plain_text[:8]

    binary_string = ""
    for i in range(8):
        ascii_val = ord(plain_text[i])
        bits = int_to_bit(ascii_val)
        binary_string += bits
    return binary_string


def get_key(student_number):
    while len(student_number) < 8:
        student_number += "0"

    student_number = student_number[:8]

    key = ""
    for i in range(8):
        ascii_val = ord(student_number[i])
        bits = int_to_bit(ascii_val)
        key += bits
    return key


IP_INVERSE = [0] * 64


def generate_ip_inverse():
    for i, p in enumerate(IP):
        IP_INVERSE[p - 1] = i + 1


def permutate(input_bits, table):
    permutated_bits = ""
    for index in table:
        permutated_bits += input_bits[index - 1]
    return permutated_bits


def solve_sbox(input_bits, sbox):
    sbox = S_BOXES[sbox]
    row = bit_to_int(input_bits[0] + input_bits[5])
    col = bit_to_int(input_bits[1:5])
    value = sbox[row * 16 + col]
    output_bits = int_to_bit(value, bit_length=4)
    return output_bits


def left_shift(bits, shifts):
    return bits[shifts:] + bits[:shifts]


def des_key_generation(key):
    """64 bit keys to 48 bit subkey"""
    key = permutate(key, PC1)
    c0 = key[:28]
    d0 = key[28:]
    c1 = left_shift(c0, 1)
    d1 = left_shift(d0, 1)

    key = permutate(c1 + d1, PC2)
    return key


def f_function(right, subkey):
    expanded = permutate(right, table=E)
    print(f"Expanded Right {len(right)}-> {len(expanded)}:\t", expanded)

    xor_result = xor(expanded, subkey)
    print("XOR with Subkey:\t", xor_result)

    updated_right = ""
    for i in range(8):
        block = xor_result[i * 6 : (i + 1) * 6]
        sbox_output = solve_sbox(block, i)
        updated_right += sbox_output
        print(f"S-Box {i + 1} input:\t", block, "\toutput:\t", sbox_output)

    print("S Boxes Output:\t\t", updated_right)

    updated_right = permutate(updated_right, table=P)
    print("F Out:\t\t\t", updated_right)

    return updated_right


def round_des(plain_text, key):
    left = plain_text[:32]
    right = plain_text[32:]

    print("Left 0:\t\t\t", left)
    print("Right 0:\t\t", right)
    print("-" * 100)

    updated_right = xor(left, f_function(right, key))

    print("-" * 100)
    print("Left 1:\t\t\t", right)
    print("Right 1:\t\t", updated_right)
    return right + updated_right


name = "yusufipek"
student_number = "2220356048"

plain_text = get_plain_text(name)
key = get_key(student_number)

print("Name:\t\t\t", name)
print("Plain Text:\t\t", plain_text)
print("Student No:\t\t", student_number)
print("Key:\t\t\t", key)
print("-" * 100)


initial_permutation = permutate(plain_text, table=IP)
print("After IP:\t\t", initial_permutation)

key_round_1 = des_key_generation(key)
print("Round 1 Key:\t\t", key_round_1)
print("-" * 100)

first_round_result = round_des(initial_permutation, key_round_1)
print("-" * 100)
print("After Round 1:\t\t", first_round_result)

generate_ip_inverse()
cipher = permutate(first_round_result, table=IP_INVERSE)
print(f"Cipher bits ({len(cipher)}):\t", cipher)
