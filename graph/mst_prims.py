class AdjNode:
    def __init__(self, data, neighbor=None, cost=None):
        self.data = data
        self.neighbor = neighbor
        self.cost = cost


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None]*self.vertices

    def add_edge(self, src, dest, cost):
        adj = AdjNode(dest)
        adj.neighbor = self.graph[src]
        adj.cost = cost
        self.graph[src] = adj

        adj = AdjNode(src)
        adj.neighbor = self.graph[dest]
        adj.cost = cost
        self.graph[dest] = adj

    def get_minimum_cost_edge(self, start):
        minimum_cost = 1000
        minimum_cost_edge = None
        temp = self.graph[start]

        while temp:
            if temp.cost < minimum_cost:
                minimum_cost = temp.cost
                minimum_cost_edge = temp
            temp = temp.neighbor

        return minimum_cost_edge

    def print_prims_mst(self, start):
        mst = []
        mst.append(start)
        temp = self.graph[start]

        while temp:

            if temp.data not in mst:
                mst.append(temp.data)
            else:
                temp = None


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1, 9)
    graph.add_edge(1, 3, 19)
    graph.add_edge(3, 4, 31)
    graph.add_edge(3, 2, 51)
    # print(graph.get_minimum_cost_edge(1))
    graph.print_prims_mst(2)
