def reverse(n):
    revnum = 0

    while n>0:
        last_dig = n%10  # for 3451 -> 1
        revnum = revnum * 10 + last_dig

        n=n//10  # removing last number from n.
    
    return revnum

reverse(5432)