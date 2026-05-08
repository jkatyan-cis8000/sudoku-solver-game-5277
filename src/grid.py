class SudokuGrid:
    def __init__(self, grid=None):
        if grid is None:
            self.grid = [[0 for _ in range(9)] for _ in range(9)]
        else:
            self.grid = [row[:] for row in grid]

    def is_valid_row(self, row):
        seen = set()
        for cell in self.grid[row]:
            if cell != 0:
                if cell in seen:
                    return False
                seen.add(cell)
        return True

    def is_valid_col(self, col):
        seen = set()
        for row in range(9):
            cell = self.grid[row][col]
            if cell != 0:
                if cell in seen:
                    return False
                seen.add(cell)
        return True

    def is_valid_subgrid(self, row_start, col_start):
        seen = set()
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                cell = self.grid[row][col]
                if cell != 0:
                    if cell in seen:
                        return False
                    seen.add(cell)
        return True

    def is_valid(self):
        for i in range(9):
            if not self.is_valid_row(i):
                return False
            if not self.is_valid_col(i):
                return False
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not self.is_valid_subgrid(row, col):
                    return False
        return True

    def is_complete(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return False
        return self.is_valid()

    def get_cell(self, row, col):
        return self.grid[row][col]

    def set_cell(self, row, col, value):
        self.grid[row][col] = value

    def clear_cell(self, row, col):
        self.grid[row][col] = 0
