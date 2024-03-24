from typing import Optional, List, Tuple


class AdjNode:
    def __init__(self, vertex: int, edge_cost: int, neighbor_list: Optional["AdjNode"] = None):
        self.vertex = vertex
        self.edge_cost = edge_cost
        self.neighbor_list = neighbor_list


class GraphOperation:
    def __init__(self, vertices: int):
        self.total_vertices: int = vertices
        self.graph_vertices: List[Optional[AdjNode]] = [None] * self.total_vertices

    def add_edge(self, src_vertex: int, dst_vertex: int, edge_cost: int):
        adj_node = AdjNode(dst_vertex, edge_cost, self.graph_vertices[src_vertex])
        self.graph_vertices[src_vertex] = adj_node

        adj_node = AdjNode(src_vertex, edge_cost, self.graph_vertices[dst_vertex])
        self.graph_vertices[dst_vertex] = adj_node

    def edge_with_minimum_cost(self) -> Optional[AdjNode]:
        minimum_edge_cost: int = 10000
        minimum_cost_edge: Optional[AdjNode] = None
        for i in range(1, len(self.graph_vertices)):
            adj_list = self.graph_vertices[i]
            while adj_list:
                if adj_list.edge_cost < minimum_edge_cost:
                    minimum_edge_cost = adj_list.edge_cost
                    minimum_cost_edge = adj_list
                adj_list = adj_list.neighbor_list

        return minimum_cost_edge

    # def print_minimum_spanning_tree(self):
    #     minimum_cost_edge = self.edge_with_minimum_cost()
    #     temp = minimum_cost_edge
    #     visited_vertices: List[int] = []
    #     while temp:




# class Graph:
#     def __init__(self, vertices):
#         self.vertices = vertices
#         self.graph = [None]*self.vertices
#
#     def add_edge(self, src, dest, cost):
#         adj = AdjNode(dest)
#         adj.neighbor = self.graph[src]
#         adj.cost = cost
#         self.graph[src] = adj
#
#         adj = AdjNode(src)
#         adj.neighbor = self.graph[dest]
#         adj.cost = cost
#         self.graph[dest] = adj
#
#     def get_minimum_cost_edge(self, start):
#         minimum_cost = 1000
#         minimum_cost_edge = None
#         temp = self.graph[start]
#
#         while temp:
#             if temp.cost < minimum_cost:
#                 minimum_cost = temp.cost
#                 minimum_cost_edge = temp
#             temp = temp.neighbor
#
#         return minimum_cost_edge
#
#     def print_prims_mst(self, start):
#         mst = []
#         mst.append(start)
#         temp = self.graph[start]
#
#         while temp:
#
#             if temp.data not in mst:
#                 mst.append(temp.data)
#             else:
#                 temp = None


if __name__ == "__main__":
    V = 8
    graph = GraphOperation(V)
    graph.add_edge(1, 2, 28)
    graph.add_edge(1, 6, 10)
    graph.add_edge(6, 5, 25)
    graph.add_edge(5, 4, 22)
    graph.add_edge(5, 7, 24)
    graph.add_edge(4, 3, 12)
    graph.add_edge(4, 7, 18)
    graph.add_edge(7, 2, 14)
    graph.add_edge(2, 3, 16)
    print(graph.edge_with_minimum_cost().vertex)
    # graph.print_prims_mst(2)
