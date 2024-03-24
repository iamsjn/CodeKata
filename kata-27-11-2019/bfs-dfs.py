from graph.bfs_dfs import Queue


class Node:
    def __int__(self, data, next):
        self.data = data
        self.next = next


class GraphOperation:

    def breadth_first_search(self, node: Node):
        queue = Queue()
        visited_list = []

        queue.enqueue(node)
        visited_list.append(node.data)

        while not queue.is_empty():
            temp_node = queue.dequeue()
            temp = temp_node
