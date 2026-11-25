import numpy as np

def gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
    :param A: Coefficient matrix
    :param b: Right-hand side vector
    :return: Solution vector x
    """

    for i in range(len(b)):
        if A[i][i] == 0:
            for j in range(len(b)):
                if A[j][i] != 0:
                    for k in range(len(b)):
                        A[i][k] += A[j][k]
                    b[i] += b[j]
                    break

    # for i in range(len(b)):
    #     for j in range(len(b)):
    #         print(A[i][j], end = " ")
    #     print(b[i])

    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            if A[j][i] != 0:
                div = (A[i][i] / A[j][i])
                # print("(", i, ", ", i, ")", "(", i, ", ", j, ")")
                for k in range(len(b)):
                    A[j][k] *= div
                    A[j][k] -= A[i][k]
                b[j] *= div
                b[j] -= b[i]

    x = np.zeros(len(b))
    for i in range(len(b) - 1, -1, -1):
        sum = b[i]
        for j in range(i, len(b)):
            sum = sum - (A[i][j] * x[j])
        x[i] = sum / A[i][i]

    return x
