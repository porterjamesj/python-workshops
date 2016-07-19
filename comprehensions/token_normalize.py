from string import printable


def clean_single_token(token):
    return ''.join([c.lower() for c in token if c in printable])


def normalize_individual_text(tokens):
    '''Given tokens, a list of strings of all words in a text, returns a
    normalized list of tokens.
    '''
    return [clean_single_token(token) for token in tokens]


example_input = ["Hi", "there", ".", chr(0) + chr(1) + "Asdf"]
example_output = ["hi", "there", ".", "asdf"]
assert normalize_individual_text(example_input) == example_output
