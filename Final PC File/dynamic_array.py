import sys
dyn_arr = []
for i in range(10):
    dyn_arr.append(i)
    print(f"Size: {len(dyn_arr)}, Memory size: {sys.getsizeof(dyn_arr)} bytes")