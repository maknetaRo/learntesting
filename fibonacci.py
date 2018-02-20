def fibonacci(n):
    """
    Returns a list of numbers in fibonacci sequence - the next element is a sum of two previous elements.
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def main():
    print(fibonacci(100))


if __name__ == "__main__":
    main()