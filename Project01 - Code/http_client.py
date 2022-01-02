'''
Create a simple python program, http_client.py, that uses a socket to interact with a
server. Note that your program MUST USE THE PYTHON SOCKET API. Yes, it is
possible to do this in one line of code with Python Requests or some other library. But
that wouldn’t be any fun, would it?

Your program shall make a socket connection to the host: “gaia.cs.umass.edu” and send
the GET request for the URI: “/wireshark-labs/INTRO-wireshark-file1.html”. To do this, you will
send the following HTTP-compliant GET request to the server exactly as shown:

"GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n”
'''

# MUST USE THE PYTHON SOCKET API
import socket   # for sockets
import sys      # for error handling


# Program should make socket connection to the host: “gaia.cs.umass.edu”
host = 'gaia.cs.umass.edu'
port = 80       # default port for web services

# catching socket handling errors
# source: https://www.binarytides.com/python-socket-programming-tutorial/
try:
	#create an AF_INET, STREAM socket (TCP)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
	print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
	sys.exit();

# getting IP of host name
try:
    remote_ip = socket.gethostbyname(host)

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

print('IP address of {} is {}'.format(host, remote_ip))

s.connect((remote_ip, port))            # connecting to remote server
print('Socket connected to {} on IP: {}\n\n'.format(host, remote_ip))

# sending data
request = 'GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'

# error handling
try:
    s.send(request.encode())            # encode string to be sent in bytes

except socket.error:
    print('Send failed')
    sys.exit()

print('Message send successfully\n\n')

response = s.recv(4096)                 # receiving data
print(response.decode())                # decode response
s.close()                               # close socket