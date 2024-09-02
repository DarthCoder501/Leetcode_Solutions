class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row for duplicates
        for i in range(9):
            s = set()  # Create an empty set to track seen numbers in the current row
            for j in range(9):
                item = board[i][j]  # Get the current cell value
                if item in s:  # If the item is already in the set, it is a duplicate
                    return False
                elif item != '.':  # Only add non-empty cells to the set
                    s.add(item)
        
        # Check each column for duplicates
        for i in range(9):
            s = set()  # Create an empty set to track seen numbers in the current column
            for j in range(9):
                item = board[j][i]  # Get the current cell value in the column
                if item in s:  # If the item is already in the set, it is a duplicate
                    return False
                elif item != '.':  # Only add non-empty cells to the set
                    s.add(item)

        # Check each 3x3 sub-box for duplicates
        for box_i in range(3):
            for box_j in range(3):
                s = set()  # Create an empty set to track seen numbers in the current 3x3 sub-box
                for i in range(3):
                    for j in range(3):
                        item = board[3 * box_i + i][3 * box_j + j]  # Get the value in the current 3x3 sub-box cell
                        if item in s:  # If the item is already in the set, it is a duplicate
                            return False
                        elif item != '.':  # Only add non-empty cells to the set
                            s.add(item)

        # If no duplicates are found, the Sudoku board is valid
        return True
