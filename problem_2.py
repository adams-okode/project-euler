def compute():
    sequence = [1, 2, 3]
    index = 2
    while len(sequence) < 4000000:
        current = sequence[1] + sequence[index]
        if current % 2 == 0:
            sequence.append(current)
        index += 1
    return sum(sequence)


if __name__ == "__main__":
    print(compute())
