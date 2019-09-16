def selectionSort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp
    return list


print(selectionSort([5, 2, 1, 9, 0, 4, 6]))
