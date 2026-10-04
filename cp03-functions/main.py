from greetings import gcd, print_hello

string = "Yandex"
print_hello(string)

result = gcd(12, 45)
print(f"result = {result}")

assert gcd(12, 45) == 3
assert gcd(17, 5) == 1
assert gcd(48, 18) == 6
