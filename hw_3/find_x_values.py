"""
x = 2 mod 3
x = 3 mod 4
x = 4 mod 5
"""

def find_x_values():
    x_values = []
    for x in range(1, 60):
        if (x % 3 == 2) and (x % 4 == 3) and (x % 5 == 4):
            x_values.append(x)
    return x_values

print(find_x_values())

