import sys
import numpy as np
i = int(sys.argv[1])
x = int(sys.argv[2])
A = np.array(x-i+1)
a = 0
if len(sys.argv) != 3 :
    print('none')
else :
    for i in range(x) :
        A[a] = i
        a = a+1
print(A)