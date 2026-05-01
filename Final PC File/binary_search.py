def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        print(f"Checking mid-index {mid} (value: {arr[mid]})")
        if arr[mid] == x: return mid
        elif arr[mid] > x: return binary_search(arr, low, mid - 1, x)
        else: return binary_search(arr, mid + 1, high, x)
    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
x = 23
print(f"Element {x} at index: {binary_search(arr, 0, len(arr)-1, x)}")