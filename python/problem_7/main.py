"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def is_prime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True


def compute():
    n = 0
    prime = 0
    while n <= 10001:
        if not is_prime(prime):
            n += 1
        prime += 1
    return prime


if __name__ == "__main__":
    print(compute())
