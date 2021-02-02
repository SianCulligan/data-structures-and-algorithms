from find_maximum_value import __version__
from find_maximum_value.find_maximum_value import BinaryTree, Node


def test_version():
    assert __version__ == '0.1.0'

#happy path
def test_can_successfully_instantiate_an_empty_tree():
    new_tree = BinaryTree()
    expected = None
    actual = new_tree.root.nodeVal
    assert expected == actual

def test_can_successfully_return_max_value():
    new_tree = BinaryTree()
    new_tree.root = Node(9)
    new_tree.root.left = Node(2)
    new_tree.root.left.right = Node(16)
    new_tree.root.left.left = Node(10)

    new_tree.root.right = Node(8) 
    new_tree.root.right.right = Node(99)
    new_tree.root.right.left = Node(3) 
    expected = 99
    actual = new_tree.find_maximum_value()
    assert expected == actual

#expected failure 
def test_can_successfully_return_an_error_when_passed_an_empty_tree():
    new_tree = BinaryTree()
    expected = "Please enter a valid tree"
    actual = new_tree.find_maximum_value()
    assert expected == actual

#edge case
def test_can_successfully_return_a_result_when_passed_negative_values():
    new_tree = BinaryTree()
    new_tree.root = Node(-9)
    new_tree.root.left = Node(-2)
    new_tree.root.left.right = Node(-16)
    new_tree.root.left.left = Node(-10)
    new_tree.root.right = Node(-8) 
    expected = -9
    actual = new_tree.root.nodeVal
    assert expected == actual