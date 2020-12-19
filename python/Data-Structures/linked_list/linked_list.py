class Node:
    def __init__(self, nodeVal=None):
        self.nodeVal = nodeVal
        self.nextVal = None

class LinkedList:
    def __init__(self):
        self.headVal = None

    def insert(self, val):
        strVal = str(val)
        insertNode = Node(strVal)
        insertNode.nextVal = self.headVal
        self.headVal = insertNode

    def toString(self):
        printval = self.headVal
        listItOut = []
        while printval is not None:
            listItOut.append("{" + printval.nodeVal + "} ->")
            printval = printval.nextVal
        if printval is None: 
            listItOut.append("NULL")
        print(listItOut)

    def includes(self, val):
        start = self.headVal
        if start == None:
            return False
        while start != None:
            if start.nodeVal != val and start.nextVal == None:
                print("False")
                return False               
            elif start.nodeVal == val:
                print("True")
                return True
            elif start.nodeVal != val:
                start = start.nextVal
            





list = LinkedList()
print("========")
print(list)
# list.headVal = Node("mon")
# e2 = Node("tues")
# e3 = Node("wed")

# # Link first Node to second node
# list.headVal.nextVal = e2

# # Link second Node to third node
# e2.nextVal = e3

# list.toString()

# list.insert("sun")
# print("---------------------")
# list.toString()
# print("---------------------")
# list.includes("mon")
# print("******************")
