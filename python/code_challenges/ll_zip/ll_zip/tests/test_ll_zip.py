from ll_zip import __version__
from ll_zip.ll_zip import Node, LinkedList, zip_lists


def test_version():
    assert __version__ == '0.1.0'

#*************************happy path*************************
def test_can_successfully_zip_two_linked_lists():
    newList = LinkedList()
    newList.insert(5)
    newList.insert(3)
    newList.insert(1)

    newList2 = LinkedList()
    newList2.insert(6)
    newList2.insert(4)
    newList2.insert(2)

    answer = zip_lists(newList, newList2)

    expected = ['1', '2', '3', '4', '5', '6']
    actual = [answer.headVal.nodeVal, answer.headVal.nextVal.nodeVal, answer.headVal.nextVal.nextVal.nodeVal, answer.headVal.nextVal.nextVal.nextVal.nodeVal, answer.headVal.nextVal.nextVal.nextVal.nextVal.nodeVal, answer.headVal.nextVal.nextVal.nextVal.nextVal.nextVal.nodeVal]

    assert expected == actual




#*************************expected fail*************************

def test_can_return_an_error_():
    newList = LinkedList()
    newList2 = LinkedList()
    answer = zip_lists(newList, newList2)

    expected = "Lists are empty"
    actual = answer

    assert expected == actual





#*************************edge cases*************************

def test_can_successfully_zip_two_linked_lists_of_different_lengths():
    newList = LinkedList()
    newList.insert(1)

    newList2 = LinkedList()
    newList2.insert(6)
    newList2.insert(5)
    newList2.insert(4)
    newList2.insert(3)
    newList2.insert(2)

    answer = zip_lists(newList, newList2)

    expected = ['1', '2', '3', '4', '5', '6']
    actual = [answer.headVal.nodeVal, answer.headVal.nextVal.nodeVal, answer.headVal.nextVal.nextVal.nodeVal, answer.headVal.nextVal.nextVal.nextVal.nodeVal, answer.headVal.nextVal.nextVal.nextVal.nextVal.nodeVal, answer.headVal.nextVal.nextVal.nextVal.nextVal.nextVal.nodeVal]

    assert expected == actual

