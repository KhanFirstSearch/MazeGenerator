import tkinter as tk

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top':True, 'left':True, 'right':True, 'bottom':True}

    def draw(self, canvas, tile_size):
        x = self.x * tile_size
        y = self.y * tile_size

        if self.walls['top']:
            canvas.create_line(x, y, x + tile_size, y, fill='white', width=2)
        if self.walls['right']:
            canvas.create_line(x + tile_size, y, x + tile_size, y + tile_size, fill='white', width=2)
        if self.walls['bottom']:
            canvas.create_line(x, y + tile_size, x + tile_size, y + tile_size, fill='white', width=2)
        if self.walls['left']:
            canvas.create_line(x, y, x, y + tile_size, fill='white', width=2)

def fillCells():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            Cell(i, j).draw(canvas, TILE_SIZE)

TILE_SIZE = 30
GRID_SIZE = 10


root = tk.Tk()
root.title("Maze")

canvas = tk.Canvas(root, width=(GRID_SIZE * TILE_SIZE) + 2, height=(GRID_SIZE * TILE_SIZE) + 2)
canvas.pack()


cell = Cell(9, 9)

fillCells()

root.mainloop()