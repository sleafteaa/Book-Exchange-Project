#Juliana Stefanec
#Book Exchange Project
#Exiting the application

def main_menu(users, books):
    while True:
        print("Welcome to the Book Exchange Platform")
        print("1: Register New Account")
        print("2: Login to Account")
        print("3: Add a Book")
        print("4: Show Book Library")
        print("5: Exchange Book")
        print("6: Provide Feedback")
        print("7: Exit")
        choice = input("Choose an option from (1-7)")
        if choice > 7 or choice < 1 or choice is not int:
            print("Please enter a correct choice")
        elif choice == 7:
            print("Exiting Application...")
            break