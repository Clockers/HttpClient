import socket
import sys
from util import readrequest

message_put1 = '''PUT /dir/test1.html HTTP/1.1
Host: localhost
Content-Type: text/html
Content-Length: 11

test data 1
'''

message_put2 = '''PUT /dir/test2.html HTTP/1.1
Host: localhost
Content-Length: 11

test data 2
'''

message_put3 = '''PUT /test.html HTTP/1.1
Connection: close
Host: localhost
Content-Length: 9

test data
'''

#Send 3 PUT request for intialize the server
try:
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    # Connect the socket to the port 9999 on localhost
    server_address = ('localhost', 9999)
    print ('Connecting to localhost on port 9999')
    sock.connect(server_address)

    print ('sending %s' % message_put1)
    sock.sendall(message_put1)
    # Receive data
    data = readrequest(sock)
    print >> sys.stderr, '%s' % data

    print ('sending %s' % message_put2)
    sock.sendall(message_put2)
    # Receive data
    data = readrequest(sock)
    print >> sys.stderr, '%s' % data

    print ('sending %s' % message_put3)
    sock.sendall(message_put3)
    # Receive data
    data = readrequest(sock)
    print >> sys.stderr, '%s' % data

except socket.error:
    print ('Unable to connect to localhost on port 9999')
finally:
    # Closing the connection
    sock.close()
