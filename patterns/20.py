def twoloop(N):
    b_inis = 2*N-2 
    for i in range(1,N): # Bottom Pattern
        # left stars
        for j in range(i):
            print("*",end='') 

        # spaces
        for k in range(b_inis):
            print(" ",end='')

        # right stars 
        for j in range(i):
            print("*",end='')
            
        b_inis-=2
        print()

    top_inis=0 # initial spaces
    for i in range(N):  # Top patter
        # left stars
        for j in range(N-i):
            print("*",end='')

        # spaces
        for k in range(top_inis):
            print(" ", end='')
                  
        # right stars
        for j in range(N-i):
            print("*",end='')

        top_inis+=2
        print()

twoloop(6)



# better approach 
def symmetry(n):
    # Write your solution here.
    for i in range(1,2*n):   # 2xn-1
        # left stars
        stars=i
        if(i>n):
            stars= 2*n - i
        for j in range(stars):
            print("*",end=' ')
        
        # spaces
        spaces=2*n-2
        for j in range(spaces):
            print(" ",end='')
        # stars
        stars=i
        if(i>n):
            stars= 2*n - i
        for j in range(stars):
            print("*",end=' ')
        
        spaces-=2
        print()

symmetry(6)