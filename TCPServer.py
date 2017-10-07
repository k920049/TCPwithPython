# import socket module
from socket import *
# Prepare a sever socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('The server is ready to receive at port {}'.format(serverPort))
# iteration check variable
iteration = 0
while True:
    # Establish the connection
    iteration = iteration + 1
    print('Loop {}'.format(iteration))
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        message = message.decode()
        message = "ACK :" + message
        print(message)
        # encoding the string to raw byte-like object
        message = message.encode()
        connectionSocket.send(message)
    except OSError as msg:
        print(msg)
        connectionSocket.close()
        break
    except IOError as msg:
        print(msg)
        connectionSocket.close()
        break
serverSocket.close()
