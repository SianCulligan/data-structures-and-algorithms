class Node:
    def __init__(self, nodeVal=None, rightVal=None, leftVal=None):
        this.nodeVal = nodeVal
        this.leftVal = leftVal
        this.rightVal = rightVal


class BinaryTree:
    def __init__(self, value=None):
        self.root = Node(value)

    def fizz_buzz_helper(self, root):
        newNode = None

        if root.nodeVal % 15 == 0:
            newNode = Node('FizzBuzz')
        elif root.nodeVal % 3 == 0:
            newNode = Node('Fizz')            
        elif root.nodeVal % 5 == 0:
            newNode = Node('Buzz')   
        else: 
            newNode = Node(root.nodeVal)

        if root.left is not None:
            newNode.left = self.fizz_buzz_helper(root.left)

        if root.right is not None:
            newNode.right = self.fizz_buzz_helper(root.right)

        return newNode


    def fizzBuzzTree(self, oldTree):
        newTree = BinaryTree()
        newTree.root = fizz_buzz_helper(oldTree.root)
        return newTree
















































