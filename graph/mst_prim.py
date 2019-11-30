class AdjNode:
    def __init__(self, data, neighbour=None, cost=None):
        self.data = data
        self.neighbour = neighbour
        self.cost = cost


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None]*self.vertices

    def add_edge(self, src, dest, cost):
        adj = AdjNode(dest)
        adj.neighbour = self.graph[src]
        adj.cost = cost
        self.graph[src] = adj

        adj = AdjNode(src)
        adj.neighbour = self.graph[dest]
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
            temp = temp.neighbour

        return minimum_cost_edge

    def print_prim_mst(self, start):
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
    graph.print_prim_mst(2)
