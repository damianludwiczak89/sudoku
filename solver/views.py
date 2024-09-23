from django.shortcuts import render
import numpy as np
from random import randint, shuffle
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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

    def backtrack(self):
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
                    return result
            self.board[index[0]][index[1]] = 0
        return None

    def blank_values(self, difficulty):
        if difficulty == "easy":
            blanks = 2
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
        return self.board


def index(request):
    return render(request, "solver/index.html")

@csrf_exempt
def play(request, difficulty):
    if difficulty == "custom":
        return JsonResponse([[0 for i in range(9)]for j in range(9)], safe=False, status=200) 
    sud = Sudoku(np.array([[0 for i in range(9)]for j in range(9)]))
    sud = sud.generate(difficulty).tolist()
    print(sud)
    return JsonResponse(sud, safe=False, status=200)


@csrf_exempt
def check_answer(request):
    data = json.loads(request.body)
    board = data.get("board")
    check_board = Sudoku(board)
    for (index, _) in np.ndenumerate(board):
        if check_board.validity(index) != True:
            return JsonResponse(False, safe=False, status=200)
    return JsonResponse(True, safe=False, status=200)


@csrf_exempt
def solution(request):
    data = json.loads(request.body)
    board = data.get("board")
    solution = Sudoku(np.array(board))
    result = solution.solve().tolist()
    for (index, _) in np.ndenumerate(board):
        if solution.validity(index) != True:
            return JsonResponse(False, safe=False, status=200)
    for row in result:
        if 0 in row:
            return JsonResponse("no solution", safe=False, status=200)
    return JsonResponse(result, safe=False, status=200)
