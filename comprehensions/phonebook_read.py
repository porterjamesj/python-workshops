import os


def phonebook_load(filename):
    """load phonebook from file"""
    f = open(filename)
    {name: number for name, number in
     [line.rstrip("\n").split() for line in f]}
    f.close()

phonebook_path = os.path.join(os.path.dirname(__file__), "phonebook.txt")

assert phonebook_load(phonebook_path) == {'james': '4402269590', 'jenny': '8765309'}
