n = int(input("n: ")) # 1 2 3 2 1
arr = list(map(int,input("example[1,2,3]: ").split())) # [1,2,3,2,1]
    

# precompute 
hash_arr = [0] * 13 # [0,0,0,0,0,0,0,0,0,0,0,0,0,0]  zero index
for i in range(n): # looping through n
    hash_arr[arr[i]]+=1 # [{1:2},{2:2},{3:1}]

q = int(input("check no. "))           # no. of checks -> 3 
for _ in range(q):            # 3 value 
    number = int(input("number: "))     # check if 1 is present            2  3 
    # fetch  
print(hash_arr[number])               #  2                             2  1