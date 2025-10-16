from itertools import permutations

block_size = 5
cipher_text = "TKREUYASNIAOINTBDIGRIEGANSRENTEORPUEDNWAEETRSNISAA"

cipher_blocks = [
    cipher_text[i : i + block_size] for i in range(0, len(cipher_text), block_size)
]


for i in permutations(range(block_size)):
    permutated_blocks = [
        "".join(cipher_blocks[n][k] for k in i) for n in range(len(cipher_blocks))
    ]

with open("permutation_output.txt", "w") as f:
    for i in permutations(range(block_size)):
        permutated_blocks = [
            "".join(cipher_blocks[n][k] for k in i) for n in range(len(cipher_blocks))
        ]
        decrypted_text = " ".join(permutated_blocks)
        f.write(f"Permutation: {i} -> {decrypted_text}\n")

# Permutation: (0, 4, 2, 1, 3) -> TURKE YISAN ATION BRIDG INGEA STERN EUROP EANDW ESTER NASIA
plain_text = "TURKEYISANATIONBRIDGINGEASTERNEUROPEANDWESTERNASIA"
formatted_plain_text = "TURKEY IS A NATION BRIDGING EASTERN EUROPE AND WESTERN ASIA"
