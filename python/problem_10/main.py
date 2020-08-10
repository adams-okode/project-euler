def compute():
    _sum = 17
    n = 11

    while n < 100:
        if (n % 2) != 0 and (n % 3) != 0 and (n % 5) != 0 and (n % 7) != 0:
            _sum+=n
        if ((n+2) % 2) != 0 and  ((n+2) % 3) != 0 and  ((n+2) % 5) != 0 and  ((n+2) % 7) != 0:
            _sum+=(n+2)
        n += 6

    return _sum


if __name__ == "__main__":
    print(compute())
