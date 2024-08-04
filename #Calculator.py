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
    if y == 0:
        return "Error! Division by zero."
    else:
        return x/y


#Main function to execute the calculator
def main():
    print("\nThis program is to get 2 numbers ad perform operations on them")
    #Prompt the user to input the two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    #Printing leading instructions to guide the user
    print('\nChoose the operation you want to perform: ')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    
    #Prompt the user to enter the choice
    choice = input("Enter choice number (1,2,3,4): ")

    #Perform the calculation based on user's choice
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
        return
    
    #Display the calculation result
    print(f'The result of the {operation} of {num1} and {num2} is: {result}')

#The script now defined all the functions but willl not execute the calculator program
#Now we need to call our "main()" function, wich contains the logic to work
#Directly call the main function to interact with the user and perform calculations
main()


#Codsoft-02
#Done---Mariam M. Rabi