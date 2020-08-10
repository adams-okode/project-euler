"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3sq + 4sq = 9 + 16 = 25 = 5sq

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def compute():
    perimiter = 1000
    for a in range(1, perimiter):
        for b in range(a+1, perimiter):
            c = perimiter-a-b
            if a**2 + b**2 == c**2:
                return a*b*c


if __name__ == "__main__":
    print(compute())
