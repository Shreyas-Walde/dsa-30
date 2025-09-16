def count(n):
    count = 0  # counter 
    
    while (n>0):
        count+=1
        n = n//10
    print(count)

count(344255)

def reverse(n):
    rev = 0
    while n>0:
        last_dig = n%10
        rev = (rev *10) + last_dig
        n=n//10  # removes the last digit
    print(rev)
reverse(4532)