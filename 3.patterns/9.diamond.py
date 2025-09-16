R = 7
for i in range(R):
    for j in range(R-i-1):  # more spaces
        print(" ", end='')
    for k in range(2*i+1):
        print("*",end='')
    for l in range(R-i-1):
        print(" ", end='')

    for m in range(i):    # no spaces
        print(' ', end='')
    for n in range(2*R-(2*i+1)):
        print("#", end='')
    for o in range(i):
        print(' ', end='')
    print()

# ------------------------------------------------

N = 5                  # i = current line
for i in range(N):
    # spaces 
    for j in range(N-i-1):      # 0 spaces
        print(" ",end='') 
    # stars
    for k in range((2*i+1)):   
        print('*',end='')
    # spaces
    for l in range(N-i-1):      # 0 space
        print(" ",end='')
    print()


N = 5 
for i in range(N):
    # spaces
    for j in range(i):
        print(" ",end='')
    # stars
    for k in range(2*N-(2*i+1)):
        print('*',end='')
    # spaces
    for l in range(i):
        print(" ",end='')
    print()

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# -----------------------------------------------------------

for i in range(N):

    for j in range(N-i-1):      # 0 spaces
        print(" ",end='') 
    # stars
    for k in range((2*i+1)):   
        print('*',end='')
    
    for l in range(N-i-1):      # 0 space
        print(" ",end='')
    print()
        
        
for i in range(N):  # rows
    for j in range(i):
        print(' ', end='')  # spaces  
        
    for k in range(2*N - (2*i+1)): # stars
        print("*", end='')  # end ='' to print beside
            
    for l in range(i):
        print(' ', end='')
    print()
