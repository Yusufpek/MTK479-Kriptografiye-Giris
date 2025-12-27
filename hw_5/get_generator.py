def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_generator(z):
    p = z
    while not is_prime(p):
        p -= 1

    n = p - 1
    print("Asal p =", p, end=", ")
    print("n =", n)

    for g in range(2, p):
        is_found = True
        print("Denenen g =", g)
        for k in range(2, n + 1):
            if n % k == 0:
                if pow(g, n // k) % p == 1:
                    print("g^{} mod {} == 1".format(n // k, p))
                    is_found = False
                    break
                else:
                    print("g^{} mod {} != 1".format(n // k, p))
        if is_found:
            return g
    return -1


def get_generator_count(z):
    founded = set()
    p = z
    while not is_prime(p):
        p -= 1

    n = p - 1

    for g in range(2, p):
        is_found = True
        for k in range(2, n + 1):
            if n % k == 0:
                if pow(g, n // k) % p == 1:
                    is_found = False
                    break
        if is_found:
            founded.add(g)
    return len(founded), founded


if __name__ == "__main__":
    z = 71
    g = get_generator(z)
    print("Üreteç g =", g)
    count, generators = get_generator_count(z)
    print("Toplam üreteç sayısı =", count)
    print("Üreteçler =", generators)
