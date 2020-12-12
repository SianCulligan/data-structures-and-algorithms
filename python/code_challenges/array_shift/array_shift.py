def insertShiftArray(arr, val):
    # Check for edge cases
    if len(arr) == False:
        print(val)
        return (val)
    elif len(arr) == 1:
        arr.insert(1, val)
        return (arr)
    halfsies = round(((len(arr))/2))
    print(halfsies)
    arr.insert(halfsies, val)
    print(arr)
    return arr

insertShiftArray([1, 2, 3, 4, 5, 6, 7], 11)