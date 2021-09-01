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

    def enqueue(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
            self.last = self.head
        else:
            node = Node(data)
            self.last.next = node
            self.last = self.last.next

    def dequeue(self):
        tmp = self.head
        self.head = self.head.next
        return tmp


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        tmp = self.top
        self.top = self.top.next
        return tmp


# class Graph_Operation:

    # def breadth_first_search(self, root):
    #     neighbors_queue = Queue()
    #     visited_vertex = []

    #     visited_vertex.append(root)
    #     neighbors_queue.enqueue(root)

    #     while not neighbors_queue.is_empty():
    #         tmp = neighbors_queue.dequeue()
    #         tmp1 = tmp.next
