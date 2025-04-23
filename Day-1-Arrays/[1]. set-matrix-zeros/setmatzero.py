def set_matrix_zero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row = [0] * rows
    col = [0] * cols

    # Mark the rows and columns that need to be set to zero
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    # Set the elements to zero based on the marked rows and columns
    for i in range(rows):
        for j in range(cols):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0

    # Print the modified matrix
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()

# Example usage
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
set_matrix_zero(matrix)