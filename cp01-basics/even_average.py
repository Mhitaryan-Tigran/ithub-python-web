def even_average(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    return sum(evens) / len(evens)


def main():
    numbers = []
    while True:
        n = int(input())
        numbers.append(n)
        if n == 100:
            break
    print(f"Среднее арифметическое чётных чисел: {even_average(numbers):g}")


if __name__ == "__main__":
    assert even_average([3, 4, 7, 10, 100]) == 38
    main()
