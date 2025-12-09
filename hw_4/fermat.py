import math


def is_square(n):
    k = math.sqrt(n)
    try:
        int(k)
        return True
    except ValueError:
        return False


# m = pq = (x-y)(x+y) = x^2 - y^2
# y^2 = x^2 - m
# y = ceil(sqrt(x^2 - m))
def fermat_factorization(m):
    r = math.ceil(math.sqrt(m))
    k = r * r - m

    while not is_square(k):
        r += 1
        k = r * r - m
        print(f"r = {r}, r^2 - m = {k} (tam kare değil)")

    y = int(math.sqrt(k))
    print(f"r = {r}, r^2 - m = {k} (tam kare)")
    print(f"X = {r}, Y = {y}")
    p = r - y
    q = r + y
    print(f"p = X - Y = {p}")
    print(f"q = X + Y = {q}")
    return p, q


if __name__ == "__main__":
    p, q = fermat_factorization(56153)
    print(f"56153 = {p} * {q}")
