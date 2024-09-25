#Directions: Create a Rock, Paper, Scissors game that allows the user to play against the computer. 
#The program should prompt the user to enter their choice, then randomly select a choice for the computer. 
#The program should then determine the winner and print the result. The program should continue to play until the user chooses to exit.
#The program should have the following functions:
#Requiements: Save the functions in a separate file called groupex.py and import them into the main program.


#START main
#PRINT welcome message
#CALL a function to get user input and store the result as a variable (user_choice)
#CALL a function to get computer's choice and store the result as variable (computer_choice)
#PRINT both user and computer choices
#CALL a function to decide the winner between two choises (user_choice and computer_choice)
#PRINT the result of the game
#LOOP until the game is over with the user's choice
#END main

from gamelib import *
print('Hello User!, Let us play rock, paper, scissor shoot.')

def play_game():
    while True:
        user_choice = user_input()
        print(f"The user's choice is: {user_choice}")
        if user_choice == 'exit':
            print("Thanks for playing! Goodbye.")
            break
        
        computer__choice = computer_choice()
        print(f"The computer's choice is: {computer__choice}")
        
        result = winner(user_choice, computer__choice)
        print(result)

# Start the game
play_game()