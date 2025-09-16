def isPalindrome(s):
    left = 0
    right = len(s)-1  # last element (zero indexing) 

    while left < right:
# Checks: Is the character at left NOT alphanumeric?
        if not s[left].isalnum(): # anything other than letter/number
            left+=1               # Skip it by doing
# same for right
        elif not s[right].isalnum():
            right-=1

        elif s[left].lower() != s[right].lower():  
# if left and right not equal -> False
            return False
# if -> True
        else:
            left+=1       # move character to left (inwards)
            right-=1      # move right (inwards)
    return True

if __name__ == "__main__":
    str = "ABCTCBA"
    ans = isPalindrome(str)


    if ans == True:
        print("Palindrome")
    else:
        print("Not Palindrome")