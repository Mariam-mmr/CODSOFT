#Password Generator
#This program is a useful tool that generates strong and random passwords for users.
#The program uses a combination of random characters of specified length.
#It allows users to specify the length and complexity of the password.


#Importing necessary modules "random" & "string"
#The module "random" provides tools for generating random numbers and selecting random items
import random
#The module "string" contains a collection of string constants such as lowercase letters, uppercase letters, digits, and punctuation
import string


#Defining a function "gen_pass" which takes two parameters "len" & "comp" Entered by user
#The parameter "len" is an integer specifying the length of the password
#The parameter "comp" is a string specifying the complexity level of the password
def gen_pass(len, comp):
    #Now we use a conditional statements to determine which set of characters to use based on complexity level
    #The first level is "low" to use only lowercase letters
    if comp == "low":
        chrs =  string.ascii_lowercase
    #The second level is "medium" to use both lowercase and uppercase letters
    elif comp == "medium":
        chrs = string.ascii_letters
    #The third level is "high" to use lowercase letters, uppercase letters, digits, and punctuation
    elif comp == "high":
        chrs = string.ascii_letters + string.digits + string.punctuation
    #If the input string is not valid in the choices it would be default to lowercase letters
    else:
        chrs =  string.ascii_lowercase
    #We return the method that generates the password according to the level and using the imported modules
    return ''.join(random.choice(chrs) for _ in range(len))
    #The statement "return" returns the generated password
    #The statement " ''.join(***) " joins the selected characters into a single string
    #The statement "random.choice(chrs)" randomely select a character from the chosen level set
    #The statement "for _ in range(len)" making a loop to repeat the selection process "len" times
    

#Defining the main function that will run the full program
def main():
    #Displaying leading messages for the user to identify the program
    print("Welcome to the password generator program!")
    print("Follow the instructions to start: ")

    #making "while" loop to repeat the program until user stop it
    while True:
        #for "try" block if everything runs without error, the code continues to execute normally.
        try:
            #Prompt the user to enter the desired length of the password "pslen"
            pslen = int(input("Enter the desired length of the password").strip())
            #check if the entered value is equal to or less than zero
            if pslen <= 0:
                print("Length must be a positive integer.")
                #The "continue" is used to skip the remaining code inside the loop and start the next iteration.
                continue   #Prompt the user to choose an operation again
    
            #Prompt the user to enter the desired complexity level of the password "comp"
            comp = input("Enter the desired complexity level (low, medium, high): ").strip().lower()
            #The " .strip() " removes any leading or trailing whitespase from the input
            #The " .lower() " converts the input to lowercase to handel case-insensitive input to be valid
            if comp not in {"low", "medium", "high"}:
                print("Invalid complexity level. Please choose 'low', 'medium', or 'high'.")
                #The "continue" is used to skip the remaining code inside the loop and start the next iteration.
                continue   #Prompt the user to choose an operation again

            #Calling the generating function "gen_pass" with its parameters and stores it in "password" variable
            password = gen_pass(pslen, comp)
            #Printing the generated password to the user, using an f-string for formatting
            print(f"Generated password is: {password}")

            #Ask if the user wants to generate another password
            #We used "strip()" which removes any leading and trailing whitespace from the user's input
            #We used "lower()" to convert the entire input to lowercase. This ensures that the comparison is case-insensitive
            again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
            #checking if the result is anything except "yes"
            if again != 'yes':
                #Printing a confirmation message and exit the program
                print("Exiting the calculator. Have a nice day!")
                break #Exits the while loop and end the program

        #This block of code "except ValueError" handles the situation where an error occurs in the "try" block.
        except ValueError:
            print("Invalid input! Please enter a numeric value for the password length.")
            


#Now we need to call our "main()" function, wich contains the logic to work
#Directly call the main function to interact with the user and perform algorithms
main()


#Codsoft-03
#Done---Mariam M. Rabi