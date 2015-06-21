
#!/usr/bin/env python

from sudokuboard import SudokuBoard
import boardtests
from copy import deepcopy;


class SudokuSolver():
    """docstring for SudokuSolver"""

    def __init__(self):
        self.solutions = []

    def solve(self, board):
        self.try_solve(board)
        print "found ", len(self.solutions), "solutions"
        for solution in self.solutions:
            print_board(solution)


    def try_solve(self, board):
        for_next = board.next_empty_index()
        if (for_next == None):
            self.solutions.append(board)
        else:
            (row,col) = for_next
            available = board.available_at(row,col)
            for a in available:
                b = deepcopy(board)
                b.rows[row][col] = a
                self.try_solve(b)


def print_board(board):
    print ""
    for r in board.rows:
        print r


def main():
    b = SudokuBoard();
    b.set_rows(boardtests.TestBoard.hard_board)
    b.set_constraints(boardtests.TestBoard.hard_constraints)
    solver = SudokuSolver()
    solver.solve(b)





if __name__ == "__main__":
  main()
