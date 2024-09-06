board = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0, 0, 0, 0, 0, 0,-1, 0, 0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0],
    ]


def maks_score(board):
    max_row = 0
    max_col = 0
    for i in range(len(board)):
        max_row += 1
    for a in range(len(board[0])):
        max_col += 1
    n_cells = max_col*max_row
    return(n_cells)

print("Tester no_duplicates... ", end="")
a = 0
assert(a == maks_score(board))
print("OK")