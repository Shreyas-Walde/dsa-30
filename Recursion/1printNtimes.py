def ntimes(i,n):
    if (i>n):
        return 
    print("hey")

    ntimes(i+1,n)   # Function call to print till i increments
    


def main():
    
    n = int(input("Enter how many times: "))
    ntimes(1,n)
    return 0

main()