# spare matrix class
class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        
    def create(self, row, col):
        self.matrix = [[0 for i in range(col)] for j in range(row)]
    
    def set(self, row, col, value):
        if row >= self.rows or col >= self.cols:
            raise ValueError("Index out of range")
        else:
            self.matrix[row][col] = value
    def get(self, row, col):
        return self.matrix[row][col]

    def show(self):
        # print the sparse matrix
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.matrix[i][j], end=" ")
            print()
# Create a 3x3 sparse matrix
matrix = SparseMatrix(3, 3)
matrix.create(3, 3)

# matrix.create(3, 3)
# Set some non-zero values
matrix.set(0, 0, 1)
matrix.set(1, 1, 2)
matrix.set(2, 2, 3)

# Print the matrix
matrix.show()
print(matrix.get(2, 2))
print(matrix.get(1, 2))