from checkmate import *

import numpy as np
#rows , cols = map(int,input().split())
print(rows,cols)
A = np.empty((rows,cols) , dtype = object)
i = 0
j = 0
for i in range(rows) :
    for j in range(cols) :
        A[i][j] = str(input())
        
print(A)
#find_king(A)
#find_pawn(A)
#find_queen(A)
#find_bishop(A)
#find_rook(A)
pawn_moves(A,find_pawn(A))
rook_moves(A,find_rook(A))
bishop_moves(A,find_bishop(A))
queen_moves(A,find_queen(A))