import numpy as np
x = int(input())
A = np.zeros(x)
B = np.full((1,x),2)
for i in range(x) :
    A[i] = input()
print(A)
print(A+B)