import time
import random
import copy
import sys

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements greater than key one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # keeps it stable (equal elements preserve order)
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append remaining elements from either half
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1             # i tracks boundary of 'smaller than pivot' region
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


def measure_time(sort_func, arr):
    arr_copy = copy.deepcopy(arr)
    start = time.perf_counter()

    if sort_func == quick_sort:
        quick_sort(arr_copy, 0, len(arr_copy) - 1)
    else:
        sort_func(arr_copy)

    end = time.perf_counter()
    return round((end - start) * 1000, 4)   # milliseconds


def generate_datasets(sizes, seed=42):
    datasets = {}
    random.seed(seed)
    for n in sizes:
        rand_list    = [random.randint(1, 100000) for _ in range(n)]
        sorted_list  = list(range(1, n + 1))
        reverse_list = list(range(n, 0, -1))
        datasets[n] = {
            'random':  rand_list,
            'sorted':  sorted_list,
            'reverse': reverse_list
        }
    return datasets


def run_experiments(datasets, sizes):
    algorithms = [
        ('Insertion Sort', insertion_sort),
        ('Merge Sort',     merge_sort),
        ('Quick Sort',     quick_sort),
    ]
    input_types = ['random', 'sorted', 'reverse']
    results = {}

    header = f"{'Size':>7} | {'Input Type':>12} | {'Insertion Sort (ms)':>20} | {'Merge Sort (ms)':>16} | {'Quick Sort (ms)':>16}"
    divider = "-" * len(header)

    print(divider)
    print(header)
    print(divider)

    for n in sizes:
        for itype in input_types:
            arr = datasets[n][itype]
            t_ins   = measure_time(insertion_sort, arr)
            t_merge = measure_time(merge_sort,     arr)
            t_quick = measure_time(quick_sort,     arr)
 
            results[(n, itype)] = {
                'Insertion Sort': t_ins,
                'Merge Sort':     t_merge,
                'Quick Sort':     t_quick,
            }
            print(f"{n:>7} | {itype:>12} | {t_ins:>20} | {t_merge:>16} | {t_quick:>16}")

    print(divider)
    return results


if __name__ == "__main__":
    # Increase recursion limit for Quick Sort on sorted/reverse inputs (worst case)
    sys.setrecursionlimit(50000)
    print("=" * 60)
    print("CORRECTNESS VERIFICATION")
    print("=" * 60)

    test_input = [5, 2, 9, 1, 5, 6]
    expected   = [1, 2, 5, 5, 6, 9]

    ins_result   = insertion_sort(list(test_input))
    merge_result = merge_sort(list(test_input))
    qs_arr       = list(test_input)
    quick_sort(qs_arr, 0, len(qs_arr) - 1)

    print(f"\n  Input:          {test_input}")
    print(f"  Expected:       {expected}")
    print(f"  Insertion Sort: {ins_result}  {'PASS' if ins_result == expected else 'FAIL'}")
    print(f"  Merge Sort:     {merge_result}  {'PASS' if merge_result == expected else 'FAIL'}")
    print(f"  Quick Sort:     {qs_arr}  {'PASS' if qs_arr == expected else 'FAIL'}")

    print("\n" + "=" * 60)
    print("PERFORMANCE MEASUREMENT (times in milliseconds)")
    print("=" * 60 + "\n")

    sizes    = [1000, 5000, 10000]
    datasets = generate_datasets(sizes)
    results  = run_experiments(datasets, sizes)