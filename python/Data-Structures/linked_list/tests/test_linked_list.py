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

