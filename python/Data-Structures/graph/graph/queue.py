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

