import random
import time


def random_list(n):
    return [random.random() for _ in range(n)]


def insertion_sort(xs):
    result = []
    for x in xs:
        if not result:
            result.append(x)
        else:
            for i, r in enumerate(result+[float("inf")]):
                if r > x:
                    break
            result.insert(i, x)
    return result


def quick_sort(xs):
    if len(xs) <= 1:
        return xs
    pivot = xs[0]
    left = []
    right = []
    for x in xs[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)


# task: refactor this by writing a decorator for printing out timing
# information and annotating the sorting functions above with it, such
# we don't have to have any timing related code in the loop below

def measure_timings():
    for sort_function in [insertion_sort, quick_sort]:
        for size in [10, 100, 1000, 10000]:
            start = time.time()
            sort_function(random_list(size))
            end = time.time()
            total_time = end - start
            print "sorting list of size {} with {} took {} milliseconds".format(
                size, sort_function.__name__, total_time*1000
            )
