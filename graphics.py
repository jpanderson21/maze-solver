from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self._root_widget = Tk()
        self._root_widget.title("Maze Solver")
        self._root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas_widget = Canvas(self._root_widget, bg="white", width=width, height=height)
        self._canvas_widget.pack(expand=1, fill="both")
        self._running = False

    def redraw(self):
        self._root_widget.update_idletasks()
        self._root_widget.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def close(self):
        self._running = False

    def draw_line(self, line, color):
        line.draw(self._canvas_widget, color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=color, width=2)


class Cell:
    def __init__(self, x1, x2, y1, y2, window, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._window = window

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1,), Point(self._x1, self._y2))
            self._window.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1,), Point(self._x2, self._y2))
            self._window.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1,), Point(self._x2, self._y1))
            self._window.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y2,), Point(self._x2, self._y2))
            self._window.draw_line(line, "black")
