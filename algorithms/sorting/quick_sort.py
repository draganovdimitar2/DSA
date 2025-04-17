def swap(some_list, idx_1, idx_2):  # helper func to swap values
    some_list[idx_1], some_list[idx_2] = some_list[idx_2], some_list[idx_1]


def pivot(my_list, pivot_idx, end_idx):
    swap_idx = pivot_idx  # initially they are the same
    for i in range(pivot_idx + 1, end_idx + 1):  # exclude the first element (pivot idx)
        if my_list[i] < my_list[pivot_idx]:  # check if the number is smaller than the pivot number
            swap_idx += 1  # increase swap idx
            swap(my_list, swap_idx, i)  # swap the swap_idx num with i_idx num
    swap(my_list, pivot_idx, swap_idx)  # when loop ends swap pivot_idx num with swap_idx num
    return swap_idx  # return only the idx so that we can get the left and right parts of the list


def quick_sort_helper(my_list, left, right):
    if left < right:  # base recursive case
        pivot_idx = pivot(my_list, left, right)  # find the middle pivot_idx
        quick_sort_helper(my_list, left, pivot_idx - 1)  # sort the left side of the list
        quick_sort_helper(my_list, pivot_idx + 1, right)  # sort the right side of the list
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)


l = [3, 5, 0, 6, 2, 1, 4]
print(quick_sort(l))
