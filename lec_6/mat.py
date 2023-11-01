import random

def create_random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def calculate_column_total(matrix, column_index):
    if not matrix or column_index < 0 or column_index >= len(matrix[0]):
        return 0
    total = sum(row[column_index] for row in matrix)
    return total

def calculate_row_avg(matrix, row_index):
    if not matrix or row_index < 0 or row_index >= len(matrix):
        return 0
    row = matrix[row_index]
    avg = sum(row) / len(row)
    return avg

random_matrix = create_random_matrix(3, 4)
print("Generated Matrix:")
for row in random_matrix:
    print(row)

column_index = 2 
column_total = calculate_column_total(random_matrix, column_index)
print(f"Total of column {column_index}: {column_total}")

row_index = 1  
row_avg = calculate_row_avg(random_matrix, row_index)
print(f"Average of row {row_index}: {row_avg}")
