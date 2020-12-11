# Could have simplified by using the .insert method or  "start stop step"

def insertShiftArray(arr, val):
    halfsies = round(((len(arr))/2))
    for index in arr:
        # Check for edge cases
        if len(arr) == False:
            return (val)
            break
        elif len(arr) == 1:
            return (arr[0], val)
            break
        elif len(arr) == 2:
            return (arr[0], val, arr[1])
            break    
        elif index == 1:
            return (arr[0], arr[1])
            continue
        else:
            # If arr passes all edge case tests, run the rest through a series of if statements
            if index == halfsies:
                return (val)
            elif index < halfsies:
                return (arr[index])
            else:
                return (arr[index-1])
    

insertShiftArray([1,2,3,4,5,6], 11)



