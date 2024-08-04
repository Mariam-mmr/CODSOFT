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
    

#Defining the main function that willl run the full program
def main():
    #Displaying a leading message for the user to identify the program
    print("Welcome to the password generator program!")
    print("Follow the instructions to start: ")
    
    #Prompt the user to enter the desired length of the password
    len = int(input("Enter the desired length of the password").script())
    #Prompt the user to enter the desired complexity level of the password
    comp = input("Enter the desired complexity level (low, medium, high): ").script().lower()
    #The " .script() " removes any leading or trailing whitespase from the input
    #The " .lower() " converts the input to lowercase to handel case-insensitive input to be valid

    #Calling the generating function "gen_pass" with its parameters and stores it in "password" variable
    password = gen_pass(len, comp)
    #Printing the generated password to the user, using an f-string for formatting
    print(f"Generated password is: {password}")


#Now we need to call our "main()" function, wich contains the logic to work
#Directly call the main function to interact with the user and perform algorithms
main()


#Codsoft-03
#Done---Mariam M. Rabi