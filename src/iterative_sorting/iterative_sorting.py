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
    try:
        # need to find the maximum element
        maximum = max(arr)

        # generate an array, counts, with length of max + 1
        counts = [0] * (maximum + 1)

        # loop over arr, counting instances of each element at the corresponding index of counts
        for num in arr:
            if num < 0:
                return "Error, negative numbers not allowed in Count Sort"
            
            counts[num] += 1

        # loop over counts, summing pairs of elements
        for i in range(len(counts) - 1):
            counts[i + 1] += counts[i]
        
        # shift everything in counts one spot to the right, and put 0 in 0
        counts_copy = counts
        for i in reversed(range(len(counts) - 1)):
            counts[i + 1] = counts[i]
        counts[0] = 0
        
        result = [0] * len(arr)
        # loop back through arr, placing each element at the index indicated by counts, then increment it
        for num in arr:
            result[counts[num]] = num
            counts[num] += 1

        return result
    except ValueError:
        return []