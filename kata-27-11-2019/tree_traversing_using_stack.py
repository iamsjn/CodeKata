class StackNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TreeNode:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, val):
        temp_node = StackNode(val, self.top)
        self.top = temp_node

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        temp_node = self.top
        self.top = self.top.next
        return temp_node


class Tree:
    def in_order_traversal(self, root):
        stack = Stack()
        stack.push(root)
        temp_root = root.left

        while temp_root != None:
            stack.push(temp_root)

            if temp_root.left == None:
                temp = stack.pop()
                print(temp.data.root, end=" ")
                temp_root = temp_root.right

                if temp_root == None and not stack.is_empty():
                    temp = stack.pop()
                    print(temp.data.root, end=" ")
                    temp_root = temp.data.right
            else:
                temp_root = temp_root.left


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)

    tree = Tree()
    tree.in_order_traversal(root)
