from breadth_first import __version__
from breadth_first.breadth_first import BinaryTree, Node
# from queue import Node, Queue


def test_version():
    assert __version__ == '0.1.0'

#happy path

def test_can_successfully_return_a_breadth_first_search():
    new_tree = BinaryTree()
    new_tree.root = Node("A")
    new_tree.root.left = Node("B")
    new_tree.root.right = Node("C")
    new_tree.root.right.left = Node("F") 
    new_tree.root.left.left = Node("D")       
    new_tree.root.left.right = Node("E")  
    expected = ["A", "B", "C", "D", "E", "F"]
    actual = new_tree.breadth_first()
    assert expected == actual

#expected failure 
def test_can_successfully_return_an_error_when_passed_an_empty_tree():
    new_tree = BinaryTree()
    expected = "Please enter a valid tree"
    actual = new_tree.breadth_first()
    assert expected == actual

#edge case
def test_can_successfully_return_a_result_when_passed_an_unbalanced_tree():
    new_tree = BinaryTree()
    new_tree.root = Node(-9)
    new_tree.root.left = Node(-2)
    new_tree.root.left.right = Node(-16)
    new_tree.root.left.left = Node(-10)
    new_tree.root.right = Node(-8) 
    expected = [-9, -2, -8, -10, -16]
    actual = new_tree.breadth_first()
    assert expected == actual