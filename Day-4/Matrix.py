import random
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def create_matrix(m, n):
    rows = []
    for i in range(m):
        col = []
        for j in range(n):
            col.append(random.random())

        rows.append(col)

    return rows

#print(create_matrix(4, 5))

def multiply_matrices(m1, m2):
    R1 = len(m1)
    C1 = len(m1[0])
    R2 = len(m2)
    C2 = len(m2[0])

    if C1 != R2:
        print("Cannot multiply the matrices. Invalid dimensions.")
        return None

    result = []
    for i in range(R1):
        result.append([0] * C2)

    for i in range(R1):
        for j in range(C2):
            for k in range(R2):
                result[i][j] += m1[i][k] * m2[k][j]

    return result


#print(c)
#print(d)
#print(multiply_matrices(c,d))

n_values = []
#execution_times = []
flops_persec=[]

for i in range(2,500,50):
    c=create_matrix(i,i)
    d=create_matrix(i,i)
    n_operations= 2*i**3

    start_time=time.time()
    multiply_matrices(c,d)
    end_time=time.time()
    execution_time=end_time-start_time
    flops=n_operations/execution_time

    n_values.append(i)
    flops_persec.append(flops)
    #execution_times.append(execution_time)
n_values = np.array(n_values)
flops_per_second = np.array(flops_persec)
plt.plot(n_values, flops_persec, marker='o')
#execution_times = np.array(execution_times)
#plt.plot(n_values, execution_times, marker='o')
plt.show()



    