#T0-D0 List
#A to-do list application is a useful project that helps user to manage and organize their tasks effeciently,
#allowing users to create, update, and track their to-do lists.


tasks = [] #initializing an empty list

#Now we define a function to add a task, and call it later in our code
#This function takes a task as input and check if this task is already existed or not
def addt(task):
    if task in tasks:
        print(f'Task "{task}" already exists.')
    else:
        #Adds a new task to the list if it does not already exist.
        tasks.append(task)
        #print a confirmation message
        print(f'Task "{task}" added successfully.')

    
#Now we define a function to update a task, and call it later in our code  
#This function takes the index of the old task, and the updated data of it, then print a confirmation message
def updt(index, new_task):
    #checking if the index is valaid (in the main list's range)
    if 0 <= index < len(tasks):
        tasks[index] = new_task
        print(f'Task {index + 1} updated to "{new_task}" successfully.')
    else:
        print('Error! Invalid task number.')


#Now we define a function to delete a task, and call it later in our code
#This function takes the index of the task to delete it, then print a confirmation message
def delt(index):
    #checking if the index is valaid (in the main list's range)
    if 0 <= index < len(tasks):
        delt_task = tasks.pop(index)
        print(f'Task "{delt_task}" deleted successfully')
    else:
        print('Error! Invalid task number.')


#Now we define a function to display the list of all tasks and call it later in our code
def disp():
    if tasks:  #checking if there are any tasks in the list or not
        #making a loop along all the tasks in the list
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')
    else:
        print("The tasks list is empty.")

        
#Now we write our main loop of the code and call previous functions in it
#Our main function is an infinite loop that keeps the application running
#But no run-time error would happen, as all possible choices have been provided
print("\nWelcome, this is a To-Do List application, Please choose from the following to start Controlling the list")
while True:
    print("\nOptions: add, update, delete, display, exit")
    #Now prompting the user to write an option and converting it to the lowercase
    option = input("Write an option: ").lower()

    #Now listing all choosing probabilities and its following operations
    
    #for the first choice
    if option == 'add':
        #prompt the user to enter the task
        task = input("Enter the task: ")
        #calling the adding function "addt" with the user's input
        addt(task)
    
    #for the second choice
    elif option == 'update':
        #prompt the user to enter the task number
        index = int(input("Enter the task number to update: ")) - 1
        #Note: in the previous line we converted the inputed text into a numerical value using "int()"
        #Note: we decremented the Entered value, as the indices counting in Python starts from zero
        new_task = input("Enter the new task: ")
        #calling the updating function "updt" with the user's inputs
        updt(index, new_task)
    
    #for the third choice
    elif option == 'delete':
        #prompt the user to enter the task number
        index = int(input("Enter the task number to delete: ")) - 1
        #Note: in the previous line we converted the inputed text into a numerical value using "int()"
        #Note: we decremented the Entered value, as the indices counting in Python starts from zero
        #calling the deleting function "delt" with the user's inputed index
        delt(index)
    
    #for the fourth choice
    elif option == 'display':
        #calling the displaying function "disp"
        disp()
    
    #for the fifth choice
    elif option == 'exit':
        #Exit confirmation
        confirm = input("Are you sure you want to exit? (yes/no): ").lower()
        if confirm == 'yes':
        #Here we break out of the loop, and ending the program
            break
    
    #for any non-listed choice
    else:  
        print('Error! Invalaid option, please try again.')


#Codsoft-01
#Done---Mariam M. Rabi