class Node:
    def __init__(self, nodeVal=None, right=None, left=None):
        self.nodeVal = nodeVal
        self.left = left
        self.right = right


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
                print()
                traverse(root.left)
            if root.right is not None: 
                traverse(root.right)
        traverse(self.root)
        print("ROOT LIST", root_list)
        return root_list 
    



def fizzBuzzTree(tree):
    newTree = BinaryTree()
    newTree.root = fizz_buzz_helper(tree.root)
    return newTree

def fizz_buzz_helper(root):
    newNode = None
    if root is None: 
        return "Root is empty"    
    if root.nodeVal % 15 == 0:
        newNode = Node('FizzBuzz')
    elif root.nodeVal % 3 == 0:
        newNode = Node('Fizz')            
    elif root.nodeVal % 5 == 0:
        newNode = Node('Buzz')   
    else: 
        newNode = Node(root.nodeVal)
    if root.left is not None:
        newNode.left = fizz_buzz_helper(root.left)
    if root.right is not None:
        newNode.right = fizz_buzz_helper(root.right)
    return newNode


# if __name__ = "__main__":
#     b_tree = BinaryTree()
#     b_tree.root = Node(1)
#     b_tree.root.left = Node(3)
#     b_tree.root.right = Node(5)
#     b_tree.root.right.left = Node(7) 
#     b_tree.root.left.left = Node(15)       
#     b_tree.root.left.right = Node(30) 




# expected = new_tree.preOrder()
# print(expected)

# new_tree = BinaryTree()
# new_tree.root = Node(1)
# print(new_tree.root.nodeVal)
# new_tree.root.left = Node(2)
# print(new_tree.root.left.nodeVal)
# new_tree.root.right = Node(3)   
# print(new_tree.root.right.nodeVal)



# b_tree = BinaryTree()
# b_tree.root = Node(1)
# b_tree.root.left = Node(3)
# b_tree.root.right = Node(5)
# b_tree.root.right.left = Node(7) 
# b_tree.root.left.left = Node(15)       
# b_tree.root.left.right = Node(30) 


# b_tree = BinaryTree()
# b_tree.root = Node(-9)
# b_tree.root.left = Node(-2)
# b_tree.root.left.right = Node(-16)
# b_tree.root.left.left = Node(-10)
# b_tree.root.right = Node(-15)


# new_tree = fizzBuzzTree(b_tree)
# expected = new_tree.preOrder()
# print("EXPECTED", expected)
# # print(b_tree.preOrder())










































