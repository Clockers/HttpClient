def readrequest(s):
    buffer = ''
    data = 1
    try:
        while data:
            data = s.recv(64)
            buffer += data
    finally:
        return buffer