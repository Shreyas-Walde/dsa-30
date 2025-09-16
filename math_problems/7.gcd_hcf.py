def findgcd(n1,n2):

    gcd=1

    for i in range(1, min(n1,n2)+1):
        if n1%i== 0 and n2%i==0:  # checkc common divisor
            gcd =i   # stores in gcd
            
    print(gcd,end='') 

findgcd(6,18)


def eucligcd(a,b):
    while a>0 and b>0:

        if a > b:
            a = a % b
        else:
            b = b % a
        
    if a == 0:
        return b
    return a

def main():
    n1 = 20
    n2 = 15

    # Find the GCD of n1 and n2
    gcd = eucligcd(n1, n2)

    print(f"GCD of {n1} and {n2} is: {gcd}")


if __name__ == "__main__":
    main()
