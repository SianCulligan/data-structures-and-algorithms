class Node:
    def __init__(self, nodeVal=None, nextVal=None):
        self.nodeVal = nodeVal
        self.nextVal = nextVal

class PseudoQueue: 

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear 
    
#enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
    def enqueue(self, val_to_add): 
        if self.isempty() is True:
            self.front, self.rear = Node(val_to_add, None), Node(val_to_add, None)

        holder = self.front
        self.front = Node(val_to_add, holder)
        
        return self.front.nodeVal

# Input	Args	Output
# [10]->[15]->[20]	5	[5]->[10]->[15]->[20]
#  	5	[5]


#dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.
    def dequeue(self): 
        node_to_remove = self.front
        if self.isempty() is True: 
            return "Exception"
        while self.front:
            if self.front.nextVal is None:
                holder = self.front
                self.front = None
                print(holder.nodeVal)
                return holder.nodeVal
            else: 
                self.front = self.front.nextVal



    def printer_helper(self):
        printval = self.front
        listItOut = []
        while printval:
            if printval.nextVal is not None: 
                to_string = str(printval.nodeVal)
                listItOut.append("[" + to_string + "] ->")
                printval = printval.nextVal
            else: 
                to_string = str(printval.nodeVal)
                listItOut.append("[" + to_string + "]")
                printval = printval.nextVal

        print(listItOut)
        
    def isempty(self):
        if self.front is None and self.rear is None: 
            print("True")
            return True
        else: 
            print("False")
            return False


class Stack: 
    def __init__(self, top=None):
        self.top = top

    def push(self, add_to_top):
        node_to_push = Node(add_to_top)
        if self.isempty() is True:
            self.top = node_to_push
        
        else:
            node_to_push.nextVal = self.top
            self.top = node_to_push
            return node_to_push.nodeVal

    def pop(self):
        holder = self.top
        if self.isempty():
            return "Exception"
        else: 
            self.top = holder.nextVal
            return holder.nodeVal

    def peek(self):
        if self.isempty():
            return "Exception"
        else:
            return self.top.nodeVal        

    def isempty(self):
        if self.top is None: 
            print("True")
            return True
        else: 
            print("False")
            return False