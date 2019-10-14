# adjacency_matrix
# class Graph:
#     def __init__(self, size):
#         self.adjMatrix = []
#         self.size = size

#         tempSize = size
#         while tempSize > 0:
#             self.adjMatrix.append([0 for i in range(size)])
#             tempSize = tempSize - 1

#     def add_edge(self, v1, v2):
#         self.adjMatrix[v1][v2] = 1
#         self.adjMatrix[v2][v1] = 1

#     def remove_edge(self, v1, v2):
#         self.adjMatrix[v1][v2] = 0
#         self.adjMatrix[v2][v1] = 0

#     def contains_edge(self, v1, v2):
#         return True if self.adjMatrix[v1][v2] > 0 else False

#     def string_representation(self):
#         return str(self.adjMatrix)


# if __name__ == '__main__':
#     graph = Graph(5)
#     graph.add_edge(0, 1)
#     graph.add_edge(0, 2)
#     graph.add_edge(1, 2)
#     graph.add_edge(2, 0)
#     graph.add_edge(2, 3)

#     print(graph.string_representation())

# adjacency_list
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
