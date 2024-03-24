from typing import List, Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional[Node] = None


class Stack:
    def __init__(self) -> None:
        self.top: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.top == None

    def push(self, value: int) -> None:
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self) -> int:
        if self.is_empty():
            raise ValueError("Stack is empty")

        temp = self.top
        self.top = self.top.next

        return temp.value

    def peek(self) -> int:
        if self.is_empty():
            raise ValueError("Stack is empty")

        return self.top.value


class DirectedGraph:
    def __init__(self, vertices: int) -> None:
        self.vertices: int = vertices
        self.graph: List[Optional[Node]] = [None] * self.vertices

    def add_edge(self, src: int, dest: int) -> None:
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def do_dfs(self, visited_vertices: List[int], start_node_value: int) -> List[int]:
        stack = Stack()
        stack.push(start_node_value)

        while not stack.is_empty():
            node_value = stack.peek()
            if not node_value in visited_vertices:
                visited_vertices.append(node_value)
                adj_node = self.graph[node_value]
                while not adj_node is None:
                    stack.push(adj_node.value)
                    adj_node = adj_node.next
            else:
                stack.pop()

        return visited_vertices


if __name__ == "__main__":
    graph = DirectedGraph(8)
    graph.add_edge(1, 2)
    graph.add_edge(2, 7)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)

    print(graph.do_dfs([], 3))
