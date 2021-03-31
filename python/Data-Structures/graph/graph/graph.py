class Node: 
    def __init__(self, value=None,):
        self.value = value

class Edge:
    def __init__(self, connections, weight=1):
        self.connections = connections
        self.weight = weight

class Graph: 
    def __init__(self, adj_list={}):
        self.adj_list = adj_list

    def add_node(self, val):
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

    def size(self):
        list_size = len(self.adj_list)
        return int(list_size)


    def get_neighbors(self, node_to_check):
        return_neighbors = self.adj_list[node_to_check]
        return return_neighbors


    def get_nodes(self):
        list_holder = self.adj_list.keys()
        return list_holder
        # I refuse to delete this, strictly bc I was on the wrong track and I took way too long to write it & deleting it doesn't feel right!
        # vals = []
        # if len(self.adj_list) == 0:
        #     return 'Error'
        # for i in range(len(self.adj_list)+1):
        #     if i == 0:
        #         continue
        #     else:
        #         print(i)
        #         vals.append(self.adj_list.value)
        # return vals

# graph = Graph()
# graph.add_node('a')
# graph.add_node('b')
# print(graph.get_nodes())