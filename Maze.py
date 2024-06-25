import tkinter as tk
import random

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    #Draws a cell when called
    def draw(self, canvas, color):
        x, y = self.x * TILE, self.y * TILE
        if (color == "red"): #Draws a red box to indicate where the current "pointer" is
            canvas.create_rectangle(x, y, x + TILE, y + TILE, fill='red', outline='red')
        if self.walls['top']:
            canvas.create_line(x, y, x + TILE, y, fill=color, width=2)
        if self.walls['right']:
            canvas.create_line(x + TILE, y, x + TILE, y + TILE, fill=color, width=2)
        if self.walls['bottom']:
            canvas.create_line(x + TILE, y + TILE, x, y + TILE, fill=color, width=2)
        if self.walls['left']:
            canvas.create_line(x, y + TILE, x, y, fill=color, width=2)

    #Checks if cells are out of bounds
    def check_cell(self, x, y, grid_cells):
        index = x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[index]

    #Check if neighbors are valid, if so, randomly select a neighbor
    def check_neighbors(self, grid_cells):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1, grid_cells)
        right = self.check_cell(self.x + 1, self.y, grid_cells)
        bottom = self.check_cell(self.x, self.y + 1, grid_cells)
        left = self.check_cell(self.x - 1, self.y, grid_cells)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return random.choice(neighbors) if neighbors else False

#Remove a wall from the current node and the neighbor node
def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False

#Initialzes the maze
def generate_maze(canvas):
    grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
    current_cell = grid_cells[0]
    stack = []

    #Keeps track of how many walls we've "broken".
    #If this equals the matrix's total length (n,n)
    #then we've traversed through the entire maze.
    break_count = 1

    #Recursivley call a "step" until maze generation is complete.
    def step():
        nonlocal current_cell, break_count
        current_cell.visited = True
        next_cell = current_cell.check_neighbors(grid_cells)
        if next_cell:
            next_cell.visited = True
            break_count += 1
            stack.append(current_cell)
            remove_walls(current_cell, next_cell)
            current_cell = next_cell
        elif stack:
            current_cell = stack.pop()

        canvas.delete("all")
        for cell in grid_cells:
            cell.draw(canvas, 'black') #Makes all boxes outlines with black
        current_cell.draw(canvas, 'red')  #Highlight the current cell with red

        if break_count != len(grid_cells):
            canvas.after(10, step)

    step()

#-----FUNCTIONAL CODE-----
root = tk.Tk()
root.title("Maze")

TILE = 30
GRID_WIDTH, GRID_HEIGHT = 20, 30
WIDTH, HEIGHT = TILE * GRID_WIDTH, TILE * GRID_HEIGHT
cols, rows = GRID_WIDTH, GRID_HEIGHT
background_color = 'white'

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=background_color)
canvas.pack()

generate_maze(canvas)

root.mainloop()


#TODO:
# Add a GUI before maze generation with:
# Custom Background Color
# Custom Size
# Custom Speed Generation