import itertools

def single_fib(n):
    """
    Calculate a single value of the fibonacci
    """
    return single_fib()

def fibonacci():
    raise NotImplementedError("implement me!")


assert list(itertools.islice(fibonacci(), 5)) == [0, 1, 1, 2, 3]
assert list(itertools.islice(fibonacci(), 10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert list(itertools.islice(fibonacci(), 20)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
# etc., etc.


# Thought: what if we want to take not a fixed number of values from the
# generator, but take them until some condition is met . . .

def take_until_greater_than(gen, n):
    """Exercise: write a generator that takes an iterable argument (gen),
    and an integer argument (n) and yields values from it until seeing
    a value that's greater than n.
    """
    raise NotImplementedError("implement me!")
