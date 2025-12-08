def miller_rabin_test_prime(number, t):
    if number <= 1:
        return False

    if number <= 3:
        return True

    if number % 2 == 0:
        return False

    # n-1 = 2^s * r
    r, s = number - 1, 0
    while r % 2 == 0:
        r //= 2
        s += 1

    print(number)
    print(f"n-1 = {number - 1} = 2^{s} * {r}", end=" ")
    print(f"s = {s}, r = {r}")

    for i in range(1, t):
        a = 2
        y = pow(a, r) % number

        if y != 1 and y != number - 1:
            j = 1
            while j <= s - 1 and y != number - 1:
                y = pow(y, 2) % number
                if y == 1:
                    return False
                j += 1
            if y != number - 1:
                return False
    return True


if __name__ == "__main__":
    test_numbers = [233, 237, 241]
    for num in test_numbers:
        if miller_rabin_test_prime(num, 3):
            print(f"{num} asal.")
            print("-" * 20)
        else:
            print(f"{num} bileşik.")
            print("-" * 20)

