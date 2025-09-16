def main(n):
     for i in range(n):
          for j in range(i+1):
            ch = chr(65+i)
            print(ch,end=' ')
                      
          print()

main(26)

def main(n):
     for i in range(1,n+1):
          for j in range(i):
               print(chr(65 +j),end=' ')
                      
          print()

main(5)
def main(n):
     num =1
     for i in range(1,n+1):
          for j in range(1,i+1):
               print(j,end=' ')
               num+=1
                      
          print()

main(4)