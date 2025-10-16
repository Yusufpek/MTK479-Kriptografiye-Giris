import numpy
from math import gcd

# alphabet mapping
letter_map = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
}

plain_text = "kriptografiyegirisdersia"
cipher_text = "xyhhnqnazgprakmadrlxbysq"


def mod_inverse(x):
    for i in range(1, 26):
        if (x * i) % 26 == 1:
            return i
    return None


def get_matrix_with_blocks(text, block_size):
    matrix = []
    for i in range(0, len(text), block_size):
        row = [letter_map[text[i + j]] for j in range(block_size)]
        matrix.append(row)
    return numpy.array(matrix)


plain_matrix = get_matrix_with_blocks(plain_text, 3)
cipher_matrix = get_matrix_with_blocks(cipher_text, 3)

# try for key
found = False
for i in range(len(plain_matrix)):
    row_i = plain_matrix[i]
    for j in range(i + 1, len(plain_matrix)):
        row_j = plain_matrix[j]
        for k in range(j + 1, len(plain_matrix)):
            row_k = plain_matrix[k]
            test_matrix = numpy.array([row_i, row_j, row_k], dtype=int)
            determinant = int(round(numpy.linalg.det(test_matrix))) % 26
            if determinant != 0 and gcd(determinant, 26) == 1:
                print(f"rows: {i}, {j}, {k} det: {determinant}")
                plain_matrix = test_matrix
                cipher_matrix = numpy.array(
                    [cipher_matrix[i], cipher_matrix[j], cipher_matrix[k]],
                    dtype=int,
                )
                found = True
                break
        if found:
            break
    if found:
        break

if found:
    inverse_plain = numpy.linalg.inv(plain_matrix)
    det_inverse = mod_inverse(determinant)

    if det_inverse:
        adjugate = numpy.rint(
            numpy.linalg.det(plain_matrix) * numpy.linalg.inv(plain_matrix)
        ).astype(int)  # randint
        inverse_plain = (det_inverse * adjugate) % 26

        print("Plain matrix:")
        print(plain_matrix)

        print("Inverse plain matrix:")
        print(inverse_plain)

        print("Cipher matrix:")
        print(cipher_matrix)

        key_matrix = numpy.dot(cipher_matrix, inverse_plain) % 26
        print("Key matrix:")
        print(key_matrix)
    else:
        print("Could not find modular inverse of determinant")

else:
    print("Could not find invertible matrix")
