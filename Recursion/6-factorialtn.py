def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


def main():
    n = int(input("Enter int: "))
    print(fact(n))

main()