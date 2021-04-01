from graph.queue import Queue

class Node: 
    def __init__(self, value=None,):
        self.value = value


class Edge:
    def __init__(self, end, weight=1):
        self.end = end
        self.weight = weight


class Graph: 
    def __init__(self, adj_list={}, node_count=0):
        self.adj_list = adj_list
        self.node_count = node_count

    def add_node(self, val):
        self.node_count += 1
        node = Node(val)
        self.adj_list[node] = []
        return node

    def add_edge(self, start, end, weight=1):
        if start not in self.adj_list:
            return "Starting point not in list"
        if end not in self.adj_list:
            return "End point not in list"
        edge = Edge(end, weight)
        adjacencies = self.adj_list[start]
        adjacencies.append(edge)

    def get_nodes(self):
        if len(self.adj_list) > 0:
            list_holder = []
            for i in self.adj_list:
                neighbor = self.get_neighbors(i)
                to_append = [i.value, neighbor]
                list_holder.append(to_append)
        return list_holder

    def get_neighbors(self, node_to_check):
        edges = []
        adjList = self.adj_list[node_to_check]
        if len(adjList) > 0:
            for i in adjList:
                edge = i.end.value
                n_weight = i.weight
                add_to_edges = edge, n_weight
                edges.append(add_to_edges)
        return edges

    def size(self):
        list_size = self.node_count
        return list_size

# Extend your graph object with a breadth-first traversal method that accepts a starting node. Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection.

    # def breadth_first_traversal(self, node):
    #     visited_nodes = [node]
    #     new_queue = Queue()
    #     new_queue.enqueue(node)
    #     while not new_queue.isempty():
    #         placeholder = new_queue.dequeue()
    #         neighbors = [edge.placeholder for edge in self.get_neighbors(node)]
    #         for i in neighbors:
    #             if i not in visited_nodes:
    #                 visited_nodes.append(i)
    #                 new_queue.enqueue(i)
    #     return visited_nodes


    def breadth_first_traversal(self, node):
        new_list = [node]
        store_results = []
        node_tracker = {}
        current = None
        neighbors = None
        
        node_tracker[node] = True
        while new_list is not None: 
            current = new_list.pop(0)
            neighbors = self.get_neighbors(current)
            store_results.append(current)

            for i in range(len(neighbors)):
                if node_tracker[neighbors[i].value] is not None:
                    node_tracker[neighbors[i].value] = True
                    new_list.append(neighbors[i].val)

        return store_results