from typing import Optional, Union, Tuple


class TreeNode:
    def __init__(self, node: int, left_node: "TreeNode" = None,
                 right_node: "TreeNode" = None):
        self.node_value = node
        self.left_node = left_node
        self.right_node = right_node


def has_no_child(tree_node: TreeNode) -> bool:
    return tree_node.left_node is None and tree_node.right_node is None


def has_child(tree_node: TreeNode) -> bool:
    return tree_node.left_node is not None or tree_node.right_node is not None


def has_both_child(tree_node: TreeNode) -> bool:
    return tree_node.left_node is not None and tree_node.right_node is not None


def get_node_with_minimum_value(tree_node: TreeNode) -> TreeNode:
    while tree_node:
        tree_node = tree_node.left_node

    return tree_node


def get_inorder_successor(root_node: TreeNode, tree_node: TreeNode) -> TreeNode:
    if tree_node.right_node is not None:
        return get_node_with_minimum_value(tree_node.right_node)

    parent_node, current_node = get_parent_node(root_node, tree_node.node_value)
    while True:
        if current_node.node_value == parent_node.node_value:
            return parent_node

        parent_node, current_node = get_parent_node(root_node, parent_node.node_value)


def get_parent_node(root_node: TreeNode, node_value: int) -> Tuple[TreeNode, TreeNode]:
    node_to_be_deleted = root_node
    parent_node = None

    while node_to_be_deleted and node_to_be_deleted.node_value != node_value:
        parent_node = node_to_be_deleted

        if node_to_be_deleted.node_value > node_value:
            node_to_be_deleted = node_to_be_deleted.left_node
        else:
            node_to_be_deleted = node_to_be_deleted.right_node

    return parent_node, node_to_be_deleted


class TreeOperation:

    def insert_node(self, root_node: Optional[TreeNode], node_value: int):
        if root_node is None:
            return TreeNode(node_value)

        if root_node.node_value > node_value:
            root_node.left_node = self.insert_node(root_node.left_node, node_value)
        else:
            root_node.right_node = self.insert_node(root_node.right_node, node_value)

        return root_node

    def delete_node(self, root_node: Union[TreeNode, None], node_value: int) -> Optional[TreeNode]:
        parent_node, node_to_be_deleted = get_parent_node(root_node, node_value)

        if has_no_child(node_to_be_deleted):
            if root_node.node_value != node_value:
                if parent_node.left_node.node_value == node_value:
                    parent_node.left_node = None
                else:
                    parent_node.right_node = None
            else:
                root_node = None

            return root_node
        elif has_both_child(node_to_be_deleted):
            successor_node = get_inorder_successor(root_node, node_to_be_deleted)
            value = successor_node.node_value
            self.delete_node(root_node, successor_node.node_value)
            node_to_be_deleted.node_value = value

            return root_node


if __name__ == "__main__":
    tree_operation = TreeOperation()
    node_keys = [15, 10, 20, 8, 12, 16]

    root = None
    for k in node_keys:
        root = tree_operation.insert_node(root, k)
