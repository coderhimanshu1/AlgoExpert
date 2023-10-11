def transposeMatrix(matrix):
    if not matrix:
        return []


    # Number of rows and columns
    rows, cols = len(matrix), len(matrix[0])


    # Create a new transposed matrix
    transposed = [[None] * rows for _ in range(cols)]


    for row in range(rows):
        for col in range(cols):
            transposed[col][row] = matrix[row][col]


    return transposed

