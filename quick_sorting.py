import random


def quick_sort(array: list) -> list:
    """
    Сортировка списка с использованием алгоритма быстрой сортировки.

    :param array: Список чисел.

    :return: Отсортированный список.
    """
    if len(array) < 2:
        return array
    else:
        prop = array[len(array) // 2]
        less = [_ for _ in array[1:] if _ <= prop]
        greater = [_ for _ in array[1:] if _ > prop]
        return quick_sort(less) + [prop] + quick_sort(greater)


my_list = [random.randint(1, 133) for _ in range(12)]
print(my_list)
print(quick_sort(my_list))
