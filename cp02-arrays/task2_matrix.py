import random

rows = int(input("Количество строк: "))
cols = int(input("Количество столбцов: "))
matrix = [[random.randint(-20, 20) for _ in range(cols)] for _ in range(rows)]

for row in matrix:
    print(" ".join(f"{v:4d}" for v in row))

print("Минимальный элемент:", min(min(row) for row in matrix))
if rows >= 2:
    print("Вторая строка:", matrix[1])
else:
    print("Второй строки нет")
print("Первый столбец:", [row[0] for row in matrix])
