class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        temp = self.top
        self.top = self.top.next
        return temp


class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def is_empty(self):
        return self.head == None

    def enqueue(self, data):
        if self.head == None and self.last == None:
            self.head = Node(data)
            self.last = self.head
        else:
            node = Node(data)
            self.last.next = node
            self.last = self.last.next

    def dequeue(self):
        if self.head == None:
            raise ValueError('Queue is empty')
        temp = self.head
        self.head = self.head.next
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
        visited_vertex = []
        neighbour_queue = Queue()

        visited_vertex.append(vertex)
        neighbour_queue.enqueue(vertex)

        while not neighbour_queue.is_empty():
            v = neighbour_queue.dequeue()
            adjacency_linked_list = self.graph[v.data]

            while adjacency_linked_list:
                if adjacency_linked_list.data not in visited_vertex:
                    visited_vertex.append(adjacency_linked_list.data)
                    neighbour_queue.enqueue(adjacency_linked_list.data)
                    adjacency_linked_list = adjacency_linked_list.next

        print(visited_vertex)
