def all_start_with_abc(text):
    return all(word[0].upper() in "ABCАВС" for word in text.split())


def main():
    print("YES" if all_start_with_abc(input("Введите слова: ")) else "NO")


if __name__ == "__main__":
    assert all_start_with_abc("apple Banana cat")
    assert not all_start_with_abc("apple dog")
    main()
