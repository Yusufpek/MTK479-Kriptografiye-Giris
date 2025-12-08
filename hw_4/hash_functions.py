def hash1(a, n):
    sum = 0
    for x in a:
        sum += x % n
        sum %= n
    return sum % n


def hash2(a, n):
    sum = 0
    for x in a:
        sum += (x % n) * (x % n)
        sum %= n
    return sum % n


if __name__ == "__main__":
    # Değişken Mesaj Uzunluğu
    print("Değişken Mesaj Uzunluğu")
    print("-" * 30)
    print("Hash1 Değişken Mesaj Uzunluğu:")
    print("Hash1:", hash1([328], 100))
    print("Hash1:", hash1([328, 2021], 100))

    print("Hash2 Değişken Mesaj Uzunluğu:")
    print("Hash2:", hash2([328], 100))
    print("Hash2:", hash2([328, 2021], 100))

    print("-" * 30)
    print("Sabit Çıktı Uzunluğu")
    print("-" * 30)
    n = 100
    print("Hash1:", hash1([1, 2, 3, 4, 5], n))
    print("Hash2:", hash2([1, 2, 3, 4, 5], n))

    print("-" * 30)
    print("Pre-Image Resistant")
    print("-" * 30)
    n = 100
    target_hash = 44

    # For hash1
    res1 = []
    for x in range(n):
        for y in range(n):
            if hash1([x, y], n) == target_hash:
                if not res1:
                    print("First Pre-image for Hash1:", [x, y])
                res1.append([x, y])

    if not res1:
        print("No pre-image found for Hash1")

    # For hash2
    res2 = []
    for x in range(n):
        for y in range(n):
            if hash2([x, y], n) == target_hash:
                if not res2:
                    print("First Pre-image for Hash2:", [x, y])
                res2.append([x, y])

    if not res2:
        print("No pre-image found for Hash2")

    print(f"{len(res1)} Pre-images found for Hash1")
    print(f"{len(res2)} Pre-images found for Hash2")
    print("Pre-images for Hash1:", res1)
    print("Pre-images for Hash2:", res2)

    print("-" * 30)
    print("Second Pre-Image Resistant")
    print("-" * 30)
    n = 100
    a = [25, 50]

    # For hash1
    res1 = []
    original_hash = hash1(a, n)
    print("Target Hash for Hash1:", original_hash)
    for x in range(n):
        for y in range(n):
            if hash1([x, y], n) == original_hash and [x, y] != a:
                if not res1:
                    print("Second Pre-image for Hash1:", [x, y])
                res1.append([x, y])

    if not res1:
        print("No second pre-image found for Hash1")

    # For hash2
    res2 = []
    original_hash = hash2(a, n)
    print("Target Hash for Hash2:", original_hash)
    for x in range(n):
        for y in range(n):
            if hash2([x, y], n) == original_hash and [x, y] != a:
                if not res2:
                    print("Second Pre-image for Hash2:", [x, y])
                res2.append([x, y])

    if not res2:
        print("No second pre-image found for Hash2")

    print(f"{len(res1)} Second Pre-images found for Hash1")
    print(f"{len(res2)} Second Pre-images found for Hash2")
    print("Second Pre-images for Hash1:", res1)
    print("Second Pre-images for Hash2:", res2)

    print("-" * 30)
    print("Collision Resistant")
    print("-" * 30)

    n = 100
    # hash1
    col1 = []
    for x in range(n):
        for y in range(x + 1, n):
            if hash1([x, x + 1], n) == hash1([y, y + 1], n):
                col1.append((x, y))

    # hash2
    col2 = []
    for x in range(n):
        for y in range(x + 1, n):
            if hash2([x, x + 1], n) == hash2([y, y + 1], n):
                col2.append((x, y))
                break

    print(f"{len(col1)} Collisions found for Hash1")
    print(f"{len(col2)} Collisions found for Hash2")
    print("Collisions for Hash1:", col1)
    print("Collisions for Hash2:", col2)
