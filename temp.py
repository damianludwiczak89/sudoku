import numpy as np
from random import randint, shuffle

class Sudoku():
    def __init__ (self, board=np.array([[0 for i in range(9)]for j in range(9)])):
        # Initialize an empty board of sudoku where 0 means blank cell
        self.board = board

    def __str__(self):
        return f"{self.board}"

    def validity(self, index):

        # Determine what values are in the row, column and 3x3 square of the given index
        row, column = index
        row_values = self.board[row]
        column_values = []
        for i in range(9):
            column_values.append(self.board[i][column])
        row /= 3
        column /= 3
        square_row = 0 if row < 1 else 3 if row < 2 else 6
        square_column = 0 if column < 1 else 3 if column < 2 else 6

        square_values1 = self.board[square_row][square_column:square_column + 3]
        square_values2 = self.board[square_row + 1][square_column:square_column + 3]
        square_values3 = self.board[square_row + 2][square_column:square_column + 3]
        square_values = np.concatenate((square_values1, square_values2, square_values3))

        # Remove 0 values
        row_values = [value for value in row_values if value != 0]
        column_values = [value for value in column_values if value != 0]
        square_values = [value for value in square_values if value != 0]

        # Check if after adding new value there are no duplicates in row, column or 3x3 square
        if len(row_values) == len(set(row_values)) and len(column_values) == len(set(column_values)) and len(square_values) == len(set(square_values)):
            return True
        else:
            return False
        
    def cell_validation(self, index, value):
        # Determine what values are in the row, column and 3x3 square of the given index
        row, column = index
        row_values = self.board[row]
        column_values = []
        for i in range(9):
            column_values.append(self.board[i][column])
        row /= 3
        column /= 3
        square_row = 0 if row < 1 else 3 if row < 2 else 6
        square_column = 0 if column < 1 else 3 if column < 2 else 6

        square_values1 = self.board[square_row][square_column:square_column + 3]
        square_values2 = self.board[square_row + 1][square_column:square_column + 3]
        square_values3 =self.board[square_row + 2][square_column:square_column + 3]
        square_values = [*square_values1, *square_values2, *square_values3]

        # Check if duplicated values exist, ignore 0 values
        row_values = [value for value in row_values if np.count_nonzero(row_values == value) > 1 and value != 0]
        column_values = [value for value in column_values if column_values.count(value) > 1 and value != 0]
        square_values = [value for value in square_values if square_values.count(value) > 1 and value != 0]

        # If the duplicated value, is the same as the value we are checking now, return False as invalid
        return False if value in [*row_values, *column_values, *square_values] else True

    def invalid_cells(self):
        invalids = []
        for (index, value) in np.ndenumerate(self.board):
            if self.cell_validation(index, value) != True:
                invalids.append(index)
        return invalids

    def backtrack(self):
        print(self.board)
        if 0 not in self.board:
            return self.board
        index = np.argwhere(self.board == 0)[0]
        possible = [i + 1 for i in range(9)]
        shuffle(possible)
        for value in possible:
            self.board[index[0]][index[1]] = value
            if self.validity(index):
                result = self.backtrack()
                if result is not None:
                    print(result)
                    return result
            self.board[index[0]][index[1]] = 0
        return None

    def blank_values(self, difficulty):
        if difficulty == "easy":
            blanks = 30
        elif difficulty == "medium":
            blanks = 40
        elif difficulty == "hard":
            blanks = 50
        while np.count_nonzero(self.board == 0) < blanks:
            row = randint(0, 8)
            column = randint(0, 8)
            self.board[row][column] = 0
        return

    def generate(self, difficulty):
        self.backtrack()
        self.blank_values(difficulty)
        return self.board

    def solve(self):
        self.backtrack()
        print(self.board)
        return self.board
    
def validity(index, result, value):

        # Determine what values are in the row, column and 3x3 square of the given index
        row, column = index
        row_values = result[row]
        column_values = []
        for i in range(9):
            column_values.append(result[i][column])
        row /= 3
        column /= 3
        square_row = 0 if row < 1 else 3 if row < 2 else 6
        square_column = 0 if column < 1 else 3 if column < 2 else 6

        square_values1 = result[square_row][square_column:square_column + 3]
        square_values2 = result[square_row + 1][square_column:square_column + 3]
        square_values3 =result[square_row + 2][square_column:square_column + 3]
        square_values = [*square_values1, *square_values2, *square_values3]

        # Check if duplicated values exist, ignore 0 values
        row_values = [value for value in row_values if row_values.count(value) > 1 and value != 0]
        column_values = [value for value in column_values if column_values.count(value) > 1 and value != 0]
        square_values = [value for value in square_values if square_values.count(value) > 1 and value != 0]

        # If the duplicated value, is the same as the value we are checking now, return False as invalid
        return False if value in [*row_values, *column_values, *square_values] else True



result =   [[0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [1, 0, 0, 0, 0, 0, 1, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,]]


solution = Sudoku(np.array(result))
invalids = solution.invalid_cells()
print(invalids)


