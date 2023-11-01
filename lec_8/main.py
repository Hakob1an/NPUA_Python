import random

class Matrix:
    def __init__(self, n, m):
        if not isinstance(n, int) or not isinstance(m, int) or n <= 0 or m <= 0:
            raise ValueError("Matrix dimensions must be positive integers.")
        self._rows = n
        self._cols = m
        self.matrix = [[random.randint(-50, 50) for _ in range(m)] for _ in range(n)]

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        total = sum(sum(row) for row in self.matrix)
        mean = total / (self._rows * self._cols)
        return mean

    def calculate_row_sum(self, row_index):
        if 0 <= row_index < self._rows:
            return sum(self.matrix[row_index])
        return "Invalid row index"

    def calculate_col_average(self, col_index):
        if 0 <= col_index < self._cols:
            col_sum = sum(row[col_index] for row in self.matrix)
            col_average = col_sum / self._rows
            return col_average
        return "Invalid column index"

    def print_submatrix(self, col1, col2, row1, row2):
        if 0 <= row1 <= row2 < self._rows and 0 <= col1 <= col2 < self._cols:
            for i in range(row1, row2 + 1):
                print(self.matrix[i][col1:col2 + 1])
        else:
            print("Submatrix indices are out of bounds")

if __name__ == "__main__":
    n = 4
    m = 4
    my_matrix = Matrix(n, m)

    my_matrix.print_matrix()

    mean = my_matrix.calculate_mean()
    print("Mean of the matrix:", mean)

    row_sum = my_matrix.calculate_row_sum(2)
    print("Sum of row 2:", row_sum)

    col_avg = my_matrix.calculate_col_average(1)
    print("Average of column 1:", col_avg)

    my_matrix.print_submatrix(1, 3, 0, 2)
