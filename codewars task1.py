def find_smallest_int(arr):
    # Code here
    smallest = arr[0]
    for number in arr:
        if smallest > number:
            smallest = number
    return smallest