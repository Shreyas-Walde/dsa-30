s = str(input("s: "))   # abcded
 

# precompute 
hash_arr = [0] * 26   # hash of 26 elements
for char in s:     # each char in string
    hash_arr[ord(char) - ord('a')] += 1 # autocast chr -> int
     #        'a' - 'a'     = increases counter in hash_arr
     #        a = 1   
q = int(input("check no. "))   # 5
for _ in range(q):           
    character = input("character: ").strip()   # a  b d
    # fetch
    print(hash_arr[ord(character)-ord('a')])   # 1  1 2