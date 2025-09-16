def armstrong(n):
    duplicate = n
    sum = 0

    while n>0:
        last_dig =  n % 10
        n = n//10 
        sum += (last_dig**3) 

    if duplicate == sum:
        print("palindrome")
    else:
        print("not")

armstrong(371)