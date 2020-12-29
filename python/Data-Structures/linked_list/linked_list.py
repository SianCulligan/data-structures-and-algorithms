class Node:
    def __init__(self, nodeVal=None, nextVal=None):
        self.nodeVal = nodeVal
        self.nextVal = nextVal

class LinkedList:
    def __init__(self, headVal=None):
        self.headVal = headVal

    def insert(self, val):
        strVal = str(val)
        insertNode = Node(strVal)
        if self.headVal is not None: 
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


# .append(value) which adds a new node with the given value to the end of the list
    def append(self, value):
        current = self.headVal
        if current is None: 
            self.headVal = Node(value)
        while current != None:
            if current.nextVal == None:
                createNewNode = Node(value)
                current.nextVal = createNewNode
                return 
            else:
                current = current.nextVal

# .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
    def insertBefore(self, insertBeforeVal, newlyAddedVal): 
        # lastVal = None
        current = self.headVal
        newNode = Node(newlyAddedVal)
        if current is None: 
            self.headVal = newNode
        while current != None: 
            if current.nextVal.nodeVal == insertBeforeVal:
                placeholder = current.nextVal
                current.nextVal = Node(newlyAddedVal, placeholder)
                return
            elif current.nextVal.nodeVal != insertBeforeVal:
                current = current.nextVal
            else:
                return "Exception"


# .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node
    def insertAfter(self, value, newValue):
        current = self.headVal
        newNode = Node(newValue)
        if current is None: 
            self.headVal = newNode
        while current != None: 
            if current.nodeVal == value:
                placeholder = current.nextVal
                current.nextVal = Node(newValue, placeholder)
                return
            elif current.nodeVal != value:
                current = current.nextVal
            else:
                return "Exception"               






newList = LinkedList()
newList.insert("Three")
newList.toString()
newList.insert("Two")
newList.toString()
newList.insert("One")
newList.toString()
newList.insertAfter("Two", "ADDED")
print("----------------")
newList.toString()