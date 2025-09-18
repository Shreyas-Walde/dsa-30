s = str(input("s: "))   # abcded
 

# precompute 
hash_arr = [0] * 256   # hash of 26 elements
for char in s:     # each char in string
    hash_arr[ord(char)] += 1 # autocast chr -> int
  
q = int(input("check no. "))   # 5
for _ in range(q):           
    character = input("character: ").strip()   
    # fetch
    print(hash_arr[ord(character)])   