class Node():

    def __init__(self, value=None, nextVal=None):
        self.value = value
        self.nextVal = nextVal

############################################################################################

class Queue: 
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear 

# Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
    def enqueue(self, add_to_back):
        node_to_queue = Node(add_to_back)
        if self.is_empty() is True:
            self.front = node_to_queue
            self.rear = node_to_queue
            return node_to_queue
        else:
            self.rear.nextVal = node_to_queue
            self.rear = self.rear.nextVal

# Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
# Should raise exception when called on empty queue
    def dequeue(self):
        node_to_remove = self.front
        if self.is_empty() is True: 
            return "Exception"
        else:
            self.front = self.front.nextVal
            node_to_remove.nextVal = None
            return node_to_remove.value

# Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
# Should raise exception when called on empty queue
    def peek(self):
        if self.isempty() is True: 
            return "Exception"
        return self.front.value


# Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.
    def is_empty(self):
        return not self.front

