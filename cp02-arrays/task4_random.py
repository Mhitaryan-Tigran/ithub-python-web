import random

size = 15
numbers = [random.randint(1, 100) for _ in range(size)]
evens = [n for n in numbers if n % 2 == 0]

print("Массив:", numbers)
print("Делятся на 3:", sum(1 for n in numbers if n % 3 == 0))
print("Среднее арифметическое чётных:", round(sum(evens) / len(evens), 2) if evens else "чётных чисел нет")
