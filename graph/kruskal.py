from typing import List, Optional


class Edge:
    def __init__(self) -> None:
        self.node1 = None
        self.node2 = None
        self.weight = None


class GraphNode:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: int = None
        self.cost: Node = None


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.rank: int = None
        self.parent: Node = None


class QueueNode:
    def __init__(self, value: int, next=None) -> None:
        self.value: int = value
        self.next: QueueNode = next


class Queue:
    def __init__(self) -> None:
        self.head = self.tail = None

    def is_empty(self):
        return self.head == None

    def enqueue(self, data: int) -> None:
        if self.tail == None and self.head == None:
            self.head = QueueNode(data)
            self.tail = self.head
        else:
            self.tail.next = QueueNode(data)
            self.tail = self.tail.next

    def dequeue(self) -> QueueNode:
        temp = self.head
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return temp


class Graph:
    def __init__(self, graph_size: int) -> None:
        self.graph_size = graph_size
        self.graph: List[GraphNode] = [None] * self.graph_size

    def add_edge(self, src: int, dest: int, weight: int) -> None:
        node = GraphNode(dest)
        node.next = self.graph[src]
        node.cost = weight
        self.graph[src] = node

        node = GraphNode(src)
        node.next = self.graph[dest]
        node.cost = weight
        self.graph[dest] = node

    def get_all_edges(self) -> None:
        all_vertices = self.get_all_vertices()
        all_edges: List[Edge] = []
        for vertex in all_vertices:
            adj_node = self.graph[vertex]

            while not adj_node == None:
                edge: Edge = Edge()
                adj_node = adj_node.next

    def get_all_vertices(self) -> List[int]:
        start_value: int = self.graph[1].value
        visited_vertices: List[int] = []
        neighbor_queue: Queue = Queue()

        visited_vertices.append(start_value)
        neighbor_queue.enqueue(start_value)

        while not neighbor_queue.is_empty():
            neighbor_value = neighbor_queue.dequeue().value
            neighbor_node = self.graph[neighbor_value]

            while not neighbor_node == None:
                if neighbor_node.value not in visited_vertices:
                    visited_vertices.append(neighbor_node.value)
                    neighbor_queue.enqueue(neighbor_node.value)
                neighbor_node = neighbor_node.next

        return visited_vertices


class DisjointSet:
    def __init__(self, set_size: int) -> None:
        self.set_size = set_size
        self.disjoint_map = [None] * self.set_size

    def make_set(self, value: int) -> None:
        node = Node(value)
        node.rank = 0
        node.parent = node

        self.disjoint_map[value] = node

    def find_set(self, node: Node) -> Node:
        parent = node.parent
        if parent.value == node.value:
            return node

        return self.find_set(node.parent)

    def is_in_same_set(self, parent1: Node, parent2: Node) -> bool:
        return parent1.value == parent2.value

    def make_union(self, value1: int, value2: int) -> None:
        node1 = self.disjoint_map[value1]
        node2 = self.disjoint_map[value2]

        parent1 = self.find_set(node1)
        parent2 = self.find_set(node2)

        if self.is_in_same_set(node1, node2):
            return

        if parent1.rank >= parent2.rank:
            parent1.rank = (
                parent1.rank + 1) if parent1.rank == parent2.rank else parent1.rank
            parent2.parent = parent1
        else:
            parent1.parent = parent2


if __name__ == '__main__':
    graph = Graph(8)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 4, 4)
    graph.add_edge(3, 5, 5)
    graph.add_edge(4, 6, 5)
