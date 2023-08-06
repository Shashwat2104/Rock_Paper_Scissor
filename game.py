import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors), or 'q' to quit: ").lower()
        if user_choice in ['rock', 'paper', 'scissors', 'q']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def play_game():
    user_wins = 0
    computer_wins = 0
    draws = 0
    
    while True:
        print("------------------------------")
        print("Rock, Paper, Scissors Game")
        print("------------------------------")
        
        user_choice = get_user_choice()
        
        if user_choice == 'q':
            break
        
        computer_choice = get_computer_choice()
        
        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == 'user':
            user_wins += 1
            print("You win!")
        elif winner == 'computer':
            computer_wins += 1
            print("Computer wins!")
        else:
            draws += 1
            print("It's a draw!")
        
        print("------------------------------")
        print("Score:")
        print("You:", user_wins)
        print("Computer:", computer_wins)
        print("Draws:", draws)
        print("------------------------------\n")

    print("Thank you for playing!")

# Start the game
play_game()
