class DynamicArray:
    def __init__(self, arr, capacity=1):
        self.arr = arr
        self.size = len(arr) # Number of elements in array
        self.capacity = max(capacity, len(arr)) #Total space allocated
        
    def append(self, x):
        if self.size == self.capacity:
            print("Length exceeded.\nExtending capacity...")
            new_arr = [None] * (2*self.capacity)
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
            self.capacity *= 2
        if self.size < len(self.arr):
            self.arr[self.size] = x
        else:
            self.arr.append(x)
        self.size += 1
        print('Element added!')
            
    def pop(self):
        if self.size == 0:
            print('UNDERFLOW :/')
        else:
            self.size -= 1
            print(self.arr[self.size])
            
    def print_array(self):
        print("Array: ")
        print(self.arr[:self.size])
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_start(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self,x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = new_node
    
    def delete_by_value(self, x):
        if self.head is None:
            print('Empty List')
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        ptr = self.head
        preptr = None
        while ptr is not None and ptr.data != x:
            preptr = ptr
            ptr = ptr.next
        if ptr is None:
            print('Element not found')
        else:
            preptr.next = ptr.next
            ptr.next = None
            
    def traverse(self):
        if self.head is None:
            print('Empty List')
        ptr = self.head
        arr = []
        while ptr is not None:
            arr.append(ptr.data)
            ptr = ptr.next
        print('List: ', arr)

class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_after_node(self, target, x):
        ptr = self.head
        while ptr:
            if ptr.data == target:
                new_node = DoubleNode(x)
                new_node.prev = ptr
                new_node.next = ptr.next
                if ptr.next is not None: # If the target is not at the end of the list
                    ptr.next.prev = new_node
                else:
                    self.tail = new_node
                ptr.next = new_node
                print('Element added!')
                return
            ptr = ptr.next
        print('Target not found')
        
    def insert_at_end(self, x):
        new_node = DoubleNode(x)
        if self.head is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
            
    def delete_at_position(self, pos):
        if self.head is None:
            print('Empty List')
        if pos == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            print('Element deleted!')
            return
        ptr = self.head
        count = 0
        while ptr and count < pos:
            ptr = ptr.next
            count += 1
        if ptr is None:
            print('Position out of bounds')
        else:
            if ptr.prev is not None:
                ptr.prev.next = ptr.next
            else:
                self.head = ptr.next
            if ptr.next is not None:
                ptr.next.prev = ptr.prev
            else:
                self.tail = ptr.prev
            print('Element deleted!')
            
    def traverse(self):
        if self.head is None:
            print('Empty List')
        ptr = self.head
        arr = []
        while ptr is not None:
            arr.append(ptr.data)
            ptr = ptr.next
        print('List: ', arr)
            
class Stack:
    def __init__(self):
        self.stackLL = SinglyLinkedList()
        self.size = 0
        
    def push(self, x):
        self.stackLL.insert_at_start(x) # O(1) time complexity
        self.size += 1
        print('Element added!')
        
    def pop(self):
        if self.size == 0:
            print('UNDERFLOW :/')
        else:
            val = self.stackLL.head.data
            self.stackLL.head = self.stackLL.head.next # O(1) time complexity
            self.size -= 1
            print(f'Element popped: {val}')
            
    def peek(self):
        if self.stackLL.head is None:
            print('Stack is empty')
        else:
            print(f'Top element: {self.stackLL.head.data}')
            
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def enqueue(self, x):
        new_node = Node(x)
        if self.tail is None: # If the queue is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print('Element added!')
        
    def dequeue(self):
        if self.head is None:
            print('UNDERFLOW :/')
        else:
            val = self.head.data
            self.head = self.head.next
            if self.head is None: # If the queue becomes empty after dequeue
                self.tail = None
            self.size -= 1
            print(f'Element dequeued: {val}')
            
    def front(self):
        if self.head is None:
            print('Queue is empty')
        else:
            print(f'Front element: {self.head.data}')
            
def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expr:
        if char in '({[': # If it's an opening bracket
            stack.push(char)
        elif char in ')}]': # If it's a closing bracket
            if stack.size == 0:
                return False
            top = stack.stackLL.head.data
            if top == pairs[char]:
                stack.pop()
            else:
                return False
    
    return stack.size == 0

# ======================================
# TEST CASES
# ======================================
if __name__ == "__main__":
    # Test Dynamic Array
    print("Testing Dynamic Array...")
    print("\n[Test 1.1] Start with capacity=2, append 10+ items")
    da = DynamicArray([], capacity=2)
    for i in range(10):
        da.append(i)
    da.print_array()
    
    print("\n[Test 1.2] Pop 3 elements")
    da.pop()
    da.pop()
    da.pop()
    da.print_array()
    
    # Test Singly Linked List
    print("\nTesting Singly Linked List...")
    sll = SinglyLinkedList()
    print("\n[Test 2A.1] Insert 3 at beginning")
    sll.insert_at_start(10)
    sll.insert_at_start(20)
    sll.insert_at_start(30)
    sll.traverse()
 
    print("\n[Test 2A.2] Insert 3 at end")
    sll.insert_at_end(40)
    sll.insert_at_end(50)
    sll.insert_at_end(60)
    sll.traverse()
 
    print("\n[Test 2A.3] Delete value 20")
    sll.delete_by_value(20)
    sll.traverse()
 
    print("\n[Test 2A.4] Delete head (30)")
    sll.delete_by_value(30)
    sll.traverse()
 
    print("\n[Test 2A.5] Delete non-existent value (99)")
    sll.delete_by_value(99)
    sll.traverse()
    
    # Test Doubly Linked List
    print("\nTesting Doubly Linked List...")
    dll = DoublyLinkedList()
    
    for val in [10, 20, 30, 40, 50]:
        dll.insert_at_end(val)
 
    print("\n[Test 2B.1] Initial list")
    dll.traverse()
 
    print("\n[Test 2B.2] Insert 25 after node with value 20")
    dll.insert_after_node(20, 25)
    dll.traverse()
 
    print("\n[Test 2B.3] Insert after last node (50)")
    dll.insert_after_node(50, 99)
    dll.traverse()
 
    print("\n[Test 2B.4] Delete at position 1 (0-based)")
    dll.delete_at_position(1)
    dll.traverse()
 
    print("\n[Test 2B.5] Delete at position 0 (head)")
    dll.delete_at_position(0)
    dll.traverse()
 
    print("\n[Test 2B.6] Delete last element (by going to last index)")
    # Count nodes to find last index
    ptr = dll.head
    count = 0
    while ptr:
        count += 1
        ptr = ptr.next
    dll.delete_at_position(count - 1)
    dll.traverse()
    
    
    # Test Stack
    print("\nTesting Stack...")
    stack = Stack()
    print("\n[Test 3A.1] Push 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"  Peek (top): {stack.peek()}")
 
    print("\n[Test 3A.2] Pop twice")
    print(f"  Popped: {stack.pop()}")
    print(f"  Popped: {stack.pop()}")
    print(f"  Peek now: {stack.peek()}")
 
    print("\n[Test 3A.3] Underflow test")
    stack.pop()
    stack.pop() 
    
    
    # Test Queue
    print("\nTesting Queue...")
    queue = Queue()
    print("\n[Test 3B.1] Enqueue 1, 2, 3")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"  Front: {queue.front()}")
 
    print("\n[Test 3B.2] Dequeue twice")
    print(f"  Dequeued: {queue.dequeue()}")
    print(f"  Dequeued: {queue.dequeue()}")
    print(f"  Front now: {queue.front()}")
 
    print("\n[Test 3B.3] Underflow test")
    queue.dequeue()
    queue.dequeue()

    # Test balanced parantheses
    print("\nTesting Balanced Parentheses...")
    test_exprs = ["()", "([])", "{[()]", "((())", "({)}", "([)]", ""]
    for expr in test_exprs:
        print(f"\n[Test 4.1] Expression: '{expr}'")
        print(f"  Balanced? {is_balanced(expr)}")
        
    print("\nAll tests completed!")
        