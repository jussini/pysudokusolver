#!/usr/bin/env python

import unittest
from sudokuboard import SudokuBoard
#from sudosolver import try_solve
import sudosolver

class TestBoard(unittest.TestCase):

    very_small_board = [[1,2,3],[4,5,6],[7,8,9]];

    invalid_board1 = [1,2]

    full_standard_board = [[1,2,3,4,5,6,7,8,9],
                           [4,5,6,7,8,9,1,2,3],
                           [7,8,9,1,2,3,4,5,6],
                           [2,3,4,5,6,7,8,9,1],
                           [5,6,7,8,9,1,2,3,4],
                           [8,9,1,2,3,4,5,6,7],
                           [3,4,5,6,7,8,9,1,2],
                           [6,7,8,9,1,2,3,4,5],
                           [9,1,2,3,4,5,6,7,8]]

    almost_full_standard_board = [[1,2,3,4,5,6,7,8,9],
                           [4,5,6,7,8,9,1,2,3],
                           [7,8,9,1,2,3,4,5,6],
                           [2,3,4,5,0,7,8,9,1],
                           [5,6,7,8,9,1,2,3,4],
                           [8,9,1,2,3,4,5,6,7],
                           [3,4,5,6,7,8,9,1,2],
                           [6,7,8,9,1,2,3,4,5],
                           [9,1,2,3,4,5,6,7,8]]

    part_standard_board = [
                           [1,2,3,4,5,6,7,8,0],
                           [4,5,6,7,8,9,1,0,3],
                           [7,0,9,1,2,3,0,5,6],
                           [2,3,4,5,0,7,8,9,1],
                           [5,0,7,8,9,1,2,3,4],
                           [8,9,1,0,3,4,5,6,7],
                           [0,0,5,6,7,8,0,1,2],
                           [6,7,8,9,1,2,3,0,5],
                           [9,1,2,3,4,5,6,7,0]
                          ]

    part_standard_board2 = [[0,0,3,4,5,6,7,8,0],
                            [0,0,0,7,8,9,1,0,3],
                            [0,0,0,1,2,3,0,5,0],
                            [2,3,4,5,0,7,8,9,1],
                            [5,0,7,8,9,1,2,3,4],
                            [8,9,0,0,3,4,5,6,7],
                            [0,0,5,6,7,8,0,1,2],
                            [6,7,8,9,1,2,3,0,5],
                            [9,1,2,3,4,5,6,7,0]]

    hard_board = [[0,2,0,0,0,0,0,0,0],
                  [0,0,5,0,0,0,0,7,0],
                  [7,0,9,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,6,0,0,0,0,0,0],
                  [0,0,0,0,0,7,0,8,3],
                  [0,0,0,0,0,0,0,0,0],
                  [4,0,0,5,0,0,0,0,0],
                  [0,0,0,0,0,4,0,3,0]]

    e = lambda x: x % 2 == 0
    o = lambda x: x % 2 == 1

    hard_constraints = [[e,e,e,e,o,o,o,o,o],
                        [o,e,o,o,e,o,e,o,e],
                        [o,o,o,e,o,e,o,e,e],
                        [e,e,o,e,e,o,o,o,o],
                        [o,o,e,o,o,e,o,e,e],
                        [e,o,o,o,e,o,e,e,o],
                        [o,o,o,o,o,e,e,e,e],
                        [e,e,e,o,o,o,e,o,o],
                        [o,o,e,e,e,e,o,o,o]]


    webboard1 = [[0,0,0,3,0,0,4,7,0],
                 [5,0,0,4,0,0,2,9,0],
                 [0,8,6,0,0,0,0,0,0],
                 [0,3,8,0,9,4,0,2,7],
                 [0,4,2,7,0,5,6,8,0],
                 [7,6,0,8,1,0,9,3,0],
                 [0,0,0,0,0,0,8,5,0],
                 [0,5,1,0,0,8,0,0,3],
                 [0,2,7,0,0,3,0,0,0]]


    def test_inits_empty(self):
        b = SudokuBoard()
        assert(len(b.rows) == 0)

    def test_set_rows(self):
        b = SudokuBoard()
        b.set_rows(self.very_small_board)
        assert(len(b.rows) == 3)

    @unittest.expectedFailure
    def test_set_invalid_size(self):
        b = SudokuBoard()
        b.set_rows(self.invalid_board1)

    def test_get_row(self):
        b = SudokuBoard()
        b.set_rows(self.very_small_board)
        r = b.get_row(1)
        assert(r == [4,5,6])

    def test_get_col(self):
        b = SudokuBoard()
        b.set_rows(self.very_small_board)
        col = b.get_column(0)
        assert(col == [1,4,7])

    def test_get_col2(self):
        b = SudokuBoard()
        b.set_rows(self.very_small_board)
        col = b.get_column(1)
        assert(col == [2,5,8])

    def test_group1(self):
        b = SudokuBoard()
        b.set_rows(self.full_standard_board)
        g = b.get_group(0,0)
        assert(g == [1,2,3,4,5,6,7,8,9])

    def test_group2(self):
        b = SudokuBoard()
        b.set_rows(self.full_standard_board)
        g = b.get_group(8,0)
        assert(g == [3,4,5,6,7,8,9,1,2])

    def test_group3(self):
        b = SudokuBoard()
        b.set_rows(self.full_standard_board)
        g = b.get_group(5,4)
        assert(g == [5,6,7,8,9,1,2,3,4])

    def test_partial_group1(self):
        b = SudokuBoard()
        b.set_rows(self.part_standard_board)
        g = b.get_group(0,6)
        assert(g == [7,8,1,3,5,6])

    def test_at(self):
        b = SudokuBoard();
        b.set_rows(self.full_standard_board)
        a = b.at(4,2)
        assert(a == 7)

    def test_available_on_column(self):
        b = SudokuBoard()
        b.set_rows(self.part_standard_board)
        a = b.available_on_column(1)
        assert(a == frozenset([8,4,6]))

    def test_available_on_row(self):
        b = SudokuBoard()
        b.set_rows(self.part_standard_board)
        a = b.available_on_row(6)
        assert(a == frozenset([9,3,4]))

    def test_available_on_group(self):
        b = SudokuBoard()
        b.set_rows(self.part_standard_board)
        a = b.available_on_group(0,0)
        assert(a == frozenset([8]))

    def test_available_on_group2(self):
        b = SudokuBoard()
        b.set_rows(self.part_standard_board)
        a = b.available_on_group(7,7)
        assert(a == frozenset([4,8, 9]))

    def test_available_at_full(self):
        b = SudokuBoard()
        b.set_rows(self.full_standard_board)
        a = b.available_on_group(7,7)
        assert(a == frozenset([]))

    def test_available_at_partial1(self):
        b = SudokuBoard()
        b.set_rows(self.part_standard_board)
        a = b.available_at(7,7)
        print "a1", a
        assert(a == [4])

    def test_available_at_partial2(self):
        b = SudokuBoard()
        b.set_rows(self.part_standard_board2)
        a = b.available_at(2,2)
        print "a2", a
        assert(a == [9,6])


    def test_next_empty_onfull(self):
        b = SudokuBoard()
        b.set_rows(self.full_standard_board)
        n = b.next_empty_index();
        assert(n == None)

    def test_next_empty(self):
        b = SudokuBoard()
        b.set_rows(self.part_standard_board)
        n = b.next_empty_index();
        assert(n == (0,8))

    def test_next_empty2(self):
        b = SudokuBoard()
        b.set_rows(self.part_standard_board2)
        n = b.next_empty_index();
        assert(n == (0,0))

    def test_solve_full(self):
        b = SudokuBoard()
        b.set_rows(self.full_standard_board)
        s = sudosolver.SudokuSolver()
        s.solve(b)
        assert(len(s.solutions) == 1)


    def test_solve_almost_full(self):
        b = SudokuBoard()
        b.set_rows(self.almost_full_standard_board)
        s = sudosolver.SudokuSolver()
        s.solve(b)
        assert(len(s.solutions) == 1)


    def test_solve_partial(self):
        b = SudokuBoard()
        b.set_rows(self.part_standard_board)
        s = sudosolver.SudokuSolver()
        s.solve(b)
        assert(len(s.solutions) == 1)


    def test_solve_partial2(self):
        b = SudokuBoard()
        b.set_rows(self.part_standard_board2)
        s = sudosolver.SudokuSolver()
        s.solve(b)
        assert(len(s.solutions) == 1)

    def test_web1(self):
        b = SudokuBoard()
        b.set_rows(self.webboard1)
        s = sudosolver.SudokuSolver()
        s.solve(b)
        assert(len(s.solutions) == 1)

    @unittest.skip("long runtime")
    def test_solve_hard(self):
        b = SudokuBoard()
        b.set_rows(self.hard_board)
        b.set_constraints(self.hard_constraints)
        s = sudosolver.SudokuSolver()
        s.solve(b)
        assert(length(s.solutions) == 1)

if __name__ == '__main__':
    unittest.main()
