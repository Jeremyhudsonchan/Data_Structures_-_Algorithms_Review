class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = {}

    def set(self, row, col, value):
        if row >= self.rows or col >= self.cols:
            raise ValueError("Index out of range")
        if value == -1:
            if (row, col) in self.matrix:
                del self.matrix[(row, col)]
        else:
            self.matrix[(row, col)] = value
    
    def get(self, row, col):
        if row >= self.rows or col >= self.cols:
            raise ValueError("Index out of range")
        return self.matrix.get((row, col), 0)
    
    def __str__(self):
        s = ""
        for row in range(self.rows):
            for col in range(self.cols):
                s += str(self.get(row, col)) + " "
            s += "\n"
        return s

# Create a 3x3 sparse matrix
matrix = SparseMatrix(3, 3)

# Set some non-zero values
matrix.set(0, 0, 1)
matrix.set(1, 1, 2)
matrix.set(2, 2, 3)

# Print the matrix
print(matrix)

print(matrix.get(0, 1))
print(matrix.get(1, 1))
