import socket
import sys
from util import readrequest

message_get = '''GET /test.html HTTP/1.0
Accept: text/html
Host: localhost

'''

#Send GET request
try:
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port 9999 on localhost
    server_address = ('localhost', 9999)
    print ('Connecting to localhost on port 9999')
    sock.connect(server_address)

    print ('sending %s' % message_get)
    sock.sendall(message_get)
    # Receive data
    data = readrequest(sock)
    print >> sys.stderr, '%s' % data

except socket.error:
    print ('Unable to connect to localhost on port 9999')

finally:
    # Closing the connection
    sock.close()




