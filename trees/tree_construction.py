from typing import Optional, List, Tuple


class TreeNode:
    def __init__(self, node: int, left_node: Optional["TreeNode"] = None,
                 right_node: Optional["TreeNode"] = None):
        self.node = node
        self.left_node = left_node
        self.right_node = right_node


def preorder_traversal(current_node: TreeNode):
    stack = []
    stack.append(current_node)

    while len(stack) > 0:
        current_node = stack.pop()
        print(current_node.node, end=" ")

        if current_node.right_node is not None:
            stack.append(current_node.right_node)

        if current_node.left_node is not None:
            stack.append(current_node.left_node)


def construct_tree(inorder: List[int], preorder: List[int], root_index: int) -> Tuple[Optional[TreeNode], int]:
    print(inorder, preorder)

    root_node = preorder[root_index]
    root_node_index = inorder.index(root_node)
    root_index = root_index + 1
    tree_node = TreeNode(root_node)

    if len(inorder) == 1:
        return tree_node, root_index

    if len(inorder[:root_node_index]) > 0:
        tree_node.left_node, root_index = construct_tree(inorder[:root_node_index], preorder, root_index)

    if len(inorder[root_node_index:]) > 1:
        tree_node.right_node, root_index = construct_tree(inorder[(root_node_index+1):], preorder, root_index)

    return tree_node, root_index


if __name__ == "__main__":
    inorder_list = [4, 2, 1, 7, 5, 8, 3, 6]
    preorder_list = [1, 2, 4, 3, 5, 7, 8, 6]
    tree_node, root_index = construct_tree(inorder_list, preorder_list, 0)
    preorder_traversal(tree_node)
