stack = []
MAX = 5

def push(item):
    if len(stack) < MAX:
        stack.append(item)
        print(f"Pushed {item}")
    else:
        print("Stack Overflow")

def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print(f"Popped {stack.pop()}")

def peek():
    if stack:
        print(f"Top: {stack[-1]}")
    else:
        print("Stack is empty")

while True:
    print("\n1. Push 2. Pop 3. Peek 4. Exit")
    ch = input("Enter choice: ")
    if ch == '1': push(int(input("Item: ")))
    elif ch == '2': pop()
    elif ch == '3': peek()
    elif ch == '4': break