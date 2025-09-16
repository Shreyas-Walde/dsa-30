def twoloop(N):
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
    
twoloop(6)