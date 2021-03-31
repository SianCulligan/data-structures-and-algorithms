class Node: 
    def __init__(self, nodeVal = None, right=None, left=None):
        self.nodeVal = nodeVal
        self.right = right
        self.left = left

# Depth first traversal is where we prioritize going through the depth (height) of the tree first. 


class BinaryTree:
    def __init__(self, value=None):
        self.root = Node(value)

# Pre-order: root >> left >> right
    def preOrder(self):
        if self.root is None: 
            return "Root is empty"

        root_list = []  

        def traverse(root):
            root_list.append(root.nodeVal)
            if root.left is not None: 
                print()
                traverse(root.left)
            if root.right is not None: 
                traverse(root.right)
        
        traverse(self.root)

        print("ROOT LIST", root_list)
        return root_list 

# In-order: left >> root >> right
    def inOrder(self):
        if self.root is None: 
            return "Root is empty"

        root_list = []  

        def traverse(root):
            if root.left is not None: 
                traverse(root.left)
            root_list.append(root.nodeVal)
            if root.right is not None: 
                traverse(root.right)
        
        traverse(self.root)

        print("ROOT LIST", root_list)
        return root_list 

# Post-order: left >> right >> root
    def postOrder(self):
        if self.root is None: 
            return "Root is empty"

        root_list = []  

        def traverse(root):
            if root.left is not None: 
                traverse(root.left)
            if root.right is not None: 
                traverse(root.right)
            root_list.append(root.nodeVal)
        
        traverse(self.root)

        print("ROOT LIST", root_list)
        return root_list    

class BinarySearchTree(BinaryTree):
    def __init__(self, root):
        super().__init__(root, root)

    def add(self, add_val):
        new_node = Node(add_val)

        if self.root is None: 
            self.root = new_node
            print("New root node added", new_node.nodeVal)
            return
        
        current = self.root
        while current:
            if current.nodeVal > add_val:
                if current.left is None :
                    current.left=new_node
                    return
                else:
                    current = current.left;
            elif current.nodeVal < add_val:
                if current.right is None :
                    current.right=new_node
                    return
                else:
                    current = current.right;
            elif current.nodeVal == add_val:
                return
                
    def contains(self, contains_val):
        current = self.root;
        while current:
            if current.nodeVal > contains_val:
                currnet = current.left
            elif current.nodeVal < contains_val:
                current = current.right
            elif current.nodeVal == contains_val:
                return True
        return False

