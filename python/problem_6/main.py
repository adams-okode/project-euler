"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def compute():
    nnos = range(1, 101)
    sq = sum(i**2 for i in nnos)  # sum of square
    qs = sum(list(nnos))**2

    return qs - sq


if __name__ == "__main__":
    print(compute())
