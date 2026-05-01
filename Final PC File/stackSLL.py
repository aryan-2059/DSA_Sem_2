class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # head is top

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None
    
def check_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty():
                return False
            if stack.pop() != pairs[char]:
                return False

    return stack.is_empty()
tests = [
    "((1+2)*3)",
    "{[()]}",
    "{[(])}",
    "(((",
    "[]{}()",
    "(]"
]

for t in tests:
    print(f"{t} -> {check_balanced(t)}")