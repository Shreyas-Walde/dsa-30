def sum_n(i,sum):                  # (3,0)  2,3   1,5    0,6
    if  i<1:                       # No     no     no    yes 6
        print(sum)                                         # 6
        return sum                   
    
    return sum_n(i-1,sum+i)       # (2,3)  1,5    0,6


def main():
    n = int(input("Enter Int: "))  #   3
    sum_n(n,0)                     #  (3,0) 

main()


def factorial(i):
    if i == 1:
        return 1
    return i * factorial(i-1)


def main():
    n = int(input("Enter: "))
    print(factorial(n))

main()