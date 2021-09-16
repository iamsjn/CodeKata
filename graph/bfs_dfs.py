class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class   Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def is_empty(self):
        return self.head == None

    def enqueue(self, data):
        if self.last == None and self.head == None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        temp = self.head
        self.head = self.head.next
        if self.head == None:
            self.last = None
        return temp


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        temp = self.top
        self.top = self.top.next
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

    def print_graph(self):
        for v in range(self.vertics):
            print("Adjacency list of vertex {}\n head".format(v), end="")
            temp = self.graph[v]
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print(" \n")

    def breadth_first_traversal(self, vertex):
        visited_vertex_list = []
        neighbours_queue = Queue()

        visited_vertex_list.append(vertex)
        neighbours_queue.enqueue(vertex)

        while not neighbours_queue.is_empty():
            v = neighbours_queue.dequeue()
            temp = self.graph[v.data]
            while temp:
                if temp.data not in visited_vertex_list:
                    visited_vertex_list.append(temp.data)
                    neighbours_queue.enqueue(temp.data)
                temp = temp.next

        print(visited_vertex_list)

    def depth_first_traversal(self, vertex):
        stack = Stack()
        visited_vertex_list = []

        stack.push(vertex)
        visited_vertex_list.append(vertex)

        while not stack.is_empty():
            v = stack.pop()
            temp = self.graph[v.data]
            while temp:
                if temp.data not in visited_vertex_list:
                    visited_vertex_list.append(temp.data)
                    stack.push(temp.data)
                temp = temp.next

        print(visited_vertex_list)


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
    graph.breadth_first_traversal(4)
    graph.depth_first_traversal(4)
