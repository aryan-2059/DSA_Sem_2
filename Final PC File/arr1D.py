arr = [10, 20, 30, 40, 50]
def insert_with_cost(val, pos):
    print(f"Inserting {val} at {pos}")
    shift_count = len(arr) - pos
    arr.insert(pos, val)
    print(f"Result: {arr}, Shifting operations: {shift_count}")

insert_with_cost(25, 2)