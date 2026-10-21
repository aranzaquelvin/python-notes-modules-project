import secrets
import time
import os

# Function para linisin yung terminal gamit ang os module
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def play_game():
    clear_screen()
    print("===================================")
    print("       WELCOME TO MATH QUIZ        ")
    print("===================================")
    time.sleep(1)
    
    # LMS Module 7 (List Basics): Pag-save ng history ng laro
    history_questions = []
    history_user_answers = []
    history_correct_answers = []
    
    score = 0
    lives = 3 

    # LMS Module 5 (While Loop): Magpapatuloy habang may buhay pa
    while lives > 0:
        clear_screen()
        print("Lives remaining: " + str(lives))
        print("Current Score: " + str(score))
        print("-----------------------------------")
        
        # secrets module: Pumipili ng random operator
        operators = ['+', '-', '*']
        op = secrets.choice(operators)
        
        # Logic para sa numbers: Mas maliit kung multiplication
        if op == '*':
            num1 = secrets.randbelow(11) + 2  # Pumipili ng number from 2 to 12
            num2 = secrets.randbelow(11) + 2
        else:
            num1 = secrets.randbelow(41) + 10 # Pumipili ng number from 10 to 50
            num2 = secrets.randbelow(41) + 10
        
        # LMS Module 2 (Operators & If/Else): Logic para sa tamang sagot
        if op == '+':
            correct_answer = num1 + num2
        elif op == '-':
            correct_answer = num1 - num2
        elif op == '*':
            correct_answer = num1 * num2
            
        print("Question: What is " + str(num1) + " " + op + " " + str(num2) + "?")
        
        # time module: Sinisimulan yung timer
        start_time = time.perf_counter()
        
        # LMS Module 2: Try-except para iwas crash kung hindi number ang tinype
        try:
            while True:
                user_input = input("Your answer: ")
                if user_input.lstrip('-').isdigit():
                    user_answer = int(user_input)
                    break
                else:
                    print("Invalid input! Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            time.sleep(2)
            lives -= 1
            continue 
        
        # time module: Kinukuha yung oras na ginugol
        end_time = time.perf_counter()
        time_taken = round(end_time - start_time, 2)
        
        # LMS Module 7: Sine-save yung nangyari sa laro sa listahan
        history_questions.append(str(num1) + " " + op + " " + str(num2))
        history_user_answers.append(user_answer)
        history_correct_answers.append(correct_answer)

        # LMS Module 2 (If/Else): Check kung tama o mali
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
    
    # LMS Module 7 (List Basics): For loop para i-print yung history
    print("\n--- GAME REVIEW ---")
    for i in range(len(history_questions)):
        print("Q" + str(i+1) + ": " + history_questions[i] + " | Your Answer: " + str(history_user_answers[i]) + " | Correct: " + str(history_correct_answers[i]))
        
    print("===================================")
    
    # LMS Module 5 (While Loop): Replay logic
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes' or play_again == 'y':
        play_game() 
    else:
        print("Game ended.")
        time.sleep(1)

if __name__ == "__main__":
    play_game()
