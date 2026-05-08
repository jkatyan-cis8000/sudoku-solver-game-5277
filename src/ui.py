from .game import SudokuGame


class SudokuUI:
    def __init__(self, difficulty='medium'):
        self.game = SudokuGame(difficulty)
        self.difficulty = difficulty

    def display_grid(self):
        grid = self.game.get_puzzle_grid().grid
        print("\n  0 1 2   3 4 5   6 7 8")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("  -------+-------+-------")
            row_str = f"{i} "
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    row_str += "| "
                cell = grid[i][j]
                row_str += str(cell) if cell != 0 else "."
                row_str += " "
            print(row_str)
        print()

    def parse_input(self, input_str):
        parts = input_str.strip().split()
        if len(parts) != 3:
            return None
        try:
            row, col, value = map(int, parts)
            if 0 <= row <= 8 and 0 <= col <= 8 and 1 <= value <= 9:
                return row, col, value
        except ValueError:
            pass
        return None

    def handle_command(self, cmd):
        cmd = cmd.strip().lower()
        if cmd == 'quit':
            return 'quit'
        if cmd == 'undo':
            if self.game.undo_move():
                print("Move undone.\n")
            else:
                print("No moves to undo.\n")
            return 'continue'
        if cmd == 'show':
            self.display_grid()
            return 'continue'
        parsed = self.parse_input(cmd)
        if parsed:
            row, col, value = parsed
            if self.game.make_move(row, col, value):
                print("Move accepted.\n")
            else:
                print("Invalid move.\n")
            return 'continue'
        return 'invalid'

    def run(self):
        print("Sudoku Game - Commands: 'row col value' to play, 'undo' to undo, 'show' to redisplay, 'quit' to exit")
        self.display_grid()

        while True:
            cmd = input("Enter your move (row col value): ")
            result = self.handle_command(cmd)
            if result == 'quit':
                print("Thanks for playing!")
                break
            elif result == 'continue':
                self.display_grid()
                if self.game.check_win():
                    print("Congratulations! You solved the puzzle!")
                    break
            elif result == 'invalid':
                print("Invalid input. Use 'row col value' format or command.")
