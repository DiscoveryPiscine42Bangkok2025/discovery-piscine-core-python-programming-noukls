import numpy as np
x = int(input())
A = np.zeros(x)
B = np.full((x),2)
for i in range(x) :
    A[i] = input()
print(A)
print(set(A + B))