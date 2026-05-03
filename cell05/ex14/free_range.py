import sys
import numpy as np
i = int(sys.argv[1])
x = int(sys.argv[2])
A = np.zeros(x-i+1)
print(A)
if len(sys.argv) != 3 :
    print('none')
else :
    A = np.arange(i,x+1,1)
print(A)