import random
#Function to get user input
#Request User Input
def user_input():
    while True:
        user_input = input('"Rock, Paper or Scissors" or exit, Please state your choice: ').lower()

#Validate User Input using IN operator and LIST
#Return User Input
        if user_input in ['rock', 'paper', 'scissors', 'exit']:
            return user_input
        else:
            print("Invalid input. Please try again.")


#Function to get computer's choice
#Create a list of choices
#Return a random choice from the list
#To use random choices, import random module, and use random.choice() method
def computer_choice():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    return computer_choice

#Function to determine the winner
#Compare user's choice and computer's choice
#IF both choices are the same
    #Return "It's a tie!"
#ELSE IF user's choice is rock and computer's choice is scissors
    #Return "You win!"
#ELSE IF user's choice is paper and computer's choice is rock
    #Return "You win!"
#ELSE IF user's choice is scissors and computer's choice is paper
    #Return "You win!"
#ELSE IF user's choice is exit
    #Return "exit"
#ELSE
    #Return "Computer wins!"
def winner(user_input, computer_choice):
    if user_input == computer_choice:
        return "It's a tie!"
    elif (user_input == 'rock' and computer_choice == 'scissors') or \
         (user_input == 'scissors' and computer_choice == 'paper') or \
         (user_input == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"