def print_hello(name):
    print(f"Hello, {name}!")


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
