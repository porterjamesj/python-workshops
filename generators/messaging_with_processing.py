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


def capitalize(strings):
    for string in strings:
        yield string.strip().upper()


def running_total(strings):
    total = 0
    for s in strings:
        total += len(s)
        yield s, total


for msg, total in running_total(capitalize(receive_messages(4321, 1024))):
    print msg
    print "total is: ", total
