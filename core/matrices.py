# Matrices.py: All basic operations within matrices (could be used with single numbers as well)

def matrix_sum(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        print("Cannot sum two matrices that aren't both quadratic!")
    else:
        for i in range(len(matrix1)):
            matrix1[i] += matrix2[i]
        return matrix1
    
def matrix_subtract(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        print("Cannot sum two matrices that aren't both quadratic!")
    else:
        for i in range(len(matrix1)):
            matrix1[i] -= matrix2[i]
        return matrix1
    
def matrix_multiply(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        print("Cannot sum two matrices that aren't both quadratic!")
    else:
        for i in range(len(matrix1)):
            matrix1[i] *= matrix2[i]
        return matrix1

def matrix_quotient(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        print("Cannot sum two matrices that aren't both quadratic!")
    else:
        for i in range(len(matrix1)):
            matrix1[i] /= matrix2[i]
        return matrix1