from array_shift import insertShiftArray

# Happy Path
def test_insert_a_val_into_the_middle_of_an_array():
    expected = [1, 2, 3, 11, 4, 5, 6]
    actual = insertShiftArray([1,2,3,4,5,6], 11)
    assert expected is actual, "Happy path test passes"

# Expected failure
def test_should_print_nothing_if_array_is_empty():
    expected = []
    actual = insertShiftArray([], 11)
    assert expected is actual, "Expected failure test passes"

# Edge Case
def test_should_round_the_halfway_point_to_the_nearest_whole_number_if_array_length_is_odd():
    expected = [1, 2, 11, 3]
    actual = insertShiftArray([1,2,3], 11)
    assert expected is actual, "Edge case test passes"