from fizz_buzz_tree import __version__
from fizz_buzz_tree.fizz_buzz_tree import Node, BinaryTree, fizzBuzzTree, fizz_buzz_helper

def test_version():
    assert __version__ == '0.1.0'


#Happy Path

# If the value is divisible by 3, replace the value with “Fizz”
# If the value is divisible by 5, replace the value with “Buzz”
# If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
# If the value is not divisible by 3 or 5, simply turn the number into a String.

def test_can_successfully_return_a_fizz_buzz_tree():
    b_tree = BinaryTree()
    b_tree.root = Node(1)
    b_tree.root.left = Node(3)
    b_tree.root.right = Node(5)
    b_tree.root.right.left = Node(7) 
    b_tree.root.left.left = Node(15)       
    b_tree.root.left.right = Node(30) 

    test_tree = fizzBuzzTree(b_tree)
    actual = test_tree.preOrder()

    expected = [1, 'Fizz', 'FizzBuzz', 'FizzBuzz', 'Buzz', 7]

    assert expected == actual

#expected failure 
def test_can_successfully_return_an_error_when_passed_an_empty_tree():
    b_tree = BinaryTree()
    expected = [None]
    actual = b_tree.preOrder()
    assert expected == actual

#edge case
def test_can_successfully_return_a_result_when_passed_negative_numbers():
    b_tree = BinaryTree()
    b_tree.root = Node(-9)
    b_tree.root.left = Node(-2)
    b_tree.root.left.right = Node(-16)
    b_tree.root.left.left = Node(-10)
    b_tree.root.right = Node(-15) 

    test_tree = fizzBuzzTree(b_tree)
    actual = test_tree.preOrder()

    expected = ['Fizz', -2, 'Buzz', -16, 'FizzBuzz']
    assert expected == actual