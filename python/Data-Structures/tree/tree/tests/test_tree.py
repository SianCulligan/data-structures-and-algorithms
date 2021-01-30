from tree import __version__
from tree.tree import BinarySearchTree, BinaryTree, Node


def test_version():
    assert __version__ == '0.1.0'

def test_can_successfully_instantiate_an_empty_tree():
    new_tree = BinaryTree()
    expected = None
    actual = new_tree.root.nodeVal
    assert expected == actual

def test_can_successfully_instantiate_a_tree_with_a_single_root_node():
    new_tree = BinaryTree()
    new_tree.root = Node(1)
    expected = 1
    actual = new_tree.root.nodeVal
    assert expected == actual

def test_can_successfully_add_a_left_child_and_right_child_to_a_single_root_node():
    new_tree = BinaryTree()
    new_tree.root = Node(1)
    new_tree.root.left = Node(2)
    new_tree.root.right = Node(3)    
    expected = [1, 2, 3]
    actual = new_tree.preOrder()
    assert expected == actual

def test_can_successfully_return_a_collection_from_a_preorder_traversal():
    new_tree = BinaryTree()
    new_tree.root = Node("A")
    new_tree.root.left = Node("B")
    new_tree.root.right = Node("C")
    new_tree.root.right.left = Node("F") 
    new_tree.root.left.left = Node("D")       
    new_tree.root.left.right = Node("E")       
    expected = ["A", "B", "D", "E", "C", "F"]
    actual = new_tree.preOrder()
    assert expected == actual

def test_can_successfully_return_a_collection_from_an_inorder_traversal():
    new_tree = BinaryTree()
    new_tree.root = Node("A")
    new_tree.root.left = Node("B")
    new_tree.root.right = Node("C")
    new_tree.root.right.left = Node("F") 
    new_tree.root.left.left = Node("D")       
    new_tree.root.left.right = Node("E")       
    expected = ["D", "B", "E", "A", "F", "C"]
    actual = new_tree.inOrder()
    assert expected == actual


def test_can_successfully_return_a_collection_from_a_postorder_traversal():
    new_tree = BinaryTree()
    new_tree.root = Node("A")
    new_tree.root.left = Node("B")
    new_tree.root.right = Node("C")
    new_tree.root.right.left = Node("F") 
    new_tree.root.left.left = Node("D")       
    new_tree.root.left.right = Node("E")       
    expected = ["D", "E", "B", "F", "C", "A"]
    actual = new_tree.postOrder()
    assert expected == actual
