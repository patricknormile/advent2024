import sys
from pathlib import Path
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data
from day06.puzzle_1 import PuzzleGrid, grid_data, find_start, find_direction

class Puzzle2Grid(PuzzleGrid):
    def __init__(self, data):
        super().__init__(data)
        self.original_grid = self.grid

    def add_obsruction(self, i, j):
        self.grid[i][j] = "#"
        self.obstruction = i,j
    def remove_obsruction(self):
        self.grid = grid_data(self.data)
        self.current = find_start(self.grid)
        self.direction = find_direction(self.grid, *self.current)
        self.n_rows = len(self.grid)
        self.n_cols = len(self.grid[0])

        self.obstruction = None
        self.candidate = None
    
    def solve_obstruction(self, i, j):
        self.add_obsruction(i, j)
        candidate_is_obstruction_count = 0
        print(f"trying {i}, {j}")
        status = True
        i = 0
        while status:
            new_status = self.move()
            if (self.candidate == self.obstruction):
                candidate_is_obstruction_count += 1
            # if candidate_is_obstruction_count >= 2:
            #     return True
            #### OH BOY THIS IS BAD
            status = new_status
            i += 1
            if i > 100000:
                return True
        return False

    def solve2(self):
        obstruction_count = 0
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.grid[i][j] == ".":
                    if self.solve_obstruction(i, j):
                        obstruction_count += 1
                self.remove_obsruction()
        self.obstruction_count = obstruction_count
        return self.obstruction_count

def main():
    data = get_days_data(2024, 6)
    grid = Puzzle2Grid(data)
    grid.solve2()
    print(grid.obstruction_count)

if __name__ == "__main__":
    main()