def prime_numbers(n):
    """
    Returns all prime numbers lower or equal to n.
    """
    prime_num = []
    if n < 2:
        return False
    for i in range(2, n + 1):
        if i == 2 or i == 3 or i == 5 or i == 7:
            prime_num.append(i)

        if i < n+1 and (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
            prime_num.append(i)

    return prime_num


x = prime_numbers(568)


def main():
    print(x)


if __name__ == "__main__":
    main()


