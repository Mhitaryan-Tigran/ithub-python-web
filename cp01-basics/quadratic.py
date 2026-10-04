import math


def solve(a, b, c):
    if a == 0:
        if b == 0:
            return "любое число" if c == 0 else None
        return (-c / b,)
    d = b * b - 4 * a * c
    if d < 0:
        return None
    if d == 0:
        return (-b / (2 * a),)
    root = math.sqrt(d)
    return ((-b + root) / (2 * a), (-b - root) / (2 * a))


def main():
    print("Решение уравнения ax² + bx + c = 0")
    a, b, c = (float(input(f"{name} = ")) for name in "abc")
    roots = solve(a, b, c)
    if roots is None:
        print("Уравнение не имеет действительных корней")
    elif isinstance(roots, str):
        print("Корнем является любое число")
    elif len(roots) == 1:
        print(f"Один корень: x = {roots[0]:g}")
    else:
        print(f"Два корня: x1 = {roots[0]:g}, x2 = {roots[1]:g}")


if __name__ == "__main__":
    assert solve(1, -3, 2) == (2.0, 1.0)
    assert solve(1, 2, 1) == (-1.0,)
    assert solve(1, 0, 1) is None
    main()
