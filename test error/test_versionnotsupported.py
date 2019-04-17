import socket
import sys
from util import readrequest

message_versionnotsupported = '''GET /test.html HTTP/1.5
Accept: text/html
Host: localhost 

'''

#Send error requests
try:
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port 9999 on localhost
    server_address = ('localhost', 9999)
    print ('Connecting to localhost on port 9999')
    sock.connect(server_address)

    print ('sending %s' % message_versionnotsupported)
    sock.sendall(message_versionnotsupported)
    # Receive data
    data = readrequest(sock)
    print >> sys.stderr, '%s' % data

except socket.error:
    print ('Unable to connect to localhost on port 9999')

finally:
    # Closing the connection
    sock.close()