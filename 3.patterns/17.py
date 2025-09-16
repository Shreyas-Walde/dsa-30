def main(n):
    for i in range(n):       

        for j in range(n-i-1):      # spaces
            print(" ",end='') 

        ch = 65
        break_point = (2*i+1)//2  # breaking from the middle

        for j in range(2*i+1):       # characters
            print(chr(ch),end='')
            if j < break_point:    # middle increment/decrement
                ch+=1
            else:
                ch-=1        
        
        for j in range(n-i-1):      # spaces
            print(" ",end='')     

            
        print()
main(5)




