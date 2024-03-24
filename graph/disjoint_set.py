class Node:
    def __init__(self, value) -> None:
        self.value: int = value
        self.rank: int = None
        self.parent: Node = None


class DisjointSet:
    def __init__(self, size) -> None:
        self.size = size
        self.disjoint_set = [None] * self.size

    def make_set(self, value):
        # Creates set with only one element
        node = Node(value)
        node.rank = 0
        node.parent = node

        self.disjoint_set[value] = node

    def union(self, value1, value2):
        node1 = self.disjoint_set[value1]
        node2 = self.disjoint_set[value2]

        node1_parent = self.find_set_representative(node1)
        node2_parent = self.find_set_representative(node2)

        if node1_parent == node2_parent:
            return

        if node1_parent.rank >= node2_parent:
            node1_parent.rank = (
                node1_parent.rank + 1) if node1_parent.rank == node2_parent else node1_parent.rank
            node2_parent.parent = node1_parent
        else:
            node1_parent.parent = node2_parent

    def find_set_representative(self, node: Node) -> Node:
        # Find disjoint_set the set representative
        parent = node.parent
        if node.value == parent.value:
            return node

        # Doing path optimization
        # Making set representative as the parent
        node.parent = self.find_set(node.parent)
        return node.parent


if __name__ == '__main__':
    disjoint_set = DisjointSet(7)

    disjoint_set.make_set(1)
    disjoint_set.make_set(2)
    disjoint_set.make_set(3)
    disjoint_set.make_set(4)
    disjoint_set.make_set(5)
    disjoint_set.make_set(6)
    disjoint_set.make_set(7)

    disjoint_set.union(1, 2)
    disjoint_set.union(2, 3)
    disjoint_set.union(4, 5)
    disjoint_set.union(6, 7)
    disjoint_set.union(5, 6)
    disjoint_set.union(3, 7)
