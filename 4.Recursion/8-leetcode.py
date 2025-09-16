# my leetcode solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s)-1

        while left < right:
# check if not alphanumeric    - isalnum()  -> a b 3 4
            if not s[left].isalnum():  # if not alphanumeric
                left+=1   # just skip it (inwards)

            elif not s[right].isalnum():  # not alphanumeric not right
                right-=1  # skip (inwards)
        
            elif s[left].lower() != s[right].lower():  # left not = right
                return False    # false
# if true
            else:
# move forward
                left+=1
# move backward
                right-=1
        return True