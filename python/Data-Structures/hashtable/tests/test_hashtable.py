from hashtable import __version__
from hashtable.hashtable import HashTable


def test_version():
    assert __version__ == '0.1.0'


def test_can_successfully_hash_a_key():
    new_hashtable = HashTable()
    expected = 16
    actual = new_hashtable._hash("pi")
    assert expected == actual


def test_can_successfully_add_and_retrieve_a_key_value():
    new_hashtable = HashTable()
    new_hashtable.add("pi", 3.14)
    expected = 3.14
    actual = new_hashtable.get("pi")
    assert expected == actual


def test_returns_null_for_a_key_that_does_not_exist():
    new_hashtable = HashTable()
    new_hashtable.add("pi", 3.14)
    expected = False
    actual = new_hashtable.get("pie")
    assert expected == actual
