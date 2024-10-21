def sudoku(P):
    for row, col in [(r, c) for r in range(9) for c in range(9) if not P[r][c]]:

        rr, cc = (row // 3) * 3, (col // 3) * 3

        use = {1, 2, 3, 4, 5, 6, 7, 8, 9} - (
                    {P[row][c] for c in range(9)} | {P[r][col] for r in range(9)} | {P[rr + r][cc + c] for r in range(3)
                                                                                     for c in range(3)})

        if len(use) == 1:
            P[row][col] = use.pop()
            return sudoku(P)
    return P

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(sudoku(puzzle))