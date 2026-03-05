# Name: Aryan Solanki
# Roll Number: 2501730347
# Date: 4th March 2026
# Subject: Data Structures and Algorithms
# Assignment: AERT Toolkit

# StackADT
class StackADT:
    def __init__(self):
        self.arr=[]
        
    def push(self,x):
        self.arr.append(x)
    
    def pop(self):
        if len(self.arr)!=0:
            return self.arr.pop()
        return None
    
    def peek(self):
        if len(self.arr)!=0:
            return self.arr[-1]
        return None
    
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        return False
    
    def size(self):
        return len(self.arr)
    

# Factorial
def factorial(n):
    if n<0:
        return " Factorial is not defined for negative numbers :/"
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


# Fibonacci
arr=[-1]*100
arr[0],arr[1]=0,1
count_naive,count_memo=0,0 # To count the number of times recursive calls are made in both approaches
def fib_naive(n):
    '''Naive approach for Fibonacci series'''
    global count_naive
    count_naive += 1
    if n<=1:
        return n
    return fib_naive(n-1)+fib_naive(n-2)

def fib_memo(n):
    '''Memoization approach for Fibonacci series'''
    global count_memo
    count_memo += 1
    if n<=1:
        return n
    if arr[n]!=-1:
        return arr[n]
    arr[n]=fib_memo(n-1)+fib_memo(n-2)
    return arr[n]


# Tower of Hanoi
move_stack = StackADT()
rod_name={1:'A', 2:'B', 3:'C'}
def hanoi(n, start, end):
    if n==1:
        move=(f'Move disk {n} from {rod_name[start]} to {rod_name[end]}')
        move_stack.push(move)
    else:
        auxillary = 6 - (start + end) # Sum of rods : 1+2+3=6
        hanoi(n-1, start, auxillary)
        move=(f'Move disk {n} from {rod_name[start]} to {rod_name[end]}')
        move_stack.push(move)
        hanoi(n-1, auxillary, end)
 
 
# Binary Search
def binary_search(arr, key, low, high):
    if low > high:
        return -1
    
    mid = (low+high)//2
    if arr[mid]==key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    elif key > arr[mid]:
        return binary_search(arr, key, mid + 1, high)
    else:
        return -1


def test_cases():
    # Test cases for StackADT
    stack = StackADT()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f'Top element: {stack.peek()}')  # Should print 3
    print(f'Stack size: {stack.size()}')  # Should print 3

    # Test cases for factorial
    print(f'Factorial of 0: {factorial(0)}')
    print(f'Factorial of 1: {factorial(1)}')
    print(f'Factorial of 5: {factorial(5)}')
    print(f'Factorial of 12: {factorial(12)}')

    # Test cases for Fibonacci
    global count_naive, count_memo
    count_naive, count_memo = 0, 0
    print(f'\nFibonacci (naive) of 10: {fib_naive(10)}')
    print(f"Naive Fibonacci calls: {count_naive}")
    # global count_naive, count_memo
    count_naive, count_memo = 0, 0
    print(f'\nFibonacci (naive) of 20: {fib_naive(20)}')
    print(f"Naive Fibonacci calls: {count_naive}")
    
    count_naive, count_memo = 0, 0
    print(f'\nFibonacci (memoized) of 10: {fib_memo(10)}')
    print(f"Memoized Fibonacci calls: {count_memo}")
    count_naive, count_memo = 0, 0
    print(f'\nFibonacci (memoized) of 20: {fib_memo(20)}')
    print(f"Memoized Fibonacci calls: {count_memo}")

    # Test cases for Tower of Hanoi
    print('Tower of Hanoi for 3 disks and rods A, B, C:')
    hanoi(3, 1, 3)
    for x in move_stack.arr:
        print(x)
    
    # Test cases for Binary Search
    ls= [1,3,5,7,9,11,13]
    print('Array: ',ls)
    print(binary_search(ls, 7, 0, len(ls)- 1))
    print(binary_search(ls, 1, 0, len(ls)- 1))
    print(binary_search(ls, 13, 0, len(ls)- 1))
    print(binary_search(ls, 2, 0, len(ls)- 1))
    arr=[]
    print(binary_search(arr, 1, 0, len(arr)- 1))
    
    
if __name__ == "__main__":
    test_cases()
