class Queue_Node:
    def __init__(self, nodeVal=None, nextVal=None):
        self.nodeVal = nodeVal
        self.nextVal = nextVal

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
        edge_holder = []
        adjList = self.adj_list[node_to_check]
        if len(adjList) > 0:
            for i in adjList:
                end_point = i.end
                weight = i.weight
                concatenate = end_point, weight
                edge_holder.append(concatenate)
        return edge_holder

    def size(self):
        list_size = self.node_count
        return list_size

# Extend your graph object with a breadth-first traversal method that accepts a starting node. Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection.

    def breadth_first_traversal(self, node=Node(None)):
        # check for empty list
        if node.value is None:
            return "Error"

        # declare variables
        visited_nodes = []
        new_queue = []
        
        results = []

        # Add 1st value to lists
        new_queue.append(node)
        visited_nodes.append(node.value)
        
        # Loop through the rest of the graph, skipping previously visited nodes
        while len(new_queue) > 0:
            # increment
            current = new_queue.pop(0)
            # get neighbors
            attached_nodes = self.get_neighbors(current)
            results.append(current.value)

            # loop through all neighbors (might be more than 2)
            for i in attached_nodes:
                if i[0].value in visited_nodes:
                    continue
                else:
                    new_queue.append(i[0])
                    visited_nodes.append(i[0].value)
        return results

# Write a function based on the specifications above, which takes in a graph, and an array of city names. Without utilizing any of the built-in methods available to your language, return whether the full trip is possible with direct flights, and how much it would cost.

# https://www.w3schools.com/python/ref_func_zip.asp
    def get_edge(self, graph=Node(None), locations=[]):
        




graph = Graph()
pandora = graph.add_node('pandora')
arendelle = graph.add_node('arendelle')
metroville = graph.add_node('metroville')
naboo = graph.add_node('naboo')
graph.add_edge(pandora, arendelle)
graph.add_edge(arendelle, metroville)
graph.add_edge(metroville, naboo)
# expected = [pandora, arendelle, metroville, naboo]
print(graph.breadth_first_traversal(pandora))