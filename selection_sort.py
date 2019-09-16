def sortFun(arr):
    for i in range(len(arr)):
        if i > i+1:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            print(i)
            print(arr)

print(sortFun([4,6,3,2,1]))