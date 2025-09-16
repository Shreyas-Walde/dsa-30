def main(n):
    for i in range(n+1):
        for j in range(i):
            ch = 65 + n-1  #end
            print(chr(ch-j), end='  ')
            
        print()

main(5)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# Solution below:
def main(n):
    for i in range(n):
        start = 65 + n-1 -i
        end =   65 + n-1
        for ch in range(start,end+1):
            print(chr(ch), end='  ')
            
        print()

main(5)


# reference

def main(n):
    for i in range(n+1):
        for j in range(i+1):
            
            print(j, end='')
        print()

main(5)