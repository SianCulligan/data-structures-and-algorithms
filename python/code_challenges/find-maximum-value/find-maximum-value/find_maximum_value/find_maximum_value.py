class Node: 
    def __init__(self, nodeVal = None, right=None, left=None):
        self.nodeVal = nodeVal
        self.right = right
        self.left = left

# Depth first traversal is where we prioritize going through the depth (height) of the tree first. 
class BinaryTree:
    def __init__(self, value=None):
        self.root = Node(value)

    def preOrder(self):
        if self.root is None: 
            return "Root is empty"
        root_list = []  
        def traverse(root):
            root_list.append(root.nodeVal)
            if root.left is not None: 
                traverse(root.left)
            if root.right is not None: 
                traverse(root.right)
        traverse(self.root)
        return root_list

    def find_maximum_value(self):
        root = self.root
        if root.nodeVal is None: 
            return "Please enter a valid tree"

        value_list = self.preOrder()
        current_max = float(int())      
        print("val List", value_list)
        for i in value_list:
            if i > current_max:
                current_max = i
            else:
                continue

        return current_max

# Atempted to write this the way I wrote my white board, but didn't work! Whoops. Here's a working version ^^ I felt gross deleting all my other work..
        # root = self.root
        # if root is None: 
        #     return "Please enter a valid tree"
        # root_max = root.nodeVal
        # left_max = int()
        # right_max = int()

        # def traverse(root):
        #     if root.left:
        #         left_max = self.find_maximum_value(root.left)
        #     if root.right:
        #         right_max = self.find_maximum_value(root.right)
        
        # traverse(root)
            
        # current_max = root_max

        # if left_max > current_max:
        #     current_max = left_max
        # if right_max > current_max:
        #     current_max = right_max
        
        # return current_max
            


new_tree = BinaryTree()
# new_tree.root = Node(9)
# new_tree.root.left = Node(2)
# new_tree.root.left.right = Node(16)
# new_tree.root.left.left = Node(10)

# new_tree.root.right = Node(8) 
# new_tree.root.right.right = Node(99)
# new_tree.root.right.left = Node(3)  


print(new_tree.find_maximum_value())