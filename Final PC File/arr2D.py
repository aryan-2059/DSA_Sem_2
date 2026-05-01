matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f"Element at [{i}][{j}]: {matrix[i][j]}")
        total += matrix[i][j]
print(f"Matrix Sum: {total}")