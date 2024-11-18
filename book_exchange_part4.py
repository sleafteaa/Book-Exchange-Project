#Juliana Stefanec
#Book Exchange Project
#Exiting the application

def display_options():
    while True:
        print("1: Register New Account")
        print("2: Login to Account")
        print("3: Exit")
        choice = input("Choose an option from (1-3)")
        if choice > 3 or choice < 1 or choice is not int:
            print("Please enter a correct choice")
        elif choice == 1:
            #call user register function
        elif choice == 2:
            #call user login function
        else:
            print("Exiting Application...")
            break
        
        
        
def main_menu():
    while True:
        print("Welcome to the Book Exchange Platform")
        print("1: Add a Book")
        print("2: Show Book Library")
        print("3: Exchange Book")
        print("4: Provide Feedback")
        print("5: Exit")
        choice = input("Choose an option from (1-7)")
        if choice > 5 or choice < 1 or choice is not int:
            print("Please enter a correct choice")
        elif choice == 1:
            #call add book function
        elif choice == 2:
            #call show library function
        elif choice == 3:
            #call complete exchange function
        elif choice == 4:
            #call feedback function
        elif choice == 5:
            print("Exiting Application...")
            break