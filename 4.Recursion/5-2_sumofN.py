# Using Functional way

def sum(n):                 # 3           2       1            0 
    if n == 0:               # No          NO      NO           Yes 
        return 0  
    
    return n + sum(n-1)     # 3 + f(2)   2+f(1)    1+f(0)           f(n-1) is waiting till it solved
                            #    6            3         1          

# 6
def main():
    n = int(input("Enter n: "))   # 3
    print(sum(n))
main()