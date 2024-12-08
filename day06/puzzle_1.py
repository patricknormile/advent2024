import sys
from pathlib import Path
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data

def grid_data(data):
    return [list(x) for x in data.split("\n") if x]

def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in ["^", "v", "<", ">"]:
                return i, j

def count_x(grid):
    count = sum([x.count("X") for x in grid])
    return count

def find_direction(grid, i, j):
    if grid[i][j] == "^":
        return "^"
    if grid[i][j] == "v":
        return "v"
    if grid[i][j] == "<":
        return "<"
    if grid[i][j] == ">":
        return ">"

def turn(direction):
    if direction == "^":
        return ">"
    if direction == ">":
        return "v"
    if direction == "v":
        return "<"
    if direction == "<":
        return "^"
class PuzzleGrid:
    def __init__(self, data):
        self.data = data
        self.grid = grid_data(self.data)
        self.current = find_start(self.grid)
        self.direction = find_direction(self.grid, *self.current)
        self.n_rows = len(self.grid)
        self.n_cols = len(self.grid[0])


    def move(self):
        i, j = self.current
        if self.direction == "^":
            candidate = (i-1, j)
        if self.direction == "v":
            candidate = (i+1, j)
        if self.direction == ">":
            candidate = (i, j+1)
        if self.direction == "<":
            candidate = (i, j-1)
        self.candidate = candidate
        if (self.candidate[0] < 0 or self.candidate[0] >= self.n_rows):
            self.grid[self.current[0]][self.current[1]] = "X"
            return False
        if self.candidate[1] < 0 or self.candidate[1] >= self.n_cols:
            self.grid[self.current[0]][self.current[1]] = "X"
            return False
        if self.grid[self.candidate[0]][self.candidate[1]] == "#":
            self.direction = turn(self.direction)
        elif self.grid[self.candidate[0]][self.candidate[1]] in [".", "X"] :
            self.grid[self.current[0]][self.current[1]] = "X"
            self.current = self.candidate
        return True

    def solve(self):
        while self.move():
            pass
        self.count = count_x(self.grid)
        return self
    def __str__(self):
        return "\n".join(["".join(x) for x in self.grid])

def main():
    data = get_days_data(2024, 6)
    grid = PuzzleGrid(data)
    grid.solve()
    print(str(grid))
    print(grid.count)

if __name__ == "__main__":
    main()