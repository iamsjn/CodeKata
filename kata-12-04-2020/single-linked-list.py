class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add_first(self, item):
        self.head = Node(item, self.head)

    def add_last(self, item):
        tmp = self.head

        while tmp.next != None:
            tmp = tmp.next
        node = Node(item, None)
        tmp.next = node

    def get_first(self):
        if self.is_empty():
            raise ValueError('List is empty')

        return self.head.data

    def traverse(self):
        if self.is_empty():
            raise ValueError('List is empty')

        tmp = self.head
        while tmp != None:
            print(tmp.data)
            tmp = tmp.next

    def reverse(self):
        if self.is_empty():
            raise ValueError('List is empty')
        linked_list = SingleLinkedList()
        tmp = self.head
        while tmp != None:
            linked_list.add_first(tmp.data)
            tmp = tmp.next

        return linked_list


if __name__ == '__main__':
    linkedList = SingleLinkedList()
    linkedList.add_first('The Alchemist part 1')
    linkedList.add_first('The Alchemist part 2')
    linkedList.add_first('The four agreements part 1')
    linkedList.add_first('The four agreements part 2')
    linkedList.add_last('The four agreements part 3')

    # print(linkedList.get_first())
    linkedList.traverse()
    # reversedLinkedList = linkedList.reverse()
    # reversedLinkedList.traverse()
