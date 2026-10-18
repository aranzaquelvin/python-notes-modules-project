# Math Quiz Game - Python Modules Project

## Description
This is a simple terminal-based Math Quiz game. It tests the user's basic arithmetic skills with a time limit and lives system.

## Modules Used:
1. random: Used to generate random numbers and pick a random math operator (+, -, *).
2. time: Used for the timer to calculate how fast the user answers, and for delays (time.sleep).
3. os: Used to clear the terminal screen so the game looks clean after every round.

## How it works
The game uses a while loop (Module 5) so it continues as long as the player has lives. It uses if-else statements (Module 2) to check if the user's answer matches the computed answer. Lists (Module 7) are used to store the game history, which is printed at the end for review.

## How to Run
python main_game.py