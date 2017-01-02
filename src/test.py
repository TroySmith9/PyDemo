from functools import reduce


def fn(x, y):
    return x * 10 + y


print(fn(1, 2))
# print(list(reduce(fn, [1, 3, 5, 7, 9])))
