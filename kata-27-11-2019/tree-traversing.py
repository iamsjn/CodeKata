class Node:
    def __init__(self, val, right, left):
        self.val = val
        self.left = left
        self.right = right


class TreeTraversal:
    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.val)
            self.in_order_traversal(root.right)

    def pre_order_traversal(self, root):
        if root:
            print(root.val)
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.val)
