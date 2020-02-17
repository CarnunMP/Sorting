# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # loop through arr
    swaps = True

    while swaps:
        swaps = False

        for i in range(len(arr) - 1):
            current_num = arr[i]
            next_num = arr[i + 1]

            # compare each element to its neighbour
            if current_num > next_num:
                # If needed, swap them
                arr[i] = next_num
                arr[i + 1] = current_num
                swaps = True

    # If no swaps performed this loop, stop
    # Else, repeat

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr