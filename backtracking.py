# This is a Sudoku Solver
# Here we are going to solve the sudoku based on Backtracking method


# A function to show the sudoku puzzle in good manner
def sudoku_show(arr):
    for i in range(len(arr)):
        line = ""
        if i == 3 or i == 6:
            print("--"*(len(arr[i])+2))
        for j in range(len(arr[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(arr[i][j]) + " "
        print(line)

#Finding the unfilled celss
def findCellToFill(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                return i,j
    return -1,-1

# a function which validate the input sudoku
def validation(arr, i, j, num):
    #Checking the row
    row_check = all([num != arr[i][y] for y in range(9)])
    if row_check:
        # Checking the column
        col_check = all([num != arr[x][j] for x in range(9)])
        if col_check:
            # Checking number in boxes
            x_box_start, y_box_start = 3*(i//3), 3*(j//3)
            for x in range(x_box_start, x_box_start+3):
                for y in range(y_box_start, y_box_start+3):
                    if arr[x][y] == num:
                        return False
            return True
    return False


# A function to solve the sudoku
def solve_sudoku(arr, i=0, j=0):
    i, j = findCellToFill(arr)
    if i == -1:
        # it show that the puzzle sovled completely
        return arr

    for num in range(1,10):
        if validation(arr, i, j, num):
            arr[i][j] = num
            if solve_sudoku(arr, i, j):
                return arr
            # A violation happen
            arr[i][j]=0
    return False


if __name__ == "__main__":
    #Sample test
    puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]
    sudoku_show(puzzle)
    print()
    result = solve_sudoku(puzzle)
    if not result:
        print("There is no solution")
    else:
        sudoku_show(result)
