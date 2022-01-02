#!/usr/bin/env python3
'''
Server
1. The server creates a socket and binds to ‘localhost’ and port xxxx
2. The server then listens for a connection
3. When connected, the server calls recv to receive data
4. The server prints the data, then prompts for a reply
5. If the reply is /q, the server quits
6. Otherwise, the server sends the reply
7. Back to step 3
8. Sockets are closed (can use with in python3)

https://docs.python.org/3.4/howto/sockets.html
https://www.binarytides.com/python-socket-programming-tutorial/
'''


import socket
import os


# The server creates a socket and binds to ‘localhost’ and port xxxx
host = socket.gethostname()     # 'localhost'
port = 1337     # Socket port xxxx

# 1. Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Source: https://realpython.com/python-sockets/

server.bind((host, port))   # Socket needs to be made a server socket
                            # Source: https://pythontic.com/modules/socket/bind#:~:text=The%20bind()%20method%20of,explicitly%20to%20a%20server%20socket

# 2. The server then listens for a connection
server.listen()
server_connection, address = server.accept()        # Server needs to accept new connection from client on socket

print("Connected by " + str(address))
print('Waiting for message .....')
print('Type /q to quit')

def startGame():
    os.system('python hangmanserver.py')    # Open file to start Hangman

while True:
    # 3. When connected, the server calls recv to receive data
    recv_data = server_connection.recv(4096).decode()

    if recv_data == '/q':       # If client quits, then the server will quit too
        print("The client has chose to end the chat.")
        break

    elif recv_data == "play":
        print("Client has wished to play Hangman!")
        print("STARTING GAME \n")
        startGame()
        break

    # 4. The server prints the data, then prompts for a reply
    print("CLIENT says: " + recv_data)
    send_data = input('> ')

    # 5. If the reply is /q, the server quits
    if send_data == '/q':
        server_connection.send(send_data.encode())      # Send data to client that server is quitting
        print("The server has chose to end the chat. Letting the client know.")
        break

    # 6. Otherwise, the server sends the reply
    server_connection.send(send_data.encode())

    ##### 7. Go back to step 3 #####

# Sockets are closed
server_connection.close()
