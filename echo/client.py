# echo client


import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# In comparison to the server, the client is pretty simple.
# It creates a socket object, uses .connect() to connect to the server and calls s.sendall() to send its message.
# Lastly, it calls s.recv() to read the server’s reply and then prints it.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")