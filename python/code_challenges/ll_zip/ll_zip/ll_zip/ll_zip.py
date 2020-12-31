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
#----------------------------------------------------------------
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





def zip_lists(list_one, list_two):
    helper_one = list_one.__str__()
    helper_two = list_two.__str__()
    lengthOne = len(helper_one)
    lengthTwo = len(helper_two)
    zipped_list = LinkedList()
    start = 0

    #account for 0 length
    if lengthOne == 0 or lengthTwo == 0:
        if lengthOne == 0 and lengthTwo == 0 :
            print("Empty Lists")
            return "Lists are empty"
        elif lengthOne == 0:
            print(list_two)
            return list_two
        elif lengthTwo == 0:
            print(list_one)
            return list_one

    #happy path
    elif lengthOne == lengthTwo: 
        while start < lengthOne:
            zipped_list.append(helper_one[start])
            zipped_list.append(helper_two[start])
            start += 1
        print("ZIP")
        print(zipped_list)
        return zipped_list

    #One is longer than two
    elif lengthOne > lengthTwo:
        while start < lengthOne:
            zipped_list.append(helper_one[start])
            if start <= (lengthTwo-1): 
                zipped_list.append(helper_two[start])
            start += 1
        print("ZIP 1 is longer")
        print(zipped_list)
        return zipped_list

    #Two is longer than one
    else: 
        while start < lengthTwo:
            if start <= (lengthOne-1): 
                zipped_list.append(helper_one[start])
            zipped_list.append(helper_two[start])
            start += 1
        print("ZIP 2 is longer")
        print(zipped_list)
        return zipped_list


# newList = LinkedList()
# newList.insert(5)
# newList.insert(3)
# newList.insert(1)
# # print("NEW LIST 1")
# # print(newList)

# newList2 = LinkedList()
# newList2.insert(8)
# newList2.insert(6)
# newList2.insert(4)
# newList2.insert(2)
# # print("NEW LIST 2")
# # print(newList2)

# zip_lists(newList, newList2)

