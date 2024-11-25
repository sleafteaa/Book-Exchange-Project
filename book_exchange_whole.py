#Entire Book Exchange Program
#Juliana Stefanec
#Prashodhan Bhattrai
#Souleymane Diarra

import json 
import tkinter as tk
from tkinter import messagebox
from logging import root

import pickle

def save_books(book_list):
    with open("books.pickle", "wb") as file:
        pickle.dump(book_list, file)

def load_books():
    try:
        with open("books.pickle", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def add_book(book_list):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    book = {"title": title, "author": author, "year": year}
    book_list.append(book)
    save_books(book_list)
    print(f"Book '{title}' added!")

def list_books(book_list):
    if not book_list:
        print("No books in the library.")
    else:
        for book in book_list:
            print(f"{book['title']} by {book['author']} ({book['year']})")

def search_books(book_list):
    query = input("Enter search term (title or author): ").lower()
    results = [book for book in book_list if query in book["title"].lower() or query in book["author"].lower()]
    if results:
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']})")
    else:
        print("No matching books found.")

def main():
    book_list = load_books()

    while True:
        print("\nOptions: 1) Add Book  2) List Books  3) Search Books  4) Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_book(book_list)

        elif choice == "2":
            list_books(book_list)

        elif choice == "3":
            search_books(book_list)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

# In-memory feedback data storage
feedback_list = []  # Stores feedback data

# Save feedback to a JSON file
def save_feedback():
    with open("feedback.json", "w") as file:
        json.dump(feedback_list, file, indent=4)

# Load feedback from a JSON file
def load_feedback():
    global feedback_list
    try:
        with open("feedback.json", "r") as file:
            feedback_list = json.load(file)
    except FileNotFoundError:
        feedback_list = []

# Display feedback screen for providing feedback
def open_feedback_screen(current_user):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Provide Feedback").pack(pady=10)
    tk.Label(root, text="Rate your exchange (1 to 5):").pack()
    rating_entry = tk.Entry(root)
    rating_entry.pack(pady=5)
    tk.Label(root, text="Leave your feedback:").pack()
    feedback_entry = tk.Entry(root, width=50)
    feedback_entry.pack(pady=5)

    def submit_feedback():
        try:
            rating = int(rating_entry.get())
            if 1 <= rating <= 5:
                feedback = feedback_entry.get()
                feedback_list.append({"rating": rating, "feedback": feedback})
                save_feedback()
                messagebox.showinfo("Success", "Feedback submitted successfully")
                open_main_application(current_user)
            else:
                messagebox.showerror("Error", "Rating must be between 1 and 5")
        except ValueError:
            messagebox.showerror("Error", "Invalid rating. Please enter a number between 1 and 5.")

    tk.Button(root, text="Submit Feedback", command=submit_feedback).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: open_main_application(current_user)).pack(pady=10)

# Display feedback summary
def open_feedback_summary(current_user):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Feedback Summary").pack(pady=10)

    if feedback_list:
        for feedback in feedback_list:
            tk.Label(root, text=f"Rating: {feedback['rating']}, Feedback: {feedback['feedback']}").pack(pady=2)
    else:
        tk.Label(root, text="No feedback available yet.").pack()

    tk.Button(root, text="Back", command=lambda: open_main_application(current_user)).pack(pady=10)


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
            open_feedback_screen(current_user)
        elif choice == 6:
            open_feedback_summary(current_user)
        elif choice == 7:
            print("Exiting Application...")
            break