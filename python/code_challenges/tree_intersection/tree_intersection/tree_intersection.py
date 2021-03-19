
class Node: 
    def __init__(self, nodeVal = None, right=None, left=None):
        self.nodeVal = nodeVal
        self.right = right
        self.left = left


class BinaryTree:
    def __init__(self, value=None):
        self.root = Node(value)

    def preOrder(self):
        # root = self.root.nodeVal
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

def tree_intersection(tree_one, tree_two): 
    error_msg = "No common values found"
    tree_one_val = tree_one.preOrder()
    tree_two_val =  tree_two.preOrder()
    commonalities = []
    current_one = tree_one.root
    current_two = tree_two.root
    if current_one is None or current_two is None: 
        return error_msg
    for value in tree_one_val:
        if value in tree_two_val:
            if value in commonalities:
                continue
            else:
                commonalities.append(value)
        else:
            continue
    if len(commonalities) == 0:
        return error_msg
    else: 
        return commonalities




# if __name__ == "__main__":
#     new_tree_one = BinaryTree()
#     new_tree_one.root = Node(5)
#     new_tree_one.root.left = Node(7)
#     new_tree_one.root.right = Node(54)   
#     new_tree_one.root.left.left = Node(4)
#     new_tree_one.root.left.right = Node(35)

#     new_tree_two = BinaryTree()
#     new_tree_two.root = Node(45)
#     new_tree_two.root.left = Node(4)
#     new_tree_two.root.right = Node(5)   
#     new_tree_two.root.right.left = Node(55)
#     new_tree_two.root.right.right = Node(57)
    
#     print("Pre Order",new_tree_one.preOrder())
