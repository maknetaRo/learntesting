"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6
and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples_of_three_and_five(n):
    numbers = []
    for n in range(1, n):
        if n % 3 == 0:
            numbers.append(n)
        elif n % 5 == 0:
            numbers.append(n)
    return sum(numbers)


def main():
    print(multiples_of_three_and_five(1000))


if __name__ == "__main__":
    main()


