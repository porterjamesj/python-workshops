import socket


def receive_messages(port, maxsize):
    """
    Yield messages recieved on an address
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", port))
    while True:
        msg, _client_addr = s.recvfrom(maxsize)
        yield msg


for msg in receive_messages(4321, 1024):
    print msg
