class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def is_empty(self):
        return self.head == None

    def enqueue(self, val):
        if self.head == None and self.last == None:
            self.head = Node(val)
            self.last = self.head
        else:
            temp_node = Node(val)
            self.last.next = temp_node
            self.last = temp_node

    def dequeue(self):
        temp = self.head
        self.head = self.head.next
        if self.head == None:
            self.last = None
        return temp


class Graph:
    def __init__(self, vertics):
        self.vertics = vertics
        self.graph = [None] * self.vertics

    def add_edge(self, v1, v2):
        node = Node(v2)
        node.next = self.graph[v1]
        self.graph[v1] = node

        node = Node(v1)
        node.next = self.graph[v2]
        self.graph[v2] = node

    def bfs(self, vertex):
        visited_vertices = []
        neighbours_queue = Queue()

        visited_vertices.append(vertex)
        neighbours_queue.enqueue(vertex)

        while not neighbours_queue.is_empty():
            vertex = neighbours_queue.dequeue()
            temp = self.graph[vertex.data]

            while temp:
                if temp.data not in visited_vertices:
                    visited_vertices.append(temp.data)
                    neighbours_queue.enqueue(temp.data)
                temp = temp.next


if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    # graph.print_graph()
    graph.bfs(4)
