def discriminant(a: int, b: int, c: int) -> int:
    return b ** 2 - 4 * a * c


def quadratic_equation(a: int, b: int, c: int) -> str | float | tuple[float, float]:
    d = discriminant(a, b, c)
    if d < 0:
        return "Корней нет"
    elif d == 0:
        return round(-b / (2 * a), 2)
    else:
        x1 = round((-b + d ** 0.5) / (2 * a), 2)
        x2 = round((-b - d ** 0.5) / (2 * a), 2)
        return x1, x2


if __name__ == '__main__':
    print(quadratic_equation(1, 8, 15))
    print(quadratic_equation(1, -13, 12))
    print(quadratic_equation(4, 2, -3))

    print(quadratic_equation(-4, 28, -49))
    print(quadratic_equation(2, 4, 2))

    print(quadratic_equation(1, 1, 1))
    print(quadratic_equation(3, -5, 3))
