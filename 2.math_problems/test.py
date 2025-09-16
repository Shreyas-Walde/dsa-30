def hcf(a,b):
    while a>0 and b>0:
        if a>b:
            a= a%b
        else: 
            b = b% a

    if a == 0: 
        return b
    return a


def main():
    n1 = 20
    n2 = 15

    # Find the GCD of n1 and n2
    gcd = hcf(n1, n2)

    print(f"GCD of {n1} and {n2} is: {gcd}")


if __name__ == "__main__":
    main()