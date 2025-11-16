import math


def find_period(x, mod):
    if x % mod == 0:
        return x

    power = 1
    number = x
    while number % mod != 1:
        number *= x
        power += 1
        print(f"Current number: {number} at power: {power} mod {mod} = {number % mod}")

    return power


def find_modulo(number, power, mod):
    print(f"Finding modulo for number: {number}, power: {power}, mod: {mod}")
    period = find_period(number, mod)
    effective_power = power % period
    if effective_power == 0:
        effective_power = period

    num = int(math.pow(number, effective_power))
    print(f"Computed {number}^{effective_power}: {num} mod {mod}: {num % mod}")
    return num % mod


def summation_modulo(numbers, powers, mod):
    total = 0
    for i in range(len(numbers)):
        total += find_modulo(numbers[i], powers[i], mod)
    return total % mod


numbers = [2, 3, 4, 5, 6]
power = [20, 30, 40, 50, 60]

print(summation_modulo(numbers, power, 7))
