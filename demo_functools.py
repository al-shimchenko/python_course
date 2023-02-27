import operator
from functools import reduce, lru_cache, partial


def mul(a, b):
    print(f'a = {a}, b = {b}')
    return a * b


def demo_reduce():
    print(sum(range(5)))
    result = reduce(lambda a, b: a + b, range(5))
    print(result)

    result = reduce(lambda a, b: a * b, [2, 4, 5, 9, 15])
    print(result)
    # or in a separated function:
    result = reduce(mul, [2, 4, 5, 9, 15])
    print(result)
    # or the best way - operator
    result = reduce(operator.mul, [2, 4, 5, 9, 15])
    print(result)

    line = reduce(operator.concat, ['abc', 'def', 'ghi'])  # concatenation of lines
    print(line)
    # shorter:
    line = "".join(['abc', 'def', 'ghi'])
    print(line)


@lru_cache  # decorator above the func
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def demo_fib():
    print(list(map(fib, range(40))))  # list of fib


def demo_partial():  # func with delayed parameters
    mul_2 = partial(mul, 2)
    print(mul_2(3))
    mul_3 = partial(mul, b=4)
    print(mul_3(3))

    print(pow(3, 2))  # degree
    print(pow(2, 3))
    pow_2 = partial(pow, exp=2)
    print(pow_2(3))
    print(pow_2(4))
    pow3to = partial(pow, 3)
    print(pow3to(4))


def main():
    demo_reduce()
    demo_fib()
    demo_partial()


if __name__ == "__main__":
    main()
