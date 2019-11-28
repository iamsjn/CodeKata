# this is a single linked list implementation
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add_first(self, data):
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node

    def get_first(self):
        if self.is_empty():
            raise ValueError('List is empty')
        return self.head.data

    def traverse(self):
        if self.is_empty():
            raise ValueError('List is empty')
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse(self):
        linked_list = SingleLinkedList()
        temp = self.head

        while temp:
            linked_list.add_first(temp.data)
            temp = temp.next

        return linked_list
