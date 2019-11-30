class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        temp_node = Node(dest, self.graph[src])
        self.graph[src] = temp_node

        temp_node = Node(src, self.graph[dest])
        self.graph[dest] = temp_node