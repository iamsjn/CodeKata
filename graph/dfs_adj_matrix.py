from typing import List, Optional


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, data) -> None:
        self.top = Node(data, self.top)

    def peek(self) -> Node:
        return self.top

    def pop(self) -> Node:
        temp = self.top
        self.top = self.top.next
        return temp


class GraphOperation:
    def __init__(self, graph_size: int):
        self.graph_size = graph_size
        self.adj_matrix = [[0 for i in range(self.graph_size)]
                           for i in range(self.graph_size)]

    def print_graph(self) -> None:
        for i in range(self.graph_size):
            print(self.adj_matrix[i], end="\n")

    def add_edge(self, src: int, dst: int) -> None:
        self.adj_matrix[src][dst] = 1
        self.adj_matrix[dst][src] = 1

    def _connected_vertices_for(self, vertex: int) -> List[int]:
        connected_vertices = []
        for i in range(self.graph_size):
            if self.adj_matrix[vertex][i] == 1:
                connected_vertices.append(i)

        return connected_vertices

    def traversal_using_dfs(self, start_vertex: int) -> List[int]:
        stack = Stack()
        visited_vertices = []
        stack.push(start_vertex)

        while not stack.is_empty():
            vertex = stack.peek()

            if vertex.data not in visited_vertices:
                visited_vertices.append(vertex.data)
                connected_vertices = self._connected_vertices_for(vertex.data)

                while len(connected_vertices) > 0:
                    stack.push(connected_vertices.pop())
            else:
                stack.pop()

        return visited_vertices


if __name__ == "__main__":
    graph = GraphOperation(5)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 4)

    print(graph.traversal_using_dfs(0))
