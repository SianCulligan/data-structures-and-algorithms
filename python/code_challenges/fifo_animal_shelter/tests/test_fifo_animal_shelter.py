from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import Node, AnimalShelter, Animal, Dog, Cat


def test_version():
    assert __version__ == '0.1.0'

def test_can_successfully_enqueue():
    littleton = Animal.Dog('Littleton')
    # new_shelter = AnimalShelter()
    # new_shelter.enqueue(littleton)

    expected = "littleton"
    actual = littleton.name
    assert expected == actual
