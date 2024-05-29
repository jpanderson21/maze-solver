from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(20, 20, 14, 19, 40, 40, win, 0)
    print(f"Mazed solved? {maze.solve()}")
    win.wait_for_close()

main()
