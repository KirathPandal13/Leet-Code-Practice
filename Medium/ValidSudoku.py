"""
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Dictionaries below to  store numbers seen in each column, rows, and 3x3 square
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9): # # Loop through each row and column index (0 to 8)
            for c in range(9):
                if board[r][c] == ".": # Skip through if the cell is empty
                    continue
                
                if ((board[r][c]) in rows[r] or 
                    (board[r][c]) in cols[c] or   # Checks to see if the current number is in the current row, column, or square. If so then it is invalid.
                    (board[r][c]) in squares[(r // 3, c // 3)]):
                    return False
                
                # Add the number to the current row, column, and square sets
                cols[c].add((board[r][c]))
                rows[r].add((board[r][c]))
                squares[(r // 3, c // 3)].add((board[r][c]))
        
        return True # If no duplicates found, the board is valid