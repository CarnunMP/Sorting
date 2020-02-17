# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    left_smallest_index = 0
    right_smallest_index = 0

    for i in range(0, elements):
        print(i, left_smallest_index, right_smallest_index)

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

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
