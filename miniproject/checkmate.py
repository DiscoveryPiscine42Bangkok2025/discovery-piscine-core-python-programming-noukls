
rows, cols = map(int, input().split())
# หา king
def find_king(A) :
    target = "k"
    for i in range(rows) :
        for j in range(cols) :
            if A[i][j] == target :
                print('King : ',i,j)
                return(i,j)
#หาpawn
def find_pawn(A):
    pawns = []
    for i in range(rows):
        for j in range(cols):
            if A[i][j] == "p":
               print('Pawn : ',i,j) 
               pawns.append((i,j))
    return (i, j)
#หา queen                
def find_queen(A):
    queens = []
    for i in range(rows):
        for j in range(cols):
            if A[i][j] == "q" :
                print('Queen : ',i,j)
                queens.append((i,j))
    return (i,j)
#หา rook
def find_rook(A):
    rooks = []
    for i in range(rows):
        for j in range(cols):
            if A[i][j] == "r":
                print('Rook : ',i,j) 
                rooks.append((i,j))
                return (i,j)
#หา bishop
def find_bishop(A):
    bishops = []
    for i in range(rows):
        for j in range(cols):
            if A[i][j] == "b":
               print('Bishop : ',i,j) 
               bishops.append((i,j))
    return (i,j)
    
#pawn กิน
def pawn_moves(A, pos):
    pawn_move = []
    i, j = pos
    directions = [(-1,1),(-1,-1)]
    for di,dj in directions :
        ni, nj = i+di, j+dj
        if 0 <= ni < rows and 0 <= nj < cols:
            if A[ni][nj] == "k":
                print(A[ni][nj])
                print('succes')
                pawn_move.append((ni, nj))
                
            else :
                print('fail')      
    return (i,j)

#rook กิน
def rook_moves(A, pos):
    rook_move = []
    i, j = pos

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    for di, dj in directions:
        ni, nj = i+di, j+dj
        while 0 <= ni < rows and 0 <= nj < cols:
            if A[ni][nj] == "k":
                print(A[ni][nj])
                print('succes')
                rook_move.append((ni,nj))
            else:
                print('fail')
                rook_move.append((ni,nj))
                break
            ni += di
            nj += dj

    return (i,j)
#bishop กิน
def bishop_moves(A, pos):
    bishop_move = []
    i, j = pos

    directions = [(-1,-1),(-1,1),(1,-1),(1,1)]

    for di, dj in directions:
        ni, nj = i+di, j+dj
        while 0 <= ni < rows and 0 <= nj < cols:
            if A[ni][nj] == "k":
                print('success')
                print(A[ni][nj])
                bishop_move.append((ni,nj))
            else:
                bishop_move.append((ni,nj))
                break
            ni += di
            nj += dj

    return (i,j)
#queen  กิน
def queen_moves(A, pos):
    return rook_moves(A, pos) + bishop_moves(A, pos)

