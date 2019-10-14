class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
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


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    bst = BST()

    print('Inorder traversal:')
    print(bst.in_order_traversal(root))

    print('Preorder traversal:')
    print(bst.pre_order_traversal(root))

    print('Postorder traversal:')
    print(bst.post_order_traversal(root))
