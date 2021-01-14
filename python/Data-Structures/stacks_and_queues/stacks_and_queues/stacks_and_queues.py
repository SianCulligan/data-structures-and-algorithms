from stacks_and_queues.linked_list_helper import Node, LinkedList, zip_lists


class Node:
    def __init__(self, nodeVal=None, nextVal=None):
        self.nodeVal = nodeVal
        self.nextVal = nextVal




############################################################################################
class Stack: 
    def __init__(self, top=None):
        self.top = top

# Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
    def push(self, add_to_top):
        node_to_push = Node(add_to_top)
        if self.isempty() is True:
            self.top = node_to_push
        
        else:
            node_to_push.nextVal = self.top
            self.top = node_to_push
            return node_to_push.nodeVal


# Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
# Should raise exception when called on empty stack
    def pop(self):
        holder = self.top
        if self.isempty():
            return "Exception"
        else: 
            self.top = holder.nextVal
            return holder.nodeVal

# Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
# Should raise exception when called on empty stack        
    def peek(self):
        if self.isempty():
            return "Exception"
        else:
            return self.top.nodeVal        

# Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty
    def isempty(self):
        if self.top is None: 
            print("True")
            return True
        else: 
            print("False")
            return False



############################################################################################
class Queue: 
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear 

# Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
    def enqueue(self, add_to_back):
        node_to_queue = Node(add_to_back)
        if self.isempty() is True:
            self.front = node_to_queue
            self.rear = node_to_queue
            return node_to_queue
        self.rear.nextVal = node_to_queue
        self.rear = node_to_queue
        return node_to_queue



# Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
# Should raise exception when called on empty queue
    def dequeue(self):
        node_to_remove = self.front
        if self.isempty() is True: 
            return "Exception"
        self.front = self.front.nextVal
        node_to_remove.nextVal = None
        self.rear = None
        return node_to_remove.nodeVal


# Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
# Should raise exception when called on empty queue
    def peek(self):
        if self.isempty() is True: 
            return "Exception"
        return self.front.nodeVal


# Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.
    def isempty(self):
        if self.front is None and self.rear is None: 
            print("True")
            return True
        else: 
            print("False")
            return False



