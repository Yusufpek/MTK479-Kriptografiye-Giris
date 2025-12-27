def get_points(a, b, z):
    # y^2 = x^3 + ax + b
    points = []
    for x in range(z):
        potential_y = (x**3 + a * x + b) % z
        for y in range(z):
            if (y * y) % z == potential_y:
                points.append((x, y))
    points.append("O")  # sonsuzluktaki nokta
    return points


if __name__ == "__main__":
    a = 3
    b = 5
    z = 19
    points = get_points(a, b, z)
    print("Eliptik Eğri Noktaları Z{} üzerinde:".format(z))
    for point in points:
        print(point)
