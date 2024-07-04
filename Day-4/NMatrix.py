
import random
import numpy

def create_matrix(m, n):
    elements = []
    for i in range(m * n):
        elements.append(random.random())
    return elements

def create_zeromatrix(m, n):
    return [0 for i in range(m * n)]

def multiply_matrices(m1, m2, R1, C1, R2, C2):
    if C1 != R2:
        print("Cannot multiply the matrices. Invalid dimensions.")
        return None
    
    result = create_zeromatrix(R1, C2)
    for i in range(R1):
        for j in range(C2):
            for k in range(C1):
                result[C2 * i + j] += m1[C1 * i + k] * m2[C2 * k + j]

    return result

c = create_matrix(2, 2)
d = create_matrix(2, 2)
r1=r2=c1=c2=2
#print("Matrix c:", c)
#print("Matrix d:", d)

new_list = multiply_matrices(c, d,r1,c1,r2,c2)
#print("Resultant Matrix:", new_list)

cn = numpy.array(c).reshape(r1, c1)
dn = numpy.array(d).reshape(r2, c2)

resn = numpy.matmul(cn, dn).flatten()
print(resn)

print(numpy.allclose(resn, new_list))