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

# Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
    def kthFromEnd(self, k): 
        values = self.__str__()
        lengthVal = len(values)
        if k >= 0 and k < lengthVal:
            placeholderIndex = ((lengthVal - 1) - k)
            # print(values[placeholderIndex])
            return values[placeholderIndex]
        else:
            # print("Exception")
            return "Exception"           


    def __str__(self):
        output = ''
        current = self.headVal
        while current is not None:
            output += f'{current.nodeVal}'
            current = current.nextVal
        print(output)
        return output        

    def middleOfList(self): 
        values = self.__str__()
        middleVal = (round((len(values))/2))-1
        if middleVal >= 0:
            print(values[middleVal])
            return values[middleVal]
        else:
            print("Exception")
            return "Exception"                  


