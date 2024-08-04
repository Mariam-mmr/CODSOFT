#Rock-Paper-Scissors Game
#This program prompts the user to choose rock, paper, or scissors and generate arandom choice for the computer
#It determine the winner based on user's and computer's choices and show the result
#The program keeps track of user's and computer's scores for multiple rounds
#It has been designed to be user-friendly interface with clear instructions and feedback 


#Importing the 'random' module, which provides functions to generate random values
#We'll use 'random' to make the computer's choice
import random

#Defining a function prompts the user to input their choice of the provided list 'choices'
def user_choice():
    choices = ["rock", "paper", "scissors"]
    #Ensuring the input is valaid by converting it to lowercase and checking if it's in the list and guide the user
    user_ch = input("\nwrite your choice [rock, paper, scissors]: ").lower()
    #If the user enters an invalid choice, it asks them to try again until they provide a valid input
    while user_ch not in choices:
        print("\ninvalid choice, please try again.")
        user_ch = input("\nwrite your choice [rock, paper, scissors]: ").lower()
    return user_ch

#Defining a function to generate a random choice for the computer in each round from the list
def comp_choice():
    return random.choice(["rock", "paper", "scissors"])

#Defining a function to determine the result of each round of the game
def game_result(user_ch, comp_ch):
    if user_ch == comp_ch:
        return "tie"
    elif (user_ch == "rock" and comp_ch == "scissors") or \
         (user_ch == "scissors" and comp_ch == "paper") or \
         (user_ch == "paper" and comp_ch == "rock"):
        return "user"
    else:
        return "computer"

#Defining a function to display the result of the round (win, lose, tie)
#The variable winner would be defined in the main function assigned to the function "game_result" 
def disp(user_ch, comp_ch, winner):
    print(f"\nyou chose: {user_ch}")
    print(f"\ncomputer chose: {comp_ch}")
    if winner == "tie":
        print("it's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

#Defining the main function, which willl be the entry point of the program including the previous functions
def main():
    #Initializing score counters for both user and computer
    comp_s = 0
    user_s = 0

    #Giving greating message giving a quick overview of the program
    print("\nHello! this is Rock-Paper-Scissors Game")
    print("Follow instructions, and enjoy!")
    
    #We make a while loop which runs the game repeatedly until the user stop
    while True:
        #calling the pervious functions to prompt user's choice, make random choice for the computer
        #Then calling the "game_result" function referred to the variable "winner" to make decisions on it
        user_ch = user_choice()
        comp_ch = comp_choice()
        winner = game_result(user_ch, comp_ch)

        #We increment the counter of the user or the computer based on the result of the game
        if winner == "user":
            user_s += 1
        elif winner == "computer":
            comp_s += 1
        
        #Now call "disp" function to display the result of the game (choises and the final result)
        disp(user_ch, comp_ch, winner)

        #Printing leading guide messages to display results
        print(f"\nScores: You --> {user_s}, Computer --> {comp_s}")
        
        #Now the user is asked if they want to play another round with tacking of the score or quit the game
        #If the user's answer is not "yes" the loop breaks and the program ends
        #We used "lower()" to make sure the user's input is valaid
        play = input("\nDo you want to play another round? (yes, no): ").lower()
        if play != "yes":
            break
    
    #When the game ends, these messages are displayed with the final score recorded
    print("\nThank you for playing! Final scores are: ")
    print(f"You: {user_s}, Computer: {comp_s}")

#The script now defined all the functions but willl not execute the Game program
#Now we need to call our "main()" function, wich contains the logic to work
#Directly call the main function to interact with the user and perform algorithms
main()


#Codsoft-04
#Done---Mariam M. Rabi