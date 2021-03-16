# from hashtable import __version__
# from hashtable.hashtable import HashTable


# def test_version():
#     assert __version__ == '0.1.0'


# def test_can_successfully_hash_a_key():
#     new_hashtable = HashTable()
#     expected = 16
#     actual = new_hashtable._hash("pi")
#     assert expected == actual


# def test_can_successfully_add_and_retrieve_a_key_value():
#     new_hashtable = HashTable()
#     new_hashtable.add("pi", 3.14)
#     expected = 3.14
#     actual = new_hashtable.get("pi")
#     assert expected == actual


# def test_returns_null_for_a_key_that_does_not_exist():
#     new_hashtable = HashTable()
#     new_hashtable.add("pi", 3.14)
#     expected = False
#     actual = new_hashtable.get("pie")
#     assert expected == actual


from hashtable.hashtable import HashTable, LinkedList


def test_create():
    hashtable = HashTable()
    assert hashtable


def test_predictable_hash():
    hashtable = HashTable()
    initial = hashtable._hash('spam')
    secondary = hashtable._hash('spam')
    assert initial == secondary


def test_in_range_hash():
    hashtable = HashTable()
    actual = hashtable._hash('spam')

    # assert actual >= 0
    # assert actual < hashtable._size

    assert 0 <= actual < hashtable.initial_size


def test_same_hash():
    hashtable = HashTable()
    initial = hashtable._hash('listen')
    secondary = hashtable._hash('silent')
    assert initial == secondary


def test_different_hash():
    hashtable = HashTable()
    initial = hashtable._hash('glisten')
    secondary = hashtable._hash('silent')
    assert initial != secondary
