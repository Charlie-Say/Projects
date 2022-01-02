#!/usr/bin/env python3
'''
Client
1. The client creates a socket and connects to ‘localhost’ and port xxxx
2. When connected, the client prompts for a message to send
3. If the message is /q, the client quits
4. Otherwise, the client sends the message
5. The client calls recv to receive data
6. The client prints the data
7. Back to step 2
8. Sockets are closed (can use with in python3)

https://docs.python.org/3.4/howto/sockets.html
https://www.binarytides.com/python-socket-programming-tutorial/
'''


import socket
import os


# The client creates a socket and connects to ‘localhost’ and port xxxx
host = socket.gethostname()  # 'localhost'
port = 1337  # Socket port xxxx

# 1. Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Source: https://realpython.com/python-sockets/
client.connect((host, port))  # Connect to the server

print('Enter message to send')
print('Type /q to quit')
print('You can start to play Hangman by entering: play')

def startGame():
    os.system('python hangmanclient.py')    # Open file to start Hangman

while True:
    # 2. When connected, the client prompts for a message to send
    message = input("> ")

    # 3. If the message is /q, the client quits
    if message == '/q':
        client.send(message.encode())       # Send message to server that client is quitting
        print("The client has chose to end the chat. Letting the server know.")
        break

    elif message == 'play':
        client.send(message.encode())
        startGame()
        break

    # 4. Client sends the message
    client.send(message.encode())

    # 5. The client calls recv to receive data
    recv_data = client.recv(4096).decode()

    if recv_data == '/q':       # If server quits, then the client will quit too
        print("The server has chose to end the chat.")
        break

    # 6. The client prints the data
    print("SERVER says: " + recv_data)

    ##### 7. Go back to step 2 #####

# Sockets are closed
client.close()
