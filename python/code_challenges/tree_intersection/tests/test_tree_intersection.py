from tree_intersection import __version__
from tree_intersection.tree_intersection import BinaryTree, Node, tree_intersection


def test_version():
    assert __version__ == '0.1.0'

# ------------------- HAPPY PATH ------------------------
def test_returns_results_when_passed_two_regular_binary_trees():
    new_tree_one = BinaryTree()
    new_tree_one.root = Node(5)
    new_tree_one.root.left = Node(7)
    new_tree_one.root.right = Node(54)   
    new_tree_one.root.left.left = Node(4)
    new_tree_one.root.left.right = Node(35)

    new_tree_two = BinaryTree()
    new_tree_two.root = Node(45)
    new_tree_two.root.left = Node(4)
    new_tree_two.root.right = Node(5)   
    new_tree_two.root.right.left = Node(55)
    new_tree_two.root.right.right = Node(57)

    expected = [5, 4]
    actual = tree_intersection(new_tree_one, new_tree_two)
    assert expected == actual


# ------------------- EDGE CASE ------------------------
def test_returns_error_when_passed_an_empty_tree():
    new_tree_one = BinaryTree()
    new_tree_one.root = Node(5)
    new_tree_one.root.left = Node(7)
    new_tree_one.root.right = Node(54)   
    new_tree_one.root.left.left = Node(4)
    new_tree_one.root.left.right = Node(35)

    new_tree_two = BinaryTree()

    expected = "No common values found"
    actual = tree_intersection(new_tree_one, new_tree_two)
    assert expected == actual

# ------------------- EXPECTED FAIL ------------------------

def test_returns_error_when_passed_trees_with_no_common_vals():
    new_tree_one = BinaryTree()
    new_tree_one.root = Node(5)
    new_tree_one.root.left = Node(7)
    new_tree_one.root.right = Node(54)   
    new_tree_one.root.left.left = Node(4)
    new_tree_one.root.left.right = Node(35)

    new_tree_two = BinaryTree()
    new_tree_two.root = Node(77)
    new_tree_two.root.left = Node(88)
    new_tree_two.root.right = Node(99)   
    new_tree_two.root.right.left = Node(111)
    new_tree_two.root.right.right = Node(222)

    expected = "No common values found"
    actual = tree_intersection(new_tree_one, new_tree_two)
    assert expected == actual