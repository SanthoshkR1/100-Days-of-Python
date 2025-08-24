def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if target is not found

arr = [3, 5, 6, 7, 8]  # Array should be sorted for binary search
target = 5
index = binary_search(arr, target)
print("Binary search result:", index)