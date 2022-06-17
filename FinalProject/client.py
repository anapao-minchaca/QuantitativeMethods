# echo-client.py

import socket
#using loopback address
HOST = "127.0.0.1" 
#using random port to communicate with server 
PORT = 65432  
"""_summary_:
    We create a socket to send our information to the server side
    we connect with host address and port to the server'
    Then we send our message and 
    When our connection is closed we print our data from the server
"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((HOST, PORT))
    for i in range(0,12):
        message = 'Mensaje'+str(i+1)+' '
        s.sendall(bytes(message, 'utf-8'))
    data = s.recv(2048)

print(f"Received {data!r}")