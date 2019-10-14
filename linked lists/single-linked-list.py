class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next


class SingleLinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add_first(self, item):
        self.head = Node(item, self.head)

    def get_first(self):
        if(self.head == None):
            raise ValueError('List is empty')
        return self.head.data

    def traverse(self):
        if(self.head == None):
            raise ValueError('List is empty')
        tmp = self.head
        while(tmp != None):
            print(tmp.data)
            tmp = tmp.next

    def reverse(self):
        linkedList = SingleLinkedList()
        tmp = self.head

        while(tmp != None):
            linkedList.add_first(tmp.data)
            tmp = tmp.next

        return linkedList


if __name__ == '__main__':
    linkedList = SingleLinkedList()
    linkedList.add_first('The Alchemist part 1')
    linkedList.add_first('The Alchemist part 2')
    linkedList.add_first('The four agreements part 1')
    linkedList.add_first('The four agreements part 2')

    # print(linkedList.get_first())
    linkedList.traverse()
    reversedLinkedList = linkedList.reverse()
    reversedLinkedList.traverse()
