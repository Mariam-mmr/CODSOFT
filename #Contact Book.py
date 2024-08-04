#Contact Book
#This program stores name, phone number, email, and address for each contact
#It allows user to add new contact, display, update, delete and search the saved contacts list
#It has been designed to be user-friendly with clear instructions and feedback 


#Here we will use classes to organize the code by gouping related data and functions together
#By using classes, the code becomes modular. Each class has a specific responsibility, making the code maintain, and extend
#In Python, "def __init__(self, ...)" is a special method known as the constructor,
#It's automatically invoked when a new instsnce of a class is created


#First we define the 'contact' class with an initializer '__init__' method that sets the 'name','phone','email', and 'address' attributes
#Defining a class "Contact" to represent individual contacts
class Contact:
    #The '__init__' is a special method that uatomatically called when a new instance of the class is created
    #The "self" parameter is a reference to the current instance of the class
    #The "self" parameter is used to access instance variables and methods
    def __init__(self, name, phone, email, address):
        #Now we assign the parameters "name","phone","email",and "address" to instance variables "self.(parameter)" of the "Contact" class
        #These instance variables store the contact's information
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address




#Second class we define is "ContactBook" to manage multiple contacts
class ContactBook:
    #Initializing a constructor method for the "ContactBook" class
    #It creates an empty list "self.contacts" to store the instances of the "Contact" class
    def __init__(self):
        self.contacts = []


    #Defining a method "add" that takes parameters to add a new contact to "contacts" list
    def add(self, name, phone, email, address):
        #Creating a new instance of the "Contact" class with the provided details
        contact = Contact(name, phone, email, address)
        #Appending the newly created contact to the contacts list (addind to the end of the list)
        self.contacts.append(contact)


    #Defining a method "view" that iterates through all contacts in the "contacts" list and prints their details
    def view(self):
        #The iteration loop through all contacts
        for contact in self.contacts:
            #Printing contacts with their main details
            print(f"Name: {contact.name}, Phone: {contact.phone}")


    #Defining a method "srch" that searches for contacts matching the keyword and printing their details
    #"self" is a reference to the current instance of the class, it allows access to the instance's attributes and methods
    #"keyword" The parameter that the method accepts, which willl be used to search for the contacts
    def srch(self, keyword):
        #Now making list comprehension for filtering contacts
        #"result" A list that willl store the contacts that match the search
        results = [contact for contact in self.contacts
                   if keyword.lower() in contact.name.lower() or
                   keyword in contact.phone]
                 #---Breaking down the list comprehension---#
             #"[contact for contact in self.contacts...]" iterates over each "contact" in "self.contacts" list
             #"keyword.lower()" converts the search to lowercase to make the search case-insensitive
             #"contact.name.lower()" converts the contact's name to lowercase for the same reason
             #"keyword.lower() in contact.name.lower()" checks if the lowercase keyword is a substring of the lowercase contact name
             #"keyword in contact.phone" checks if the keyword is a substring of the contact's phone number
             #"if..." The contact is included in the "results" list if either condition (name or phone match) is true
        #Now we iterate through all contacts in the list "result" to print them
        for contact in results:
            #Using ' print(f" ") ' to care about format of the variables included
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")


    #Defining a method "updt" to update specific details of an existed "contact" in our list "self.contacts" 
    #This method depends searching for the contact using the "name" of it
    #"name" is a parameter that represents the name of the contact user wants to update
    #"nname=None, nphone=None,..." are optional parameters, if provided they willl be used to update the corresponding fields...
    #...of the contact. if not provided, the fields willl remain unchanged
    def updt(self, name, nname=None, nphone=None, nemail=None, naddress=None):
        #Now we iterate over the contacts list "self.contacts" through each "contact" 
        for contact in self.contacts:
            #checking if the contact name in user's search matches the name of a contact in list "self.contacts"
            #If the match is found, the method willl update the contact's data
            if contact.name == name:
                #check if new name "nname" is provoded or not "None"
                if nname:
                    #if the new name "nname" is provided, the contact's "name" attribute willl be updated to the new one
                    contact.name = nname
                #check if new phone "nphone" is provoded or not "None"
                if nphone:
                    #if the new phone "nphone" is provided, the contact's "phone" attribute willl be updated to the new one
                    contact.phone = nphone
                #check if new email "nemail" is provoded or not "None"
                if nemail:
                    #if the new email "nemail" is provided, the contact's "email" attribute willl be updated to the new one
                    contact.email = nemail
                #check if new address "naddress" is provoded or not "None"    
                if naddress:
                    #if the new address "naddress" is provided, the contact's "address" attribute willl be updated to the new one
                    contact.address = naddress
                    #Printing a confirmation message to user
                print(f"Contact '{name}' updated successfully.")
                #Once the contact is found and updated, the method exits by returning "return"
                #This steps ensures thst no more contacts are checked or updated
                return
        #Handling the case when the contact is not found in our search giving a leading message to the user    
        print(f"Contact '{name}' not found in the list.")


    #Defining a method to delete "dlt" a contact using its name and remove it from the list
    #The parameter "name" represents the name of the contact that we want to delete
    def dlt(self, name):
        #Now we iterate over our list "self.contacts" to search for "contact"
        for contact in self.contacts:
            #Checking if the searched name "name" is included in our list
            if contact.name == name:
                #if the match is found, then the method willl delete the "contact" from the list "self.contacts"
                #We didn't use the "pop()" as it requires providing index of the element we delete as we need to enumerate it before
                #On the other hand the method "remove()" doesn't require the index
                self.contacts.remove(contact)
                #Printing a confirmation message to user to ensure deleting successfully
                print(f"Contact '{name}' deleted successfully.")
                #Once the contact is found and deleted, the method exits by returning "return"
                #This steps ensures thst no more contacts are checked or deleted
                return
        #Handling the case when the contact is not found in our search giving a leading message to the user    
        print(f"Contact '{name}' not found in the list.")


    #Defining a method to interact with user and apply changes on the list including the previous functions
    def usr_act(self):
        #Here we create an infinite loop, to run until the user stops it by choosing exit
        while True:
            #Displaying guiding messages and options for the user to choose from and interact with the program
            print("\nContact Book Menu")
            print("choose an option to continue")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            #Getting user input and store it in the choice "ch" variable to make decisions later
            #Displaying a message to prompt the user to choose one option
            ch = input("Choose an option number: ")

            #Based on user choice we make decisions
            #for choice 1, check if the user wants to add contact
            if ch == 1:
                #Now collecting the details of the new option
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter phone number: ")
                #Now calling the "add" method to add the new contact to the list
                self.add(name, phone, email, address)
                #Printing a confirmation message of adding successfully
                print(f"Contact '{name}' added successfully.")
            
            #for choice 2, checking if user wants to view the contacts list
            elif ch == 2:
                #Calling the method "view" to display all contacts
                self.view()

            #for choice 3, checking if user wants to search for a contact
            elif ch == 3:
                #Prompt the user to input the searching keyeord, either a name or phone number
                keyword = input("Enter name or phone number to search: ")
                #calling the searching method "srch" to find a keyword match
                self.srch(keyword)

            #for choice 4, checking if user wants to update a contact
            elif ch == 4:
                #getting method's parameters from user to update the contact's data
                #if user wants to keep any data unchanged, they can leave the input blank
                name = input("Enter the name of the contact you want to update: ")
                nname = input("Enter the new name (keep blank to keep current): ")
                nemail = input("Enter the new phone (keep blank to keep current): ")
                nphone = input("Enter the new email (keep blank to keep current): ")
                naddress = input("Enter the new address (keep blank to keep current): ")
                #Calling the method "updt" to update an existed contact
                self.updt(name, nname, nphone, nemail, naddress)

            #for choice 5, checking if user wants to delete a contact
            elif ch == 5:
                #Prompt the user to enter the name of the contact to delete it
                name = input("Enter the name of the contact to delete it: ")
                #Calling the method "dlt" to delete the contact knowing its name
                self.dlt(name)

            #for choice 5, checking if user wants to exit the program
            elif ch == 6:
                #Printing a guiding message for the user
                print("Exiting Contact Book ...")
                #Now exiting the while loop and ending the program
                break

            #for invalid choices, printing a leading message to user
            else:
                print("Error! Invalid choice, Please try again.")


#Defining the main function that willl run the full program
#Note: A class is a blueprint for creating objects (instances). It can contain methods (which like functions defined within the class)...
#...and attributes (variables that belong to the class)
#When we create an instance of a class, we're essentially creating an object that has the structure and behavior defined by the class
def main():
    #An instance of the "contactBook" class is created
    contact_book = ContactBook()
    #The user interface method "usr_act" is called on the "contact_book" instance, to start the menu and user interaction loop
    contact_book.usr_act()


#Now we need to call our "main()" function, wich contains the logic to work
#Directly call the main function to execute the program
main()


#Codsoft-05
#Done---Mariam M. Rabi