from .ui import SudokuUI


def main():
    print("Welcome to Sudoku!")
    difficulty = input("Choose difficulty (easy/medium/hard) [medium]: ").strip().lower()
    if difficulty not in ['easy', 'medium', 'hard']:
        difficulty = 'medium'
    
    ui = SudokuUI(difficulty)
    ui.run()


if __name__ == '__main__':
    main()
