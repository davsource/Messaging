# Echo Server

An echo server is a simple type of network server that sends back (or echoes) any message it receives from a client. It serves as a basic example for understanding socket programming and network communication.

Creating an echo server in Python involves setting up a TCP connection where the server binds to a specific IP address and port. Once connected, the server enters a loop that continuously accepts client requests, processes them, and responds with the same message.

This type of server is ideal for testing purposes, demonstrating the basic concepts of network I/O, and can be expanded into more complex systems by adding additional logic or features such as message parsing, security, or multi-client handling.

## Socket Installation

The `socket` module is a part of Python's standard library and comes pre-installed with any Python distribution. This means you don't need to install any external packages or libraries to use it.

## Usage

In Python, echo servers are typically implemented using the `socket` module, which provides access to the low-level networking interface. The server listens for incoming connections from clients, reads the data sent by the client, and immediately sends that same data back.

This behavior allows developers to test communication and ensure the server can handle data transmission effectively.

## Viewing Socket State

### Read this after you've looked through and ran all of the source in `echo`.

To see the current state of sockets on your host, use netstat. It’s available by default on macOS, Linux, and Windows.

Here’s the netstat output from macOS after starting the server:

```shell
$ netstat -an
Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
tcp4       0      0  127.0.0.1.65432        *.*                    LISTEN
```

Notice that the `Local Address` 127.0.0.1.`65432`. If `host.py` had used `HOST = ""` instead of `HOST = "127.0.0.1"`, netstat would show this:

```shell
$ netstat -an
Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
tcp4       0      0  *.65432                *.*                    LISTEN
```

`Local Address` is `*.65432`, which means all available host interfaces that support the address family will be used to accept incoming connections. In this example, `socket.AF_INET` was used (IPv4) in the call to `socket()`. You can see this in the Proto column: `tcp4`.

The output above is trimmed to show the echo server only. You’ll likely see much more output, depending on the system you’re running it on. The things to notice are the columns `Proto`, `Local Address`, and `(state)`. In the last example above, netstat shows that the echo server is using an IPv4 TCP socket `(tcp4)`, on port 65432 on all interfaces `(*.65432)`, and it’s in the listening state `(LISTEN)`.

Another way to access this, along with additional helpful information, is to use lsof (list open files). It’s available by default on macOS and can be installed on Linux using your package manager, if it’s not already:

```shell
$ lsof -i -n
COMMAND     PID   USER   FD   TYPE   DEVICE SIZE/OFF NODE NAME
Python    67982 David    3u  IPv4 0xecf272      0t0  TCP *:65432 (LISTEN)
```

`lsof` gives you the `COMMAND`, `PID` (process ID), and `USER` (user ID) of open Internet sockets when used with the `-i` option. Above is the echo server process.

`netstat` and `lsof` have a lot of options available and differ depending on the OS that you’re running them on. Check the `man` page or documentation for both. They’re definitely worth spending a little time with and getting to know. You’ll be rewarded. On macOS and Linux, use `man` `netstat` and `man lsof`. For Windows, use `netstat /?`.

Here’s a common error that you’ll encounter when a connection attempt is made to a port with no listening socket:

```shell
$ python echo-client.py 
Traceback (most recent call last):
  File "./echo-client.py", line 9, in <module>
    s.connect((HOST, PORT))
ConnectionRefusedError: [Errno 61] Connection refused
```

Either the specified port number is wrong or the server isn’t running. Or maybe there’s a firewall in the path that’s blocking the connection, which can be easy to forget about. You may also see the error `Connection timed out`. Get a firewall rule added that allows the client to connect to the TCP port!

# Communication Breakdown

Now you’ll take a closer look at how the client and server communicated with each other:

![](https://realpython.com/cdn-cgi/image/width=1134,format=auto/https://files.realpython.com/media/sockets-loopback-interface.44fa30c53c70.jpg)

When using the loopback interface (IPv4 address `127.0.0.1` or IPv6 address `::1`), data never leaves the host or touches the external network. In the diagram above, the loopback interface is contained inside the host. This represents the internal nature of the loopback interface and shows that connections and data that transit it are local to the host. This is why you’ll also hear the loopback interface and IP address `127.0.0.1` or `::1` referred to as “localhost.”