#!/bin/python3

import math
import os
import random
import re
import sys


def get_binary(result, i):
    while i > 1:
        print(i % 2)
        i = i // 2

# def get_xor(n, i):
#     return get_binary(n) ^ get_binary(i)

# Complete the sumXor function below.


# def sumXor(n):
#     count = 0
#     # for i in range(0, n):
#     if get_binary(n + 0) == get_xor(n, 0):
#         count += 1
#     return count


if __name__ == '__main__':
    print(get_binary('', 4))
    # print(sumXor(5))
