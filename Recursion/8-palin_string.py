def ispalindrome(i:int,s:str) -> bool:
    
    if i>= len(s)//2:
        return True
    if s[i] != s[len(s)-i-1]:
        return False
    return ispalindrome(i+1,s)


def main():
    s = "MADAM"
    s= s.lower()
#   n = len(s)
    print(ispalindrome(0,s))

if __name__ == "__main__":
    main()