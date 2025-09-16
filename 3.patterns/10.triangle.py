def main(N):
    for i in range(2*N):  # 2n-1
            stars = i
            if (i>N): 
                stars = 2*N-i
            for j in range(stars):
                print("*",end='')
            print()
main(5)