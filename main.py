from random import randint
from typing import Sequence


def binary_search(arr: Sequence[int], value: int) -> tuple:
    """Функция бинарного поиска для поиска искомого значения."""

    right = len(arr) - 1
    left = 0
    counter = 0

    while left <= right:
        counter += 1
        center = (left + right) // 2

        if arr[center] == value:
            return counter, center, value

        if arr[center] < value:
            left = center + 1
        else:
            right = center - 1

    return counter, -1, None


def main():
    """Точка входа в программу."""
    rand_size = 100
    random_value = randint(0, rand_size - 1)
    array = tuple(range(rand_size))

    result_search = binary_search(array, random_value)

    print(f"Количество попыток: {result_search[0]}")
    print(f"Искомое : {result_search[1]}")
    print(f"Найденное : {result_search[2]}")


if __name__ == "__main__":
    main()
