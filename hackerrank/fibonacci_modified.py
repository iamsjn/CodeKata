import math


def fibonacciModified(t1, t2, n):
    t3 = t1 + t2 ** 2
    if n <= 3:
        return t3
    return fibonacciModified(t2, t3, n - 1)


if __name__ == "__main__":
    print(fibonacciModified(0, 1, 5))
