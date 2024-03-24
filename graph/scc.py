class GraphOperation:
    def __init__(self, size, edges):
        self.size = size
        self.edges = edges
        self.adj_list = [[] for _ in range(self.size)]

        for src, dst in self.edges:
            self.adj_list[src].append(dst)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v)
        for i in self.adj_list[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def get_transpose(self):
        edges_t = []
        for i in range(self.size):
            for j in self.adj_list[i]:
                edges_t.append((j, i))
        graph_operation_t = GraphOperation(self.size, edges_t)

        return graph_operation_t

    def fill_order(self, v, stack, visited):
        visited[v] = True
        for i in self.adj_list[v]:
            if not visited[i]:
                self.fill_order(i, stack, visited)
        stack.append(v)

    def print_scc(self):
        stack = []
        visited = [False] * self.size

        for i in range(self.size):
            self.fill_order(i, stack, visited)

        graph_operation_t = self.get_transpose()

        visited = [False] * self.size

        while len(stack) > 0:
            i = stack.pop()
            if not visited[i]:
                graph_operation_t.dfs_util(i, visited)
            print(" ")


if __name__ == "__main__":
    edges = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]
    size = 5
    graph_operation = GraphOperation(size, edges)
    graph_operation.print_scc()

