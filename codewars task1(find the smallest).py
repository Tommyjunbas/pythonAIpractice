def find_smallest_int(arr):
    # Code here
    smallest = arr[0]
    for number in arr:
        if smallest > number:
            smallest = number
    return smallest
if __name__ == "__main__":
    print(f"find_smallest_int([10, 2, 8]): {find_smallest_int([10, 2, 8])}")