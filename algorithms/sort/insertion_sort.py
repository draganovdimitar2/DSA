def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            print(arr[j+1], arr[j])
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


print(insertion_sort([5, 8, 2, 4, 6, 7, 2]))
