def modulo_hundred(number, power):
    result = number % 100

    while power > 1:
        result = (result * number) % 100
        power -= 1
    return result


print(modulo_hundred(328, 2021))
