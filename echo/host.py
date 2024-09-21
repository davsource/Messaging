# echo server
import socket

host = '127.0.0.1'
# host can be a hostname, IP address, or empty string.
# If an IP address is used, host should be an IPv4-formatted address string.
# The IP address 127.0.0.1 is the standard IPv4 address for the loopback interface, so only processes on the host will be able to connect to the server.
# If you pass an empty string, the server will accept connections on all available IPv4 interfaces.

port = 65432
# Port represents the TCP port number to accept connections on from clients.
# It should be an integer from 1 to 65535, as 0 is reserved.
# Some systems may require superuser privileges if the port number is less than 1024.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # socket.socket() creates an object that supports the context manager type, so you can use it in a with statement. There’s no need to call s.close()
    # The arguments passed to socket() are constants used to specify the address family of the socket type.
    # AF_INET is the Internet address family for IPV4, SOCK_STREAM is the socket type for TCP.
    
    s.bind((host, port))
    # The .bind() method is used to associate the socket with a specific network interface and port number.
    # The values passed to  .bind() depend on the address family of the socket.
    # Since we are using socket.AF_INET (IPV4), it expects a two-tuple: (host, port).
    
    s.listen()
    #The .listen() method has a backlog parameter. It specifies the number of unaccepted connections that the system will allow before refusing new connections.
    # Starting in Python 3.5, it’s optional. If not specified, a default backlog value is chosen.
    # If your server receives a lot of connection requests simultaneously, 
    # increasing the backlog value may help by setting the maximum length of the queue for pending connections.
    
    connection, address = s.accept()
    # The .accept() method blocks execution and waits for an incoming connection.
    # When a client connects, it returns a new socket object representing the connection and a tuple holding the address of the client.
    # The tuple will contain (host, port) for IPv4 connections or (host, port, flowinfo, scopeid) for IPv6.
    # One thing that’s imperative to understand is that you now have a new socket object from .accept().
    # This is important because it’s the socket that you’ll use to communicate with the client.
    # It’s distinct from the listening socket that the server is using to accept new connections.
    
    with connection:
        print(f'Connected by {address}!')
        
        while True:
            data = connection.recv(1024)
            
            if not data:
                break
            
            connection.sendall(data)
        
        # After .accept() provides the client socket object conn, an infinite while loop is used to loop over blocking calls to connection.recv().
        # This reads whatever data the client sends and echoes it back using connection.sendall().
        
        # If connection.recv() returns an empty bytes object, b'', that signals that the client closed the connection and the loop is terminated.
        # The with statement is used with conn to automatically close the socket at the end of the block.