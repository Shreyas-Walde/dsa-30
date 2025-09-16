N=5
for i in range(N):
    # stars
    for k in range((i)):   
        print('*',end='')
    print()    
for i in range(N):  # rows
        
    for k in range(N - (i+1)): # stars
        print("*", end='')  # end ='' to print beside
    print()

###############################################################
print("------------------------#--------------------")

for i in range(2*N):  # 2n-1
    stars = i
    if (i>N): 
        stars = 2*N-i
    for j in range(stars):
        print("*",end='')
    print()

