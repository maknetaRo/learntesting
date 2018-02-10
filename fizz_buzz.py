def fizz_buzz(n):
    result = []
    for elem in range(1, n):
        number = ""
        if elem % 3 == 0:
            number += "Fizz"
        if elem % 5 == 0:
            number += "Buzz"
        if elem % 3 != 0 and elem % 5 != 0:
            number = str(elem)
        result.append(number)
    return result


def main():
    print("\n".join(fizz_buzz(101)))

if __name__ == "__main__":
    main()
