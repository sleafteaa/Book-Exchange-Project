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
        print("3: Book Lookup")
        print("4: Exchange Book")
        print("5: Provide Feedback")
        print("6: Show Feedback")
        print("7: Exit")
        choice = input("Choose an option from (1-7)")
        if choice > 7 or choice < 1 or choice is not int:
            print("Please enter a correct choice")
        elif choice == 1:
            add_book(book_list)
        elif choice == 2:
            list_books(book_list)
        elif choice == 3:
            search_books(book_list)
        elif choice == 4:
            #call exchange book function
        elif choice == 5:
            open_feedback_screen(user)
        elif choice == 6:
            open_feedback_summary(user)
        elif choice == 7:
            print("Exiting Application...")
            break
