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

# try this out by running `echo "foo" | nc -u -w0 $ADDRESS 4321`, where
# address is the address it's being run on
#
# challenge: change the above code by wrapping the call to
# `recieve_messages` in a generator that, given a string yields a
# dictionary with running word counts of all the strings it's seen so
# far, then print out the running totals in the loop.
#
# e.g. after recieveing "hello world", it yields {"hello": 1, "world": 1}
# if it the recieves "hello generators", it yields {"hello": 1, "world": 2, "generators": 1}, etc., etc.
#
# test that this works with the person sitting next to you! :)
