# in python, functions are "first class"

# what does this mean?

# it means we can treat them more-or-less like any other python values (strings, numbers, lists, dicts.)

# well what can we do with values in general?

# we can assign them to different names

x = "hello world"

y = x

print y  # => hello world

# can we also do this with functions?


def greet(name):
    return "hello " + name

greet_someone = greet
print greet_someone("John")  # => hello John

# we can define new values and use them inside of functions:


def get_author(book):
    authors = {
        "Wuthering Heights": "Emily Brontë",
        "Catch-22": "Joseph Heller",
        "Wonderland": "Joyce Carol Oates"
    }
    return authors[book]

print get_author("Wonderland")

# can we do this with functions?


def greet_with_inner_function(name):
    def print_greeting():
        return "hello " + name
    return print_greeting()


print greet_with_inner_function("Alice")  # => hello Alice


# we can pass values as arguments and return values from functions


def add_three(x):
    x_plus_three = x + 3
    return x_plus_three


print add_three(4)  # => 7


# can we do both of these with functions?

# passing functions as arguments

import random


def give_me_a_facilitator():
    return random.choice(["James", "Lisa", "Rose", "Ginger"])


def greet_someone(get_name):
    name = get_name()
    return "hello " + name


# returning values from functions

def make_greeter(name):
    def greeter():
        return "hello " + name
    return greeter

rachel_greeter = make_greeter("Rachel")
print rachel_greeter()  # => hello Rachel


# hmm, could we write a function which both takes a function as an
# argument, and returns another function as it's return value?


def logged(func):
    def func_to_return():
        print "about to call func"
        print func()
        print "done calling func"
    return func_to_return


def hello():
    return "hello world"


greet_with_logging = logged(greet)
greet_with_logging()


# does this make sense?
# great, now you understand decorators!


@logged
def hello():
    return "hello world"

hello()


# what is going on here?

# a decorator is just a function that takes a function and returns
# another function. typically the function returned is a "modfied"
# version of the function passed in as an argument, which generally
# works by wrapping a call or calls to the function passed in

# the above is exactly equivalent to:

def hello():
    return "hello world"

hello = logged(hello)


# "decorating" a function definition with `@someotherfunction` just
# results in passing in the newly defined function into
# `someotherfunction` and then assigned the return value of that call
# to the name we specified in `def`.

# so when we call `hello`, we get the logging lines like we did before:

hello()


# note that what the decorator does with the function passed in can be
# anything or nothing at all. some examples:

def just_make_this_return_three_dammit(f):
    def returns_three():
        return 3
    return returns_three


@just_make_this_return_three_dammit
def add(x, y):
    return x+y

print add(10, 5) # => 3

# admitedely not very useful, but hopefully illustrative

# another one


def twice(f):
    def wrapped(x):
        return [f(x), f(x)]
    return wrapped


@twice
def square(x):
    return x * x

print square(4)  # => [16,16]


# misc useful things to know about decorators

# it's often handy to write decorators that accept and return
# functions which accept any number of arguments this can be done
# using python's "variadic arguments" feature, e.g. for our logging
# example before:

def logged(f):
    name = f.__name__
    def wrapper(*args):
        print "about to call {}".format(name)
        f(*args)
        print "done calling {}".format(name)
    return f


# now it works with any number of arguments!

@logged
def square(x):
    return return x*x


@logged
def add(x, y):
    return x + y


# if you read the source code of other people's decorators, you will
# often seen written using `functools.wraps` on the wrapper function.
# this is nothing magical, it just transfers metadata (like the
# __name__ attribute we used above) about the wrapped function onto
# the returned wrapper.

# to illustrate the problem:

print add.__name__  # => wrapper  :(


# we can fix it using this decorator:

from functools import wraps


def logged(f):
    name = f.__name__
    @wraps(f)
    def wrapper(*args):
        print "about to call {}".format(name)
        f(*args)
        print "done calling {}".format(name)
    return f


@logged
def add(x, y):
    return x + y

print add.__name__  # => add :)
