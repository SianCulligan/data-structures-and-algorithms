class Node: 
    def __init__(self, value):
        self.value = value

class Queue_Node:
    def __init__(self, nodeVal=None, nextVal=None):
        self.nodeVal = nodeVal
        self.nextVal = nextVal

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
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
        if self.size() > 0:
            list_holder = []
            for i in self.adj_list:
                neighbor = self.get_neighbors(i)
                to_append = [i.value, neighbor]
                list_holder.append(to_append)
        return list_holder

    def get_neighbors(self, node_to_check):
        if node_to_check not in self.adj_list:
            return "Starting point not in list"
        edges = []

        for i in self.adj_list[node_to_check]:
            # MUST HAVE LABELS - will not always return val followed by weight. Use as dictionary (Use labels as keys)
            edges.append({'val': i.vertex.value, 'weight': i.weight})
        return edges

    def size(self):
        list_size = self.node_count
        return list_size

    def depth_first(self, root):
        if root not in self.adj_list:
            return "Starting point not in list"
        find_keys = self.adj_list.keys()
        key_rack = []
        root_list = []

        for i in find_keys:
            key_rack.append(i)
        
        root_list.append(key_rack[0].value)

        while len(key_rack):
            s = key_rack.pop(0)
            print("VALUES", s.value)
            
            if s.value not in root_list:
                root_list.append(s.value)

        print("ROOT LIST", root_list)
        return root_list

############################################################################################
class Queue: 
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear 

    def enqueue(self, add_to_back):
        node_to_queue = Queue_Node(add_to_back)
        if self.isempty() is True:
            self.front = node_to_queue
            self.rear = node_to_queue
            return node_to_queue
        self.rear.nextVal = node_to_queue
        self.rear = node_to_queue
        return node_to_queue

    def dequeue(self):
        node_to_remove = self.front
        if self.isempty() is True: 
            return "Exception"
        self.front = self.front.nextVal
        node_to_remove.nextVal = None
        self.rear = None
        return node_to_remove.nodeVal


    def peek(self):
        if self.isempty() is True: 
            return "Exception"
        return self.front.nodeVal

    def isempty(self):
        if self.front is None and self.rear is None: 
            print("True")
            return True
        else: 
            print("False")
            return False





