import random


class SelectionSorting:
    """
    Класс для реализации алгоритма сортировки выбором.
    """

    def find_smallest(self, arr):
        """
        Нахождение наименьшего элемента в списке.

        :param arr: Список, в котором будет производиться поиск.

        :return: Индекс наименьшего значения.
        """
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest_index

    def sorting(self, arr):
        """
        Выполняет сортировку списка с использованием алгоритма сортировки выбором.

        :param arr: Список, который необходимо отсортировать.

        :return: Отсортированный список.
        """
        new_arr = []
        for _ in range(len(arr)):
            smallest = self.find_smallest(arr)
            new_arr.append(arr.pop(smallest))
        return new_arr


my_list = [random.randint(1, 133) for _ in range(1, 133)]

a = SelectionSorting()
print(a.sorting(my_list))
