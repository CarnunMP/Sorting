# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    left_smallest_index = 0
    right_smallest_index = 0

    for i in range(0, elements):
        if left_smallest_index >= len(arrA):
            merged_arr[i] = arrB[right_smallest_index]
            right_smallest_index += 1
        elif right_smallest_index >= len(arrB):
            merged_arr[i] = arrA[left_smallest_index]
            left_smallest_index += 1
        elif arrA[left_smallest_index] <= arrB[right_smallest_index]:
            merged_arr[i] = arrA[left_smallest_index]
            left_smallest_index += 1
        else:
            merged_arr[i] = arrB[right_smallest_index]
            right_smallest_index += 1
    
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) <= 1: # base case
        return arr
    else:
        # split
        middle_index = len(arr) // 2
        left_arr = arr[:middle_index]
        right_arr = arr[middle_index:]

        # sort the parts
        sorted_left = merge_sort(left_arr)
        sorted_right = merge_sort(right_arr)

        # and merge
        return merge(sorted_left, sorted_right)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    # Okay. So I think the idea is: start, mid, and end are indices which describe two arrays.
    # Might as well start by making copies of them!
    # (Question: as these copies are only temporary, do they affect space complexity?)

    left_arr = arr[start: mid + 1]
    right_arr = arr[mid + 1: end + 1]

    # Then merge as before:
    elements = len( left_arr) + len( right_arr )
    merged_arr = [0] * elements

    left_smallest_index = 0
    right_smallest_index = 0

    for i in range(0, elements):
        if left_smallest_index >= len(left_arr):
            merged_arr[i] = right_arr[right_smallest_index]
            right_smallest_index += 1
        elif right_smallest_index >= len(right_arr):
            merged_arr[i] = left_arr[left_smallest_index]
            left_smallest_index += 1
        elif left_arr[left_smallest_index] <= right_arr[right_smallest_index]:
            merged_arr[i] = left_arr[left_smallest_index]
            left_smallest_index += 1
        else:
            merged_arr[i] = right_arr[right_smallest_index]
            right_smallest_index += 1

    # And finally, loop over merged_arr, copying elements back to arr:
    for i, num in enumerate(merged_arr):
        arr[i + start] = num

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    if r - l >= 1:
        # split
        middle_index = l + ((r - l) // 2)

        # sort the parts
        arr = merge_sort_in_place(arr, l, middle_index)
        arr = merge_sort_in_place(arr, middle_index + 1, r)

        # and merge
        return merge_in_place(arr, l, middle_index, r)
    else:
        return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
