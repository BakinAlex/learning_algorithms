class Dijkstra:
    """
    Класс Dijkstra реализует алгоритм Дейкстры для нахождения кратчайшего пути в графе.
    """

    processed = []

    def __init__(self, graph, costs_node, parents):
        self.graph = graph
        self.costs_node = costs_node
        self.parents = parents

    def _find_lowest_costs_node(self):
        """
        Поиск узла с наименьшей стоимостью.

        :return: узел с наименьшей стоимостью.
        """
        lowest_cost = float('inf')
        lowest_coat_node = None
        for key, value in self.costs_node.items():
            if value < lowest_cost and key not in self.processed:
                lowest_cost = value
                lowest_coat_node = key
        return lowest_coat_node

    def algorithm(self):
        """
        Реализация алгоритма Дейкстры.

        :return: Словари родителей и веса узлов.
        """
        node = self._find_lowest_costs_node()
        while node is not None:
            cost = self.costs_node[node]
            neighbors = self.graph[node]
            for neighbor in neighbors:
                new_cost = cost + neighbors[neighbor]
                if self.costs_node[neighbor] > new_cost:
                    self.costs_node[neighbor] = new_cost
                    self.parents[neighbor] = node
            self.processed.append(node)
            node = self._find_lowest_costs_node()
        return self.parents, self.costs_node


graph_0 = {'start': {'a': 6, 'b': 2}, 'a': {'end': 1}, 'b': {'a': 3, 'end': 5}, 'end': {}}
costs_node_0 = {'a': 6, 'b': 2, 'end': float('inf')}
parents_0 = {'a': 'start', 'b': 'start', 'end': {}}

graph_a = {'start': {'a': 5, 'b': 2}, 'a': {'c': 4, 'd': 2}, 'b': {'a': 8, 'd': 7}, 'c': {'d': 6, 'end': 3},
           'd': {'end': 1}, 'end': {}}
costs_node_a = {'a': 5, 'b': 2, 'c': float('inf'), 'd': float('inf'), 'end': float('inf')}
parents_a = {'a': 'start', 'b': 'start', 'c': {}, 'd': {}, 'end': {}}

graph_b = {'start': {'a': 10}, 'a': {'b': 20}, 'b': {'c': 1, 'end': 30}, 'c': {'a': 1}, 'end': {}}
costs_node_b = {'a': 10, 'b': float('inf'), 'c': float('inf'), 'end': float('inf')}
parents_b = {'a': 'start', 'b': {}, 'c': {}, 'end': {}}

graph_c = {'start': {'a': 2, 'b': 2}, 'a': {'c': 2, 'end': 2}, 'b': {'a': 2}, 'c': {'b': -1, 'end': 2}, 'end': {}}
costs_node_c = {'a': 2, 'b': 2, 'c': float('inf'), 'end': float('inf')}
parents_c = {'a': 'start', 'b': 'start', 'c': {}, 'end': {}}

diks = Dijkstra(graph_c, costs_node_c, parents_c)
print(diks.algorithm())
