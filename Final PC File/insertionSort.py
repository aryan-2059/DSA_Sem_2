def insertion_sort(arr):
    comps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            else: break
        arr[j+1] = key
    return comps

print(f"Comps (Sorted): {insertion_sort([1,2,3,4,5])}")
print(f"Comps (Reverse): {insertion_sort([5,4,3,2,1])}")