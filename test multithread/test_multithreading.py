import socket
import sys
import time
from util import readrequest

message_get1 = '''GET /testmulti.html HTTP/1.1
Accept: text/html
Accept-Language: it
User-Agent: Mozilla/4.0
Host: localhost

'''
message_put1 = '''PUT /testmulti.html HTTP/1.1
Content-Type: text/html
Content-Length: 20
Host: localhost

test multi-threading
'''

message_delete2 = '''DELETE /testmulti.html HTTP/1.1
Host: localhost
Connection: close

'''
message_get2 = '''GET /testmulti.html HTTP/1.1
Accept: text/html
Accept-Language: it
User-Agent: Mozilla/4.0
Host: localhost
Connection: close

'''

try:
    # Create a TCP/IP socket
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.settimeout(2)
    socket2.settimeout(2)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 9999)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    socket1.connect(server_address)
    socket2.connect(server_address)

    print ('sending "%s"' % message_put1)
    socket1.sendall(message_put1)
    # Receive data
    data = readrequest(socket1)
    print >> sys.stderr, '%s' % data

    print ('sending "%s"' % message_get1)
    socket2.sendall(message_get1)
    # Receive data
    data = readrequest(socket2)
    print >> sys.stderr, '%s' % data

    time.sleep(5)

    print ('sending "%s"' % message_delete2)
    socket1.sendall(message_delete2)
    # Receive data
    data = readrequest(socket1)
    print >> sys.stderr, '%s' % data

    print ('sending "%s"' % message_get2)
    socket2.sendall(message_get2)
    # Receive data
    data = readrequest(socket2)
    print >> sys.stderr, '%s' % data

except socket.error:
    print ('Unable to connect to localhost on port 9999')

finally:
    # Closing the connection
    socket1.close()
    socket2.close()

