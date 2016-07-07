def unique_messages(messages):
    unique = {}
    for message in messages:
        if message["id"] not in unique:
            unique[message["id"]] = message["text"]
    return unique

messages = [
    {"id": 1, "text": "hi"},
    {"id": 1, "text": "hi"},
    {"id": 2, "text": "bye"},
]

assert unique_messages(messages) == {1: 'hi', 2: 'bye'}
