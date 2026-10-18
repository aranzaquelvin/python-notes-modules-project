import random
import time
import os

# Function para linisin yung terminal gamit ang os module
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_valid_answer():
    """Kumuha ng valid integer input mula sa user."""
    while True:
        user_input = input("Your answer: ").strip()
        # Accept lang ang valid integer (isang '-' lang at digits)
        if user_input.lstrip('-').isdigit() and user_input.count('-') <= 1:
            return int(user_input)
        else:
            print("Invalid input! Please enter a valid number.")

def play_game():
    clear_screen()
    print("===================================")
    print("       WELCOME TO MATH QUIZ        ")
    print("===================================")
    time.sleep(1)
    
    history_questions = []
    history_user_answers = []
    history_correct_answers = []
    
    score = 0
    lives = 3 

    while lives > 0:
        clear_screen()
        print("Lives remaining: " + str(lives))
        print("Current Score: " + str(score))
        print("-----------------------------------")
        
        operators = ['+', '-', '*']
        op = random.choice(operators)
        
        if op == '*':
            num1 = random.randint(2, 12)
            num2 = random.randint(2, 12)
        else:
            num1 = random.randint(10, 50)
            num2 = random.randint(10, 50)
        
        if op == '+':
            correct_answer = num1 + num2
        elif op == '-':
            correct_answer = num1 - num2
        elif op == '*':
            correct_answer = num1 * num2
            
        print("Question: What is " + str(num1) + " " + op + " " + str(num2) + "?")
        
        start_time = time.perf_counter()
        
        user_answer = get_valid_answer()
        
        end_time = time.perf_counter()
        time_taken = round(end_time - start_time, 2)
        
        history_questions.append(str(num1) + " " + op + " " + str(num2))
        history_user_answers.append(user_answer)
        history_correct_answers.append(correct_answer)

        if user_answer == correct_answer:
            print("Correct. You took " + str(time_taken) + " seconds.")
            score += 10
            time.sleep(1.5)
        else:
            print("Wrong. The correct answer is " + str(correct_answer) + ".")
            lives -= 1
            time.sleep(2)
            
    clear_screen()
    print("===================================")
    print("             GAME OVER             ")
    print("===================================")
    print("Final Score: " + str(score))
    
    print("\n--- GAME REVIEW ---")
    for i in range(len(history_questions)):
        print("Q" + str(i+1) + ": " + history_questions[i] + " | Your Answer: " + str(history_user_answers[i]) + " | Correct: " + str(history_correct_answers[i]))
        
    print("===================================")

# Main loop — instead of recursion
if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes' or play_again == 'y':
            continue
        else:
            print("Game ended.")
            time.sleep(1)
            break