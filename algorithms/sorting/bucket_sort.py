from math import sqrt, ceil
from algorithms.sorting.insertion_sort import insertion_sort


def bucket_sort(arr):
    number_of_buckets = round(sqrt(len(arr)))  # formula
    max_value = max(arr)
    l = []  # list for our buckets

    for i in range(number_of_buckets):
        l.append([])  # adding buckets in l based on number of buckets

    for el in arr:  # putting each el in a bucket
        bucket_index = ceil(el * number_of_buckets / max_value)  # find bucket index (formula)
        l[bucket_index - 1].append(el)  # add the element to the bucket based on bucket index

    for b_index in range(number_of_buckets):  # sorting elements in each bucket
        l[b_index] = insertion_sort(l[b_index])  # quick sort alg would be a better option here

    k = 0
    for i in range(number_of_buckets):  # merge the buckets
        for j in range(len(l[i])):
            arr[k] = l[i][j]
            k += 1

    return arr


print(bucket_sort([5, 8, 2, 4, 6, 7, 2]))
