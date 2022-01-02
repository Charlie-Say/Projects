'''
Your program will create a listening socket bound to ‘127.0.0.1’ or ‘localhost’, and a random port
number > 1023. You will then use your web browser to connect to your server and
receive data.
When your socket accepts a request, a new socket is created. Read the socket request
on the new socket and print it. Then send the following html data on the new socket and
close it.

        data = "HTTP/1.1 200 OK\r\n"\
            "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
            "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

Run your program (http_server.py). Start up your web browser and navigate to
127.0.0.1:xxxx (where xxxx is the port you specified in your server). Take screenshots of
your server and your browser.
'''


from socket import *

host = '127.0.0.1'
port = 1337            # random port > 1023

data =  "HTTP/1.1 200 OK\r\n"\
        "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
        "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

# help source: https://realpython.com/python-sockets/
s = socket(AF_INET, SOCK_STREAM)                        # create socket
s.bind((host, port))                                    # associate the socket with specific network interface and port
s.listen()                                              # create a listening socket bound to '127.0.0.1'

while True:
    conn, addr = s.accept()             # client connection, returns a new socket object tuple (host, port)
    recv_data = conn.recv(4096)         # receive data the client sends

    print("Recieved: {}".format(str(recv_data)))        # confirm socket received data
    conn.send(data.encode())                            # echoes data sent by client

    print("Sending>>>>>>>>>>>>")
    print(data)
    print("<<<<<<<<<<<")

    conn.close()
    break
