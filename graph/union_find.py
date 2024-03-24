from typing import List, Tuple


class DisjointSet:
    def __init__(self, size: int):
        self.parent_map = {}
        self.rank_map = {}

        for i in range(size):
            self.parent_map[i] = i
            self.rank_map[i] = 0

    def union(self, val1: int, val2: int) -> None:
        par1 = self.find(val1)
        par2 = self.find(val2)

        if self.rank_map[par1] >= self.rank_map[par2]:
            if self.rank_map[par1] == self.rank_map[par2]:
                self.rank_map[par1] = self.rank_map[par1] + 1
            self.parent_map[par2] = par1
        else:
            self.parent_map[par1] = par2

    def find(self, val: int) -> int:
        if self.parent_map[val] != val:
            self.parent_map[val] = self.find(self.parent_map[val])

        return self.parent_map[val]


class Graph:
    def __init__(self, graph_edges: List[Tuple[int, int]], graph_size: int):
        self.graph_size = graph_size
        self.adj_list = [[] for _ in range(self.graph_size)]

        for src, dst in graph_edges:
            self.adj_list[src].append(dst)

    def has_cycle(self) -> bool:
        disjoint_set = DisjointSet(self.graph_size)

        for i in range(self.graph_size):
            for j in self.adj_list[i]:
                par1 = disjoint_set.find(i)
                par2 = disjoint_set.find(j)

                if par1 == par2:
                    return True
                else:
                    disjoint_set.union(i, j)


if __name__ == "__main__":
    edges = [
        (0, 1), (0, 6), (0, 7), (1, 2), (1, 5), (2, 3),
        (2, 4), (7, 8), (7, 11), (8, 9), (8, 10), (10, 11)]

    total = 12

    graph = Graph(edges, total)
    print(graph.has_cycle())
