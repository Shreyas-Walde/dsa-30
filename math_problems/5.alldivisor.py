def divisors(n):
    
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=' ')
    
divisors(2)


import math
def finddivisors(n):
    divisor = []

    # using math to find square of n
    # sqrtN = int(math.sqrt(n))
    sqrtN = int(n ** 0.5)

    for i in range(1,sqrtN+1):
        if n % i == 0:
            divisor.append(i)

            if i != n//i:      # add once if reached to sqrt
                divisor.append(n//i)
    
    return sorted(divisor)


if __name__ == "__main__":
    number = 36
    divisors = finddivisors(number)
    print("Divisors of", number, "are:", end=' ')
    for divisor in divisors:
        print(divisor, end=' ')
    print()