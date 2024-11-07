#Juliana Stefanec
#Notification Functionality
"""
import socket
import threading
def start_chat_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(5)
    while True:
        client, addr = server.accept()
        threading.Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
    while True:
        message = client.recv(1024).decode('utf-8')
        if not message:
            break
# Send message to recipient or update chat UI

def start_chat_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    while True:
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
"""        
import graphics

def request_notify():
    if choose_book is True:
        """
        choose_book can be a condition met in part 2
        to represent a book request
        """ 
        return "Someone is interested in your book!"
    else:
        return None
    
def decision_notify():
    if decision is True:
        """
        decision can be a variable asked to the donor
        if they would like to confirm or deny a request,
        we'd need to decide which part of the code this would be part of
        """
        return book_donor + "has accepted your request!"
    else:
        return book_donor + "has denied your request."
    #book_donor is the unique username of the book donor
