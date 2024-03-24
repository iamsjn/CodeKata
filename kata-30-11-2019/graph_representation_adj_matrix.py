class Graph:
    def __init__(self, size):
        self.adjMatrix = []
        self.size = size
        tempSize = self.size

        #[[0 for x in range(cols_count)] for x in range(rows_count)]
        while tempSize > 0:
            self.adjMatrix.append([0 for i in range(self.size)])
            tempSize = tempSize - 1

    def add_edge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def contains_edge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def string_representation(self):
        return str(self.adjMatrix)


if __name__ == '__main__':
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)

    print(graph.string_representation())
