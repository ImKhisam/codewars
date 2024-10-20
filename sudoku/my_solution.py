def sudoku_check(puzzle, x, y, n):
    for i in range(9):
        if puzzle[x][i] == n:
            return False
    for j in range(9):
        if puzzle[j][y] == n:
            return False
    for i in range(3):
        for j in range(3):
            if puzzle[i + x - x % 3][j + y - y % 3] == n:
                return False
    return True

def sudoku(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for n in range(1, 10):
                    if sudoku_check(puzzle, i, j, n):
                        puzzle[i][j] = n
                        if sudoku(puzzle):
                            return puzzle
                        puzzle[i][j] = 0
                return
    return puzzle

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(sudoku_solver(puzzle))