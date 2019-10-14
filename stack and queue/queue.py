class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def is_empty(self):
        return self.head == None

    def enqueue(self, data):
        if self.last == None:
            self.head = Node(data, None)
            self.last = self.head
        else:
            self.last.next = Node(data, None)
            self.last = self.last.next

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        temp = self.head
        self.head = self.head.next
        return temp.data


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('Alchemist part 1')
    queue.enqueue('Alchemist part 2')
    queue.enqueue('Alchemist part 3')

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
