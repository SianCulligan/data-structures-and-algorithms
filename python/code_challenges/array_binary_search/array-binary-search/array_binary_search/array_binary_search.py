# TWO WAYS OF DOING THIS PROBLEM

# def BinarySearch(arr, val):
#     indexCount = 0
#     if val not in arr:
#         print(-1)
#         return(-1)
#     else:
#         for i in arr: 
#             if i == val:
#                 print(indexCount)
#                 return indexCount
#             elif i != val:
#                 indexCount += 1



def BinarySearch(arr, val):
    high = (len(arr))-1
    low = 0
    mid = round(len(arr)/2)
    if val > arr[high]:
        return(-1)
    elif val < arr[low]:
        return(-1)  
    else :
        for i in arr:
            if val == arr[mid]:
                return mid
            elif val > arr[mid]:
                mid = (round(high/mid)) + mid
                continue
            elif val < arr[mid]:
                mid = round(mid/2)
                continue
            else:
                return(-1)


BinarySearch([4,8,15,16,23,33,34,35, 36, 37, 38 ,39, 40, 41, 42, 77], 77)
