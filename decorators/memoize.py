import os


def count_bytes_in_directory(path):
    path = os.path.abspath(os.path.expanduser(path))
    total = 0
    for dirpath, _, filepaths in os.walk(path):
        for filepath in filepaths:
            abspath = os.path.join(dirpath, filepath)
            total += os.path.getsize(abspath)
    return total


# task: refactor this code to use a "caching decorator", so that the
# caching happens implicitly whenever this function is called, rather
# than us having to write it explicilty at every call site


CACHE = {}
while True:
    path = raw_input().strip()
    if path in CACHE:
        print CACHE[path]
    else:
        total = count_bytes_in_directory(path)
        CACHE[path] = total
        print total
