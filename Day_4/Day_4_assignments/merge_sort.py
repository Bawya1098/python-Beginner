def mergesort(list_array):
    if (len(list_array) == 1):
        return list_array
    mid = int(len(list_array) / 2)
    left = mergesort(list_array[:mid])
    right = mergesort(list_array[mid:])
    return mergesort(left, right)


arr = [1, 2, 4, 3, 8, 7]
print(mergesort(arr))
