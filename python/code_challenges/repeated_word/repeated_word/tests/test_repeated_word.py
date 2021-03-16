from repeated_word import __version__
from repeated_word.repeated_word import HashTable, repeated_word


def test_version():
    assert __version__ == '0.1.0'


# HAPPY PATH 
def test_picks_first_repeated_word():
    expected = "a", 10
    actual = repeated_word("Once upon a time, there was a brave princess who")
    assert actual == expected


# EDGE CASE 
def test_empty_list():
    expected = "No repeating words ¯\_(ツ)_/¯", 0
    actual = repeated_word("")
    assert actual == expected

# EXPECTED FAIL
def test_no_repeated_words():
    expected = "No repeating words ¯\_(ツ)_/¯", 4
    actual = repeated_word("Once upon a time")
    assert actual == expected

#STRETCH GOAL
def test_counts_the_number_of_words():
    expected = "summer", 23
    actual = repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    assert actual == expected
