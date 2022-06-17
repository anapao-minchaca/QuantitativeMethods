import socket
import  sys
#using loopback address
HOST = "127.0.0.1"  
#using random port
PORT = 65432  
"""_summary_:
    We create a socket to start our server- client communication
    We add our FAST OPEN TCP protocol to our sockte to ensurre that the protocol is being used
    We open our socket to listen to the clients message
    Once we receive our message it closes our connection
    This FAST OPEN TCP was tested on linux and Mac
    With Mac OS we can't ensure that FAST OPEN TCP works
"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM,socket.SOL_TCP) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if(sys.platform.startswith('linux')):
        s.setsockopt(socket.SOL_TCP, socket.TCP_FASTOPEN, 5)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(3000)
            if not data:
                break
            conn.sendall(data)