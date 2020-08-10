"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

thought 
------
L.C.M. = (a×b)/gcd(a,b)
"""


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def compute():
    numbers = list(range(1, 21))
    res = 1
    for v in numbers:
        res *= v // gcd(v, res)
    return res


if __name__ == "__main__":
    print(compute())
