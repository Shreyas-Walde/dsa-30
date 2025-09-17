n = int(input("n: "))
arr = list(map(int,input("example[1,2,3]: ").split()))
    

# precompute 
hash_arr = [0] * 13
for i in range(n):
    hash_arr[arr[i]]+=1

q = int(input("check no. "))
for _ in range(q):
    number = int(input("number: "))
    # fetch
    print(hash_arr[number])