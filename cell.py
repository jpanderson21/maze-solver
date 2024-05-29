from graphics import *


class Cell:
    def __init__(self, x1, x2, y1, y2, window=None, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self._window = window
        self.visited = False

    def draw(self):
        if not self._window:
            return

        left_line = Line(Point(self.x1, self.y1,), Point(self.x1, self.y2))
        left_color = "black" if self.has_left_wall else "white"
        self._window.draw_line(left_line, left_color)

        right_line = Line(Point(self.x2, self.y1,), Point(self.x2, self.y2))
        right_color = "black" if self.has_right_wall else "white"
        self._window.draw_line(right_line, right_color)

        top_line = Line(Point(self.x1, self.y1,), Point(self.x2, self.y1))
        top_color = "black" if self.has_top_wall else "white"
        self._window.draw_line(top_line, top_color)

        bottom_line = Line(Point(self.x1, self.y2,), Point(self.x2, self.y2))
        bottom_color = "black" if self.has_bottom_wall else "white"
        self._window.draw_line(bottom_line, bottom_color)

    def draw_move(self, to_cell, undo=False):
        if not self._window:
            return

        start_point = Point((self.x1 + self.x2) / 2.0, (self.y1 + self.y2) / 2.0)
        end_point = Point((to_cell.x1 + to_cell.x2) / 2.0, (to_cell.y1 + to_cell.y2) / 2.0)
        line = Line(start_point, end_point)
        color = "gray" if undo else "red"
        self._window.draw_line(line, color)
