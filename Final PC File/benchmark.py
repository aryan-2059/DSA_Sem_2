import random, time
def insertion(a):
    a = a.copy()
    for i in range(1, len(a)):
        key, j = a[i], i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def merge(a):
    if len(a) <= 1: return a
    m = len(a)//2
    l, r = merge(a[:m]), merge(a[m:])
    res, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]: res.append(l[i]); i += 1
        else: res.append(r[j]); j += 1
    return res + l[i:] + r[j:]

def quick(a):
    if len(a) <= 1: return a
    p = a[len(a)//2]
    left = [x for x in a if x < p]
    mid  = [x for x in a if x == p]
    right= [x for x in a if x > p]
    return quick(left) + mid + quick(right)

def gen(n, case, seed):
    random.seed(seed)
    if case == "random": return [random.randint(1, 100000) for _ in range(n)]
    if case == "sorted": return list(range(n))
    return list(range(n, 0, -1))  # reverse
def run():
    sizes = [1000, 5000, 10000]
    cases = ["random", "sorted", "reverse"]
    algos = {"Insertion": insertion, "Merge": merge, "Quick": quick}

    print(f"{'Size':<6}{'Case':<10}{'Algo':<10}{'Time(s)':<10}")
    print("-"*36)

    for n in sizes:
        for c in cases:
            data = gen(n, c, 42)
            for name, f in algos.items():
                t1 = time.perf_counter()
                f(data)
                t2 = time.perf_counter()
                print(f"{n:<6}{c:<10}{name:<10}{(t2-t1):<10.5f}")

run()