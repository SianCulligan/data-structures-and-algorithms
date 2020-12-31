from array_binary_search import __version__
from array_binary_search.array_binary_search import BinarySearch


def test_version():
    assert __version__ == '0.1.0'

# -------HAPPY PATH----------
def test_checking_a_value_that_exists_in_the_array():
    expected = 4
    actual = BinarySearch([1,2,3,4,5,6], 5)
    assert expected is actual, "Happy path test passes"


# -------EDGE CASE----------
def test_checking_a_value_that_does_not_exist_in_the_array():
    expected = -1
    actual = BinarySearch([1,2,3], 11)
    assert expected is actual, "Edge case test passes"

# -------EXPECTED FAILURE---------
def test_should_still_print_neg_one_if_passed_a_string():
    expected = -1
    actual = BinarySearch([1,2,3,4,5,6], "hi!")
    assert expected is actual, "Expected failure test passes"