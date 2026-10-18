# Math Quiz Game - Python Modules Project

## Description
This is a simple terminal-based Math Quiz game built to test your mental arithmetic under pressure. It features a timer and a "3 strikes" lives system—perfect for simulating the mild panic of a surprise math quiz! If you're good at mental math, you survive. If not, well, at least the code works.

## Modules Used:
1. **`random`**: Used to generate random numbers and pick a random math operator (+, -, *). Because hardcoding 100 math problems is a violation of student rights.
2. **`time`**: Used for the timer to calculate how fast you answer, and for dramatic delays (`time.sleep`). It also gives you a few seconds to reflect on your wrong answers.
3. **`os`**: Used to clear the terminal screen after every round. We clear the screen so you don't have to stare at your previous mistakes (both in the game and in life).

## How it works
The game uses a **while loop (LMS Module 5)** to keep the game running as long as the player has lives left. It uses **if-else statements (LMS Module 2)** to check if your answer is correct. Lastly, **Lists (LMS Module 7)** are used to store the game history, so you can review exactly where you went wrong at the end—like a personalized feedback report from your professor.

## How to Run
Make sure you are in the correct folder, then run:
```bash
python main_game.py
