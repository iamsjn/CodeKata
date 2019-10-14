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


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TreeTraversal:
    def in_order_traversal(self, root):
        stack = Stack()
        stack.push(root)

        root = root.left
        while root != None:
            stack.push(root)
            root = root.left

            if root == None and not stack.is_empty():
                temp = stack.pop()
                print(temp.val)

                if temp.right == None and not stack.is_empty():
                    tmp = stack.pop()
                    print(tmp.val)
                    root = tmp.right
                else:
                    root = temp.right


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)

    traversal = TreeTraversal()
    traversal.in_order_traversal(root)
