def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    min_num = arr[0]
    max_num = arr[0]
    
    for num in arr:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    total_sum = sum(arr)
    solution = total_sum - min_num - max_num
    
    return solution