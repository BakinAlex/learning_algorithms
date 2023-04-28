def binary_search(list, item):
    """
    Поиск элемента в отсортированном списке с использованием алгоритма бинарного поиска.

    :param list: Отсортированный список элементов.
    :param item: Целое число, которое необходимо найти в списке.

    :return: Индекс элемента в списке, если он найден, иначе None.
    """
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [i for i in range(1, 133)]

print(binary_search(my_list, 55))
print(binary_search(my_list, 1253))
