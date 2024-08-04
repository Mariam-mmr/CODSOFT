#Calculator
#This program is a simple calculator with basic arithmetic operations.
#It perform the calculation for two numbers and display the result

#Function Definitions for Basic Arithmetic Operations
#The first operation...Adding two numbers
def add(x,y):
    return x+y
#The second operation...Subtracting two numbers
def sub(x,y):
    return x-y
#The third operation...Multiplying two numbers
def mul(x,y):
    return x*y
#The fourth operation...Dividing two numbers
def div(x,y):
    #Handling the case of division by zero
    if y == 0:
        return "Error! Division by zero."
    #If y != 0, then the division is defined
    else:
        return x/y


#The main function to execute the calculator
def main():
    #making "while" loop to repeat the program until user stop it
    while True:
        print("\nThis program performs basic arithmetic operations on two numbers.")
        #for "try" block if everything runs without error, the code continues to execute normally.
        #the try block is attempting to convert the user’s input into floating-point numbers using float().
        #This is necessary because input() returns data as a string, and you need to convert it to a numerical type for arithmetic operations.
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        #This block of code "except ValueError" handles the situation where an error occurs in the "try" block.
        #it catches a ValueError, which occurs if the conversion to "float", (case of non-numeric values).
        except ValueError:
            #When this error is caught, the program prints an error message indicating that the input was invalid.
            print("Invalid input! Please enter numeric values.")
            continue  # Prompt the user to enter the numbers again

        #Printing leading instructions to guide the user
        print('\nChoose the operation you want to perform: ')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
    
        #Prompt the user to enter the choice
        choice = input("Enter choice number (1,2,3,4): ")

        #Perform the calculation based on user's choice and calling suitable functions
        if choice == '1':
            result = add(num1,num2)
            operation = "Addition"
        elif choice == '2':
            result = sub(num1,num2)
            operation = "Subtraction"
        elif choice == '3':
            result = mul(num1,num2)
            operation = "Multiplication"
        elif choice == '4':
            result = div(num1,num2)
            operation = "Division"
        else:
            print('invalid choice, please choose again.')
            #The "continue" is used to skip the remaining code inside the loop and start the next iteration.
            continue  #Prompt the user to choose an operation again
    
        #Display the calculation result
        print(f'The result of the {operation} of {num1} and {num2} is: {result}')

        #Ask if the user wants to perform another calculation
        #We used "strip()" which removes any leading and trailing whitespace from the user's input
        #We used "lower()" to convert the entire input to lowercase. This ensures that the comparison is case-insensitive
        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        #checking if the result is anything except "yes"
        if again != 'yes':
            #Printing a confirmation message and exit the program
            print("Exiting the calculator. Have a nice day!")
            break #Exits the while loop and end the program

#The script now defined all the functions but will not execute the calculator program
#Now we need to call our "main()" function, wich contains the logic to work
#Directly call the main function to interact with the user and perform calculations
main()


#Codsoft-02
#Done---Mariam M. Rabi