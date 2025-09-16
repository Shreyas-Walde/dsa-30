def recursion(i,n):  # (3,3)     (2,3)     (1,3)      (0,3)
    if i<1:          # (3<1)fals  2<1fals   1<1fals    0<1true 
        return                                      # return   
    recursion(i-1,n) # (2,3)      (1,3)    (0,3)   
    print(i)          # 3          2         1        

def main():
    n = int(input("Enter n: "))
    recursion(n,n)   # (3,3)

main()