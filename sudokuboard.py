#!/usr/bin/env python


class SudokuBoard:

    EMPTY = 0
    ALL = frozenset(range(1,10))


    def __init__(self):
        self.rows = []

    def set_rows(self, rows):
        assert(len(rows) % 3 == 0)
        self.rows = rows
        self.constraints = None

    def set_constraints(self, constraints):
        self.constraints = constraints

    def get_constraint(self, rownum, colnum):
        if self.constraints is not None:
            return self.constraints[rownum][colnum]
        else:
            return lambda x: True

    def get_row(self, rownum):
        return self.rows[rownum]

    def get_column(self, colnum):
        col = [row[colnum] for row in self.rows]
        return col

    def at(self, row, column):
        return self.rows[row][column]

    def get_group(self, row, column):
        row_group = row / 3
        col_group = column / 3
        col_indice = [i for i in range(len(self.rows)) if i / 3 == col_group]
        row_indice = [i for i in range(len(self.rows[0])) if i / 3 == row_group]

        group = [self.at(r,c) for r in row_indice for c in col_indice]
        return [i for i in group if i != self.EMPTY]

    def available_on_column(self, colnum):
        col = self.get_column(colnum);
        available = self.ALL - frozenset(col)
        return available

    def available_on_row(self, rownum):
        row = self.get_row(rownum);
        available = self.ALL - frozenset(row)
        return available

    def available_on_group(self, rownum, colnum):
        group = self.get_group(rownum,colnum);
        available = self.ALL - frozenset(group)
        return available


    def available_at(self, rownum, colnum):
        on_row = self.available_on_row(rownum)
        on_col = self.available_on_column(colnum)
        on_group = self.available_on_group(rownum, colnum)

        constraint = self.get_constraint(rownum, colnum)
        values = on_row & on_col & on_group
        return [v for v in values if constraint(v)]


    def next_empty_index(self):
        # todo, better
        for i in range(len(self.rows)):
            for j in range(len(self.rows[0])):
                if self.at(i, j) == self.EMPTY:
                    return (i,j)
        return None
