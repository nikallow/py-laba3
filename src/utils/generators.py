import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """
    Генерирует массив случайных целых чисел.

    :param n: Количество элементов в массиве
    :param lo: Нижняя граница диапазона
    :param hi: Верхняя граница диапазона
    :param distinct: Все элементы уникальные
    :param seed: Seed рандома
    :return: Список случайных целых чисел
    :raises ValueError: If impossible gen n уникальных элементов в заданном диапазоне
    """
    rng = random.Random(seed)

    if distinct:
        if (hi - lo + 1) < n:
            raise ValueError(
                f"Невозможно сгенерировать {n} уникальных элементов на [{lo}, {hi}]"
            )
        else:
            return rng.sample(range(lo, hi + 1), n)

    return [random.randint(lo, hi) for _ in range(n)]


def rand_float_array(
    n: int, lo: float = 0.0, hi: float = 1.0, *, seed=None
) -> list[float]:
    """
    Генерирует массив случайных вещественных чисел.

    :param n: Количество элементов в массиве
    :param lo: Нижняя граница диапазона
    :param hi: Верхняя граница диапазона
    :param seed: Seed рандома
    :return: Список случайных вещественных чисел
    """
    rng = random.Random(seed)

    return [rng.uniform(lo, hi) for _ in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Генерирует почти отсортированный массив.

    :param n: Количество элементов в массиве
    :param swaps: Количество случайных обменов
    :param seed: Seed рандома
    :return: Почти отсортированный список целых чисел
    """
    rng = random.Random(seed)

    arr = list(range(n))

    for _ in range(swaps):
        i, j = rng.randint(0, n - 1), random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """
    Генерирует массив с большим количеством повторяющихся элементов.

    :param n: Количество элементов в массиве
    :param k_unique: Количество уникальных значений
    :param seed: Seed рандома
    :return: Список с большим количеством дубликатов
    """
    rng = random.Random(seed)

    unique_values = list(range(k_unique))
    return [rng.choice(unique_values) for _ in range(n)]


def reverse_sorted(n: int) -> list[int]:
    """
    Генерирует массив, отсортированный в обратном порядке.

    :param n: Количество элементов в массиве
    :return: Массив, отсортированный по убыванию [n-1, n-2, ..., 0]
    """
    return list(range(n - 1, -1, -1))
