class AdjNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.Graph = [None] * self.vertices

    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.Graph[src]
        self.Graph[src] = node

        node = AdjNode(src)
        node.next = self.Graph[dest]
        self.Graph[dest] = node
