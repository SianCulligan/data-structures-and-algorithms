from linked_list.linked_list import Node, LinkedList

def test_can_successfully_instantiate_an_empty_linked_list():
    newList = LinkedList()
    expected = None
    actual = newList.headVal
    assert expected == actual

def test_can_properly_insert_into_the_linked_list():
    newList = LinkedList()
    newList.insert("Head Node Inserted")
    expected = "Head Node Inserted"
    actual = newList.headVal.nodeVal
    assert expected == actual

def test_head_property_will_properly_point_to_the_first_node_in_the_linked_list():
    newList = LinkedList()
    newList.insert("Two")
    newList.insert("One")
    expected = "One"
    actual = newList.headVal.nodeVal
    assert expected == actual

def test_can_properly_insert_multiple_nodes_into_the_linked_list():
    newList = LinkedList()
    newList.insert("Three")
    newList.insert("Two")
    newList.insert("One")
    expected = [newList.headVal.nodeVal, newList.headVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nodeVal]
    actual = ["One", "Two", "Three"]
    assert expected == actual

def test_return_true_when_finding_a_value_within_the_linked_list_that_exists():
    newList = LinkedList()
    newList.insert("Three")
    newList.insert("Two")
    newList.insert("One") 
    newList.includes("Two")  
    expected = newList.includes("Three")
    actual = True
    assert expected == actual    

def test_return_false_when_searching_for_a_value_in_the_linked_list_that_does_not_exist():
    newList = LinkedList()
    newList.insert("Three")
    newList.insert("Two")
    newList.insert("One") 
    newList.includes("Two")  
    expected = newList.includes("Four")
    actual = False
    assert expected == actual  

def test_can_properly_return_a_collection_of_all_the_values_that_exist_in_the_linked_list():
    newList = LinkedList()
    newList.insert("Three")
    newList.insert("Two")
    newList.insert("One")
    expected = [newList.headVal.nodeVal, newList.headVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nodeVal]
    actual = ["One", "Two", "Three"]
    assert expected == actual 

def test_can_successfully_add_a_node_to_the_end_of_the_linked_list():
    newList = LinkedList()
    newList.insert("Three")
    newList.insert("Two")
    newList.insert("One")
    newList.append("Four")
    expected = [newList.headVal.nodeVal, newList.headVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nextVal.nodeVal]
    actual = ["One", "Two", "Three", "Four"]
    assert expected == actual


def test_can_successfully_add_multiple_nodes_to_the_end_of_a_linked_list():
    newList = LinkedList()
    newList.insert("Three")
    newList.insert("Two")
    newList.insert("One")
    newList.append("Four")
    newList.append("Five")
    expected = [newList.headVal.nodeVal, newList.headVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nextVal.nextVal.nodeVal]
    actual = ["One", "Two", "Three", "Four", "Five"]
    assert expected == actual


def test_can_successfully_insert_a_node_before_a_node_located_i_the_middle_of_a_linked_list():
    newList = LinkedList()
    newList.insert("Three")
    newList.insert("Two")
    newList.insert("One")
    newList.insertBefore("Two", "Added")

    expected = [newList.headVal.nodeVal, newList.headVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nextVal.nodeVal]
    actual = ["One", "Added", "Two", "Three"]
    assert expected == actual

def test_can_successfully_insert_a_node_before_the_first_node_of_a_linked_list():
    newList = LinkedList()
    newList.insert("Three")
    newList.insert("Two")
    newList.insert("One")
    expected = "One"
    actual = newList.headVal.nodeVal
    assert expected == actual

def test_can_successfully_insert_after_a_node_in_the_middle_of_the_linked_list():
    newList = LinkedList()
    newList.insert("Three")
    newList.insert("Two")
    newList.insert("One")
    newList.insertBefore("Two", "Four")
    expected = [newList.headVal.nodeVal, newList.headVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nextVal.nodeVal]
    actual = ["One", "Four", "Two", "Three"]
    assert expected == actual

def test_can_successfully_insert_a_node_after_the_last_node_of_the_linked_list():
    newList = LinkedList()
    newList.insert("Three")
    newList.insert("Two")
    newList.insert("One")
    newList.insertAfter("Three", "Four")
    expected = [newList.headVal.nodeVal, newList.headVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nodeVal, newList.headVal.nextVal.nextVal.nextVal.nodeVal]
    actual = ["One", "Two", "Three", "Four"]
    assert expected == actual








# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list

def test_k_is_greater_than_the_length_of_the_linked_list():
    newList = LinkedList()
    newList.insert(2)
    newList.insert(8)
    newList.insert(3)
    newList.insert(1)
    expected = "Exception"
    actual = newList.kthFromEnd(6)
    assert expected == actual

def test_k_and_the_length_of_the_list_are_the_same():
    newList = LinkedList()
    newList.insert(2)
    newList.insert(8)
    newList.insert(3)
    newList.insert(1)
    expected = "Exception"
    actual = newList.kthFromEnd(4)
    assert expected == actual

def test_k_and_the_length_of_the_list_are_the_same():
    newList = LinkedList()
    newList.insert(2)
    newList.insert(8)
    newList.insert(3)
    newList.insert(1)
    expected = '3'
    actual = newList.kthFromEnd(2)
    assert expected == actual

def test_k_is_not_a_positive_integer():
    newList = LinkedList()
    newList.insert(2)
    newList.insert(8)
    newList.insert(3)
    newList.insert(1)
    expected = "Exception"
    actual = newList.kthFromEnd(-2)
    assert expected == actual

def test_where_the_linked_list_is_of_a_size_one():
    newList = LinkedList()
    newList.insert(2)
    expected = "2"
    actual = newList.kthFromEnd(0)
    assert expected == actual

def test_where_k_is_not_at_the_end_but_somewhere_in_the_middle_of_the_linked_list():
    newList = LinkedList()
    newList.insert(2)
    newList.insert(8)
    newList.insert(3)
    newList.insert(1)
    expected = "3"
    actual = newList.kthFromEnd(2)
    assert expected == actual