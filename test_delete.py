import socket
import sys
from util import readrequest

message_delete = '''DELETE /test.html HTTP/1.1
Accept: text/html
Host: localhost
Connection: close

'''

#Send DELETE request
try:
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port 9999 on localhost
    server_address = ('localhost', 9999)
    print ('Connecting to localhost on port 9999')
    sock.connect(server_address)

    print ('sending %s' % message_delete)
    sock.sendall(message_delete)
    # Receive data
    data = readrequest(sock)
    print >> sys.stderr, '%s' % data

except socket.error:
    print ('Unable to connect to localhost on port 9999')

finally:
    # Closing the connection
    sock.close()
