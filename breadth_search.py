from collections import deque
graph = {'you': ['alice', 'bob', 'claire'], 'bob': ['anuj', 'peggy'], 'alice': ['peggy'], 'claire': ['tom', 'jonny'],
         'anuj': [], 'peggy': [], 'tom': [], 'jonny': [], }


def person_is_seller(name):
    """
    Определяет, является ли последняя буква имени, буквой "m".

    :param name: Имя.
    :type name: str.
    :return: True или False.
    """
    return name[-1] == 'm'


def search_seller(name):
    """
    Производит поиск продавца манго, среди друзей, указанного имени и дальнейших друзей.

    :param name: Имя.
    :type name: str.
    :return: Имя продавца манго или "Mango seller not found!", если продавец не найден.
    """
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        print(person)
        if person not in searched:
            if person_is_seller(person):
                return person.capitalize() + ' is a mango seller!'
            else:
                search_queue += graph[person]
                searched.append(person)
    return 'Mango seller not found!'


print(search_seller('you'))
