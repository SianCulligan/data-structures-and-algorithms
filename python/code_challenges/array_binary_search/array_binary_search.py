def BinarySearch(arr, val):
    indexCount = 0
    if val not in arr:
        print(-1)
        return(-1)
    else:
        for i in arr: 
            if i == val:
                print(indexCount)
                return indexCount
            elif i != val:
                indexCount += 1



BinarySearch([4,8,15,16,23,42], 16)
