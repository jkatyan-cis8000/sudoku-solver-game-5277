import random
from .grid import SudokuGrid


class SudokuGame:
    def __init__(self, difficulty='medium'):
        self.difficulty = difficulty
        self.solution_grid = None
        self.puzzle_grid = None
        self.moves = []
        self._generate_puzzle()

    def _generate_puzzle(self):
        self.solution_grid = self._generate_solution()
        self.puzzle_grid = self._remove_numbers(self.solution_grid)
        self.moves = []

    def _generate_solution(self):
        grid = SudokuGrid()
        self._fill_diagonal(grid)
        self._solve(grid)
        return SudokuGrid(grid.grid)

    def _fill_diagonal(self, grid):
        for i in range(0, 9, 3):
            self._fill_box(grid, i, i)

    def _fill_box(self, grid, row, col):
        nums = list(range(1, 10))
        random.shuffle(nums)
        idx = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                grid.set_cell(r, c, nums[idx])
                idx += 1

    def _solve(self, grid):
        for row in range(9):
            for col in range(9):
                if grid.get_cell(row, col) == 0:
                    for num in range(1, 10):
                        if self._is_safe(grid, row, col, num):
                            grid.set_cell(row, col, num)
                            if self._solve(grid):
                                return True
                            grid.set_cell(row, col, 0)
                    return False
        return True

    def _is_safe(self, grid, row, col, num):
        for c in range(9):
            if grid.get_cell(row, c) == num:
                return False
        for r in range(9):
            if grid.get_cell(r, col) == num:
                return False
        start_row = row - row % 3
        start_col = col - col % 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if grid.get_cell(r, c) == num:
                    return False
        return True

    def _remove_numbers(self, solution, count=40):
        grid = SudokuGrid(solution.grid)
        cells = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(cells)
        for r, c in cells[:count]:
            grid.clear_cell(r, c)
        return grid

    def make_move(self, row, col, value):
        if self.puzzle_grid.get_cell(row, col) != 0:
            return False
        if value == 0:
            return False
        if not self._is_safe(self.puzzle_grid, row, col, value):
            return False
        self.puzzle_grid.set_cell(row, col, value)
        self.moves.append((row, col, value))
        return True

    def undo_move(self):
        if not self.moves:
            return False
        row, col, _ = self.moves.pop()
        self.puzzle_grid.clear_cell(row, col)
        return True

    def check_win(self):
        return self.puzzle_grid.is_complete()

    def get_puzzle_grid(self):
        return SudokuGrid(self.puzzle_grid.grid)

    def get_solution_grid(self):
        return SudokuGrid(self.solution_grid.grid)
