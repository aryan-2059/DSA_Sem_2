def factorial(n, depth=0):
    indent = "  " * depth
    print(f"{indent}Calling factorial({n})")
    if n == 0 or n == 1:
        print(f"{indent}Returning 1")
        return 1
    res = n * factorial(n - 1, depth + 1)
    print(f"{indent}Returning {res}")
    return res

n = int(input("Enter number: "))
print(f"Result: {factorial(n)}")