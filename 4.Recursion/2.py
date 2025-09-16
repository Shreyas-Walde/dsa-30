def tilln(i,n):
    if i>n:
        return 
    print(i)
    tilln(i+1,n)


def main():
    n = int(input("Number till: "))
    tilln(1,n)
    return 0

main()