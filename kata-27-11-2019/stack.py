class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, data):
        temp_node = Node(data)
        temp_node.next = self.top
        self.top = temp_node

    def pop(self):
        if self.is_empty():
            raise ValueError('Stck is empty')
        temp_node = self.top
        self.top = temp_node.next
        return temp_node.data

    def peek(self):
        if self.is_empty():
            raise ValueError('Stck is empty')
        return self.top.data
