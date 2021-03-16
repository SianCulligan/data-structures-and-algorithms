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
# --------------------


def test_contains_and_add():
    hashtable = HashTable()
    hashtable.add('glisten', 'glitter')
    expected = True
    actual = hashtable.contains('glisten')
    assert actual == expected


def test_get():
    hashtable = HashTable()
    hashtable.add('glisten', 'glitter')
    expected = 'glitter'
    actual = hashtable.get('glisten')
    assert actual == expected