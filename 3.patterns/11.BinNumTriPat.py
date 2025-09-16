
def main(n):
    start = 1
    for i in range(n):
        if (i%2==0): # for every even line 1 print first
            start=1
        else:
            start=0 
        for j in range(i+1):
            print(start,end='')
            start=1-start
        print()

main(5)