# A matrix - Sparsely populated
matrix1 = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 2, 0, 7],
    [0, 0, 0, 5]
]

matrix2 = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 2, 0, 7],
    [0, 0, 0, 5]
]

matrix3 = [
    [0, 1, 0, 0],
    [0, 2, 0, 7],
    [0, 0, 0, 5]
]

def convert_to_sparse(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    meta = [num_rows, num_cols, 0]
    sparseMatrix = []
    sparseMatrix.append(meta)

    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] != 0:
                lst = []
                lst.append(i)
                lst.append(j)
                lst.append(matrix[i][j])
                sparseMatrix[0][2] += 1
                sparseMatrix.append(lst)  

    return sparseMatrix

def print_sparse_matrix(sparseMatrix):
    for row in sparseMatrix:
        print(row)

def sparseAdd(sp1, sp2):
    pass

def Test1():
    spMtrx1 = convert_to_sparse(matrix1)
    print_sparse_matrix(spMtrx1)


def Test2():
    spMtrx1 = convert_to_sparse(matrix1)
    spMtrx2 = convert_to_sparse(matrix2)
    # print_sparse_matrix(spMtrx)

    res = sparseAdd(spMtrx1, spMtrx2)
    print_sparse_matrix(res)

    res = sparseAdd(spMtrx1, spMtrx3)
    print_sparse_matrix(res)

def main():
    Test1()

main()