'''
Your program will make a socket connection to the host: “gaia.cs.umass.edu” and send the
GET request for the URI: “/wireshark-labs/HTTP-wireshark-file3.html”.

To do this, you will send
the following HTTP-compliant GET request to the server exactly as below:
"GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

There is no end-of-transmission (EOT) with sockets, so knowing when you’ve received
all the data can be difficult. Fortunately for this project, the gaia.cs.umass.edu server will
close the connection after sending its data, so the easy thing to do is detect when recv
or read return <= 0 bytes in a loop.
'''


import socket   # for sockets
import sys      # for error handling
import time     # for breaking out of loop


# Program should make socket connection to the host: “gaia.cs.umass.edu”
host = 'gaia.cs.umass.edu'
port = 80       # default port for web services

# catching socket handling errors
# help source: https://www.binarytides.com/python-socket-programming-tutorial/
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
request = 'GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'

# error handling
try:
    s.send(request.encode())            # encode string to be sent in bytes

except socket.error:
    print('Send failed')
    sys.exit()

print('Message send successfully\n\n')


# write function with loop to collect all data from response
# help source: https://www.binarytides.com/receive-full-data-with-the-recv-socket-function-in-python/
def recv_all_data(socket, timeout = 2):
    socket.setblocking(0)       # make socket non-blocking

    total_data = []             # make array to store fragments of data received
    data = ''                   # capture received data in string to append to total_data array

    begin = time.time()         # start time

    while True:
        if total_data and time.time()-begin > timeout:      # if you got some data, then break after timeout
            break

        # receive data and decode into string format
        try:
            data = socket.recv(8192)
            dec_data = data.decode()

            # condition to check variable 'data' has any value remaining
            if data:
                total_data.append(dec_data)                # if condition passes, append decoded data to total_data array

        except:
            pass

    return ''.join(total_data)                              # join elements in total_data array into a single string and return

print('Request: GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1')
print('Host: %s\n\n' %host)

print(recv_all_data(s))         # print output of function recv_all_data
s.close()                       # close socket