from time import sleep
import random

from cell import Cell
from graphics import Point, Window


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                p1 = Point(self._x1 + i * self._cell_size_x, self._y1 + j * self._cell_size_y)
                p2 = Point(p1.x + self._cell_size_x, p1.y + self._cell_size_y)
                column.append(Cell(p1.x, p2.x, p1.y, p2.y, window=self._win))
            self._cells.append(column)
        for col in self._cells:
            for cell in col:
                cell.draw()
                # self._animate()

    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        sleep(0.001)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[0][0].draw()
        self._animate()
        self._cells[-1][-1].has_right_wall = False
        self._cells[-1][-1].draw()
        self._animate()

    def _cell_exists(self, i, j):
        return (i >= 0 and i < len(self._cells)) and (j >= 0 and j < len(self._cells[0]))

    def _connect_adjacent_cells(self, i1, j1, i2, j2):
        if i1 == i2 and j1 == j2 - 1:
            self._cells[i1][j1].has_bottom_wall = False
            self._cells[i2][j2].has_top_wall = False
        elif i1 == i2 and j1 == j2 + 1:
            self._cells[i1][j1].has_top_wall = False
            self._cells[i2][j2].has_bottom_wall = False
        elif i1 == i2 - 1 and j1 == j2:
            self._cells[i1][j1].has_right_wall = False
            self._cells[i2][j2].has_left_wall = False
        elif i1 == i2 + 1 and j1 == j2:
            self._cells[i1][j1].has_left_wall = False
            self._cells[i2][j2].has_right_wall = False
        else:
            raise Exception(f"Cannot connect non-adjacent cells: ({i1}, {j1}) and ({i2}, {j2})")

        self._cells[i1][j1].draw()
        self._cells[i2][j2].draw()
        self._animate()


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            possible_cells = []
            if self._cell_exists(i-1, j) and self._cells[i-1][j].visited == False:
                possible_cells.append((i-1, j))
            if self._cell_exists(i, j-1) and self._cells[i][j-1].visited == False:
                possible_cells.append((i, j-1))
            if self._cell_exists(i+1, j) and self._cells[i+1][j].visited == False:
                possible_cells.append((i+1, j))
            if self._cell_exists(i, j+1) and self._cells[i][j+1].visited == False:
                possible_cells.append((i, j+1))

            if not possible_cells:
                self._cells[i][j].draw()
                self._animate()
                return

            next_cell = possible_cells[random.randrange(len(possible_cells))]
            self._connect_adjacent_cells(i, j, next_cell[0], next_cell[1])
            self._break_walls_r(next_cell[0], next_cell[1])


    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True

        if current == self._cells[-1][-1]:
            return True

        if self._cell_exists(i-1, j) and self._cells[i-1][j].visited == False and not current.has_left_wall:
            current.draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                current.draw_move(self._cells[i-1][j], undo=True)
        if self._cell_exists(i, j-1) and self._cells[i][j-1].visited == False and not current.has_top_wall:
            current.draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                current.draw_move(self._cells[i][j-1], undo=True)
        if self._cell_exists(i+1, j) and self._cells[i+1][j].visited == False and not current.has_right_wall:
            current.draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                current.draw_move(self._cells[i+1][j], undo=True)
        if self._cell_exists(i, j+1) and self._cells[i][j+1].visited == False and not current.has_bottom_wall:
            current.draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                current.draw_move(self._cells[i][j+1], undo=True)

        return False
