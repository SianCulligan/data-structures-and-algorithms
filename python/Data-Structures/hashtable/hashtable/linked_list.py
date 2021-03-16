class Node:
    def __init__(self, nodeVal=None, next=None):
        self.nodeVal = nodeVal
        self.next = next

class LinkedList:
    def __init__(self, headVal=None):
        self.headVal = headVal

    def insert(self, data):
        node = Node(data)
        if not self.headVal:
            self.headVal =  node
        else: 
            current = self.headVal
            while current.next: 
                current = current.next
            current.next = node

    def display(self):
        printval = self.headVal
        listItOut = []
        while printval is not None:
            listItOut.append("{" + printval.nodeVal + "} ->")
            printval = printval.next
        if printval is None: 
            listItOut.append("NULL")
        print(listItOut)
        return listItOut
