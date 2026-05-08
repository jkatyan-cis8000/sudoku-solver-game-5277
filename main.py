#!/usr/bin/env python3
from src.game import SudokuGame
from src.ui import SudokuUI


def main():
    print("Welcome to Sudoku!")
    print("Select difficulty: easy, medium, hard")
    difficulty = input("Enter difficulty (default: medium): ").strip().lower()
    if difficulty not in ['easy', 'medium', 'hard']:
        difficulty = 'medium'
    
    ui = SudokuUI(difficulty)
    ui.run()


if __name__ == "__main__":
    main()
