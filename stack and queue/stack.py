class Node:
    def __init__(self, data, next):
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
        if(self.is_empty()):
            raise ValueError('Stack is empty')
        temp = self.top
        self.top = self.top.next
        return temp.data

    def peek(self):
        if(self.is_empty()):
            raise ValueError('Stack is empty')
        return self.top.data


if __name__ == '__main__':
    stack = Stack()
    for i in range(5):
        stack.push(i)
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
