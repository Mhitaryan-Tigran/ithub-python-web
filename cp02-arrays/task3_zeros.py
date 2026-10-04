def has_two_zeros(items):
    return any(a == 0 and b == 0 for a, b in zip(items, items[1:]))


def main():
    size = int(input("Количество элементов: "))
    items = [int(input(f"Элемент {i + 1}: ")) for i in range(size)]
    print("Есть два нуля подряд" if has_two_zeros(items) else "Двух нулей подряд нет")


if __name__ == "__main__":
    assert has_two_zeros([1, 0, 0, 5])
    assert not has_two_zeros([0, 1, 0])
    main()
