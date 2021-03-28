def solve(board):
    possibleMoves = [[[] for i in range(len(board))] for j in range(len(board[0]))]

    checkValid(board, possibleMoves)
    
def checkValid(board, possibleMoves):

    #Set up all possible moves for every slot
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == 0):
                validRow = set(checkRow(board, i))
                possibleMoves[i][j] = list(validRow.intersection(set(checkColumn(board,j)), set(checkSector(board,i,j))))

    #Iterate until all slots with only one placement option are placed
    for i in range(len(board)):
        for j in range(len(board[i])):
            #Search for slots with only one possible move
            if (len(possibleMoves[i][j]) == 1):
                #Update the board
                board[i][j] = possibleMoves[i][j][0]
                #Remove the move in the possible move list from other slots on the same row, column, and sector
                for k in range(len(board[i])):
                    if (board[i][k] != 0 and board[i][k] in possibleMoves[i][j]):
                        possibleMoves[i][j].remove(board[i][k])

                for l in range(len(board[0])):
                    if (board[l][j] != 0 and board[l][j] in possibleMoves[i][j]):
                        possibleMoves[i][j].remove(board[l][j])

    checkValid(board, possibleMoves)

    #Backtracking algorithm

    return

def checkRow(board, row):
    validMove = [1,2,3,4,5,6,7,8,9]
    for i in range(len(board[row])):
        if (board[row][i] != 0 and board[row][i] in validMove):
            validMove.remove(board[row][i])
    return validMove

def checkColumn(board, col):
    validMove = [1,2,3,4,5,6,7,8,9]
    for i in range(len(board[0])):
        if (board[i][col] != 0 and board[i][col] in validMove):
            validMove.remove(board[i][col])
    return validMove

def checkSector(board, row, col):
    validMove = [1,2,3,4,5,6,7,8,9]
    sector_x = col // 3
    sector_y = row // 3

    for i in range(sector_y*3, sector_y*3+3):
        for j in range(sector_x*3, sector_x*3+3):
            if (board[i][j] != 0 and board[i][j] in validMove):
                validMove.remove(board[i][j])

    return validMove

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# board = [
#     [2,9,5,7,0,0,8,6,0],
#     [0,3,1,8,6,5,0,2,0],
#     [8,0,6,0,0,0,0,0,0],
#     [0,0,7,0,5,0,0,0,6],
#     [0,0,0,3,8,7,0,0,0],
#     [5,0,0,0,1,6,7,0,0],
#     [0,0,0,5,0,0,1,0,9],
#     [0,2,0,6,0,0,3,5,0],
#     [0,5,4,0,0,8,6,7,2]
# ]

print(solve(board))