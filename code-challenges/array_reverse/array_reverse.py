def arrayReverse(arr):
    arrCount = len(arr)-1
    while arrCount >= 0:
        print (arr[arrCount])
        arrCount -= 1


exampleList = [5,4,3,2,1]
arrayReverse(exampleList)