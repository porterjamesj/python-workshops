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

# the above is exactly equivalent to:

def hello():
    return "hello world"

hello = logged(hello)





# examples

# timing
# retrying (set up flaky server on my vps to use as an example?)
# memoize
#
