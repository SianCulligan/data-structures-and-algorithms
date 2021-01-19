from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import Node, AnimalShelter


def test_version():
    assert __version__ == '0.1.0'

def test_can_successfully_enqueue():
    new_shelter = AnimalShelter()
    new_shelter.enqueue("dog")
    new_shelter.enqueue("dog")
    new_shelter.enqueue("cat")
    expected = "cat"
    actual = new_shelter.front.nodeVal
    assert expected == actual

def test_can_successfully_enqueue_single_node():
    new_shelter = AnimalShelter()
    new_shelter.enqueue("cat")
    expected = "cat"
    actual = new_shelter.front.nodeVal
    assert expected == actual

def test_can_successfully_dequeue():
    new_shelter = AnimalShelter()
    new_shelter.enqueue("dog")
    expected = "dog"
    actual = new_shelter.dequeue("dog")
    assert expected == actual

def test_can_successfully_return_an_error_when_shelter_is_empty():
    new_shelter = AnimalShelter()
    expected = "Null"
    actual = new_shelter.dequeue("dog")
    assert expected == actual

def test_can_successfully_return_an_error_when_user_inputs_animal_other_than_cat_or_dog():
    new_shelter = AnimalShelter()
    new_shelter.enqueue("dog")
    expected = "Null"
    actual = new_shelter.dequeue("lizard")  
    assert expected == actual

