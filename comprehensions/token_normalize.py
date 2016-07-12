from string import printable


def normalize_individual_text(tokens):
    '''Given tokens, a list of strings of all words in a text, returns a
    normalized list of tokens.
    '''
    lowercased_list_of_tokens = []
    for token in tokens:
        clean_token = []
        for c in token:
            if c in printable:
                clean_token.append(c.lower())
        lowercased_list_of_tokens.append(''.join(clean_token))
    return lowercased_list_of_tokens


example_input = ["Hi", "there", ".", chr(0) + chr(1) + "Asdf"]
example_output = ["hi", "there", ".", "asdf"]
assert normalize_individual_text(example_input) == example_output
