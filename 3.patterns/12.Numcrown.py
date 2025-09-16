
def main(n):
    spaces = 2*(n-1)
    for i in range(1,n+1):  # outer loop
        
        for j in range(1,i+1):   # Number
            print(j,end='')

        for j in range(1,spaces+1):   # Spaces
            print(' ',end='')
        
        for j in range(i,0,-1):  # Number
            print(j, end='')
        
        spaces-=2
        print()

main(9)