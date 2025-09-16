# better approach 
def symmetry(n):
    # Write your solution here.
    for i in range(1,2*n):   # 2xn-1
        # left stars
        stars=i
        if(i>n):
            stars= 2*n - i
        for j in range(stars):
            print("*",end='')
        
        # spaces
        spaces=2*n-2
        for j in range(1,spaces+1):
            print(" ",end='')

        # stars
        for j in range(stars):
            print("*",end='')
        
        spaces-=2
        print()
        if (i<n):
            spaces -=2
        else:
            spaces +=2

symmetry(6)