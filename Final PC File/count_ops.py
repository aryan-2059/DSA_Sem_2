def counted_search(arr, target):
    ops = 0
    for i in range(len(arr)):
        ops += 1
        if arr[i] == target:
            print(f"Found at {i}. Total operations: {ops}")
            return
    print(f"Not found. Total operations: {ops}")

arr = [10, 20, 30, 40, 50]
print("Best Case (10):")
counted_search(arr, 10)
print("Worst Case (50):")
counted_search(arr, 50)