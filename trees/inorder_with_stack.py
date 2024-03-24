from typing import Optional


class TreeNode:
    def __init__(self, node: int, left_node: "TreeNode" = None,
                 right_node: "TreeNode" = None):
        self.node = node
        self.left_node = left_node
        self.right_node = right_node


def inorder_traversal(current_node: TreeNode):
    stack = []
    visited_nodes = []
    stack.append(current_node)

    while len(stack) > 0:
        if current_node.left_node is not None and current_node not in visited_nodes:
            current_node = current_node.left_node
            stack.append(current_node)
        else:
            current_node = stack.pop()
            visited_nodes.append(current_node)
            if current_node.right_node is not None:
                current_node = current_node.right_node
                stack.append(current_node)

    for node in visited_nodes:
        print(node.node, end=" ")


def preorder_traversal(current_node: TreeNode):
    stack = []
    visited_nodes = []
    stack.append(current_node)

    while len(stack) > 0:
        current_node = stack.pop()
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)

        if current_node.right_node is not None:
            stack.append(current_node.right_node)

        if current_node.left_node is not None:
            stack.append(current_node.left_node)

    for node in visited_nodes:
        print(node.node, end=" ")


def postorder_traversal(current_node: TreeNode):
    stack = []
    visited_nodes = []
    stack.append(current_node)

    while len(stack) > 0:
        if current_node.right_node is not None:
            stack.append(current_node.right_node)

        if current_node.left_node is not None:
            stack.append(current_node.left_node)

        current_node = stack.pop()
        visited_nodes.append(current_node)

    for node in visited_nodes:
        print(node.node, end=" ")


if __name__ == "__main__":
    tree_node_4 = TreeNode(4)
    tree_node_2 = TreeNode(2, tree_node_4)
    tree_node_7 = TreeNode(7)
    tree_node_8 = TreeNode(8)
    tree_node_5 = TreeNode(5, tree_node_7, tree_node_8)
    tree_node_6 = TreeNode(6)
    tree_node_3 = TreeNode(3, tree_node_5, tree_node_6)
    tree_node_1 = TreeNode(1, tree_node_2, tree_node_3)

    # inorder_traversal(tree_node_1)
    # preorder_traversal(tree_node_1)
    # postorder_traversal(tree_node_1)
