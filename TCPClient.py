# import socket module
from socket import *
# Prepare a client socket
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# Message to send
sentence = input('Enter your student id:')
sentence = sentence.encode()
try:
    # Sending the message
    clientSocket.send(sentence)
    # Ready to receive a message from the server
    sentence = clientSocket.recv(1024)
    print(sentence)
except OSError as msg:
    print(msg)
except IOError as msg:
    print(msg)
clientSocket.close()
