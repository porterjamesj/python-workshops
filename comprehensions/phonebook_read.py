import os


def phonebook_load(filename):
    """load phonebook from file"""
    pb = {}
    with open(filename) as f:
        for line in f:
            name, number = line.rstrip('\n').split()
            pb[name] = number
    return pb

phonebook_path = os.path.join(os.path.dirname(__file__), "phonebook.txt")

assert phonebook_load(phonebook_path) == {'james': '4402269590', 'jenny': '8765309'}
