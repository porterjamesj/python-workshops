# N.B. this is almost entirely copied from
# http://www.dabeaz.com/generators-uk/GeneratorsUK.pdf, which is a
# great resource that covers this stuff in much more detail than I
# have time to, you should check it out!


# Iteration

# Python has `for` statement, you can iterate over stuff with it:


for x in [1, 4, 5, 10]:
    print x

# as you may have noticed, you can iterate over a lot of different
# things, not just lists:

# iterating over dictionaries, you get keys

prices = {'GOOG': 490.10,
          'AAPL': 145.23,
          'YHOO': 21.71}

for key in prices:
    print key


# iterating over strings, you get chars

s = "Yow!"
for c in s:
    print c


# iterating over a file, you get lines

for line in open("mutliated_world.txt"):
    print line


# many functions work on any "iterable" object, e.g.

print sum([1, 2, 3])
print sum({1: "a", 2: "b", 3: "c"})

# other functions that work like this include, min, max,
# constructors like list, dict, set,

# key idea: the only reason we can iterate over lots of different
# things is that they all support a common "iteration protocol"

items = [1, 4, 5]
it = iter(items)
it.next() # => 1
it.next() # => 4
it.next() # => 5
it.next() # => StopIteration

# protocol says "how" to iterate over something

# this works on *all* iterable objects

stuff = {"a": 1, "b": 2, "c": 3}
it = iter(stuff)
it.next() # => "a"
it.next() # => "b"
it.next() # => "c"
it.next() # => raise StopIteration


# we could do the same thing on files, strings, etc., etc.

# so how do for loops work then:


for x in obj:
    print x


# is translated to:


_iter = iter(obj)  # Get iterator object
while True:
    try:
        x = _iter.next()  # Get next item
    except StopIteration:  # No more items
        break
    print x


# any object that supports iter() and next(), we call "iterable"

# you can write your own iterable objects!
# we're going to skip that for today, but it is pretty cool



# Generators


# A generator is a function that produces a sequence of results
# instead of a single value


def countdown(n):
    while n > 0:
        yield n
        n -= 1


# rather than `return`ing a single value, we generate a series of
# values, using `yield`

# the behavior of a generator is very different than a normal
# function. calling a generator creates a generator object, but
# doesn't start running the function:


def countdown(n):
    print "Counting down from", n
    while n > 0:
        yield n
        n -= 1

# generators are iterable


for i in countdown(5):
    print i


x = countdown(10)  # doesn't print anything

x # => <generator object at 0x...>


# generators only start executing on first call to `next`:

x.next()  # this prints the "Counting down from" message, and returns 10


# yield produces a value, and then suspends execution of the
# function. execution restarts on next call to `next`

x.next() # => 9
x.next() # => 8
# etc., etc.

# when generator returns, iteration stops:

x.next()  # => raise StopIteration (eventually)


# generator functions are mostly just more convenient ways of writing
# iterators

# you don't have to worry about the iterator protocol (iter and next
# and all that), it just works

# Generator Expressions

# like a list comprehension, but constructs a generator, rather than a
# list

a = [1, 2, 3, 4]
b = (2*x for x in a)

for i in b:  # => 2, 4, 6, 8
    print b
