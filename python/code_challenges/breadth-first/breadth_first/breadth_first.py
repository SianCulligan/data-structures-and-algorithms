from queue import Queue

class Node: 
    def __init__(self, nodeVal = None, right=None, left=None):
        self.nodeVal = nodeVal
        self.right = right
        self.left = left


############################################################################################

class BinaryTree:
    def __init__(self, value=None):
        self.root = Node(value)
        
    def breadth_first(self): 
        if self.root is None: 
            return "Root is empty"

        return_list = [] 

        new_queue = Queue() 
        new_queue.enqueue(self.root) 

        while not new_queue.is_empty():
            current = new_queue.dequeue()

            if current is None:
                break

            return_list.append(current.nodeVal)

            if current.left is not None:
                new_queue.enqueue(current.left)

            if current.right is not None:
                new_queue.enqueue(current.right)
        return return_list




new_tree = BinaryTree()
new_tree.root = Node("A")
new_tree.root.left = Node("B")
new_tree.root.right = Node("C")
new_tree.root.right.left = Node("F") 
new_tree.root.left.left = Node("D")       
new_tree.root.left.right = Node("E")  

print(new_tree.breadth_first())

            # a
    # b               c
# d     e           f

# expected a b c d e f