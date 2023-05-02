import random
def countdown(i):
    """
    Выполнение обратного отсчета c использованием алгоритма рекурсии.

    :param i: Целое число, с которого необходимо начать отсчет.

    :return: Целое число или ничего, если выполняется условие "i == 0"
    """
    print(i)
    if i == 0:
        return
    else:
        countdown(i - 1)


# countdown(10)


def fact(x: int) -> int:
    """
    Вычесление факториала числа с использованием алгоритма рекурсии.

    :param x: Целое число, для вычесление факториала.

    :return: Факториал целого числа и "1", если число, переданное в формулу, равно единице.
    """
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


# print(fact(7))


def summ(lst: list) -> int:
    """
    Вычисление суммы элементов списка с использованием алгоритма рекурсии.

    :param lst: Список чисел.

    :return: Сумма элементов списка.
    """
    if len(lst) == 0:
        return 0
    else:
        return lst.pop() + summ(lst)


# print(summ([1, 2, 3, 4]))
# print(summ([1]))
# print(summ([]))
