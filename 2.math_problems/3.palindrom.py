def palindrome(n):
    duplicate = n
    reverse = 0

    while n>0:
        last_dig = n % 10  # 3352 -> 2
        n = n//10 # 3352 -> 335

        reverse = reverse * 10 + last_dig

    
    if duplicate == reverse:
        print("True")
    else: 
        print("False")

palindrome(123321)