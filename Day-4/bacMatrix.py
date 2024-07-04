import random
import numpy as np

def create_matrixA(m, k):
    matrixA = []
    for i in range(m):
        for j in range(k):
            matrixA.append(random.random())
    return matrixA

def create_matrixB(k, n):
    matrixB = []
    for i in range(k):
        for j in range(n):
            matrixB.append(random.random())
    return matrixB

def create_zeromatrix(m, n):
    return [0 for i in range(m * n)]

def multiply_matrices(matrixA, matrixB, m, k, n):
    matrixC = create_zeromatrix(m, n)
    
    for i in range(m):
        for j in range(n):
            for l in range(k):
                matrixC[n * i + j] += matrixA[k * i + l] * matrixB[n * l + j]
    
    return matrixC

def batch_rows(matrix, num_cols, batch_size):
    batched_rows = []
    num_elements = len(matrix)
    num_batches = num_elements // (num_cols * batch_size)
    
    for i in range(num_batches):
        start_index = i * num_cols * batch_size
        end_index = start_index + num_cols * batch_size
        batched_rows.append(matrix[start_index:end_index])
    
    return batched_rows

m = 20
n = 30
k = 11
batch_size = 5

matrixA = create_matrixA(m, k)
matrixB = create_matrixB(k, n)

print("Matrix A flattened into single-row list:")
print(matrixA)

print(matrixB)

matrixC = multiply_matrices(matrixA, matrixB, m, k, n)

print(matrixC)

batched_rows = batch_rows(matrixC, n, batch_size)

for i, batch in enumerate(batched_rows):
    print(f"Batch {i + 1}:")
    print(batch)

cn = np.array(matrixA).reshape(m, k)
dn = np.array(matrixB).reshape(k, n)
resn = np.matmul(cn, dn).flatten()
print(np.allclose(resn, matrixC))
