from gmpy import mpq,mpz
from random import randint,seed
from time import time

def rand_matrix(n, typ=int, N=10):
    ''' A function to matrix with random elements '''

    m = []
    for i in range(n):
        a = []

        for j in range(n):
            p = randint(0, N)
            a.append(p)

        m.append(a)
    return m

def matrixmult (A, B):
    ''' A function to do normal matrix multiplication '''

    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      print "Cannot multiply the two matrices. Incorrect dimensions."
      return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k]*B[k][j]
    return C

def test_1(N):
    seed(2)
    for n in range(100, 1000, 100):
        a = rand_matrix(n, mpq, N)
        b = rand_matrix(n, mpq, N)
        t0 = time()
        C = matrixmult(a, b)
        t1 = time()

        print 'dimension: %d traditional way: %.2f' %(n, t1-t0)

test_1(1000000)
