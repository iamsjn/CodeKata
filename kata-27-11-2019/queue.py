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
        if self.head == None and self.last == None:
            self.head = Node(data)
            self.last = self.head
        else:
            temp_node = Node(data)
            self.last.next = temp_node
            self.last = temp_node

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        temp_node = self.head
        self.head = self.head.next
        return temp_node.data
